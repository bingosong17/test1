import threading
import time
import logging
from django.shortcuts import render
from rest_framework import status
from rest_framework import views
from rest_framework.response import Response

from .sendmail import *
from .serializers import *
from .reportTodd import *


def doCmd(cmd, agrstr, parmsDic, data, original_path):
    """
    :param parmsDic: 参数集合
    :param data: 用于接口的返回数据，提取中间的report使用
    :param original_path:
    :param agrstr: 命令执行的参数
    :param cmd: 命令
    """
    res = os_do_cmd(cmd, agrstr)
    print(res)
    # 生成html报告后，先修改报告中css的路径，否则显示乱码
    if data['report']:
        while True:
            try:
                changeReportCssPath(data['report'])
                break
            except:
                time.sleep(1)
                continue

    # 删除拷贝出来的执行项目
    pathpart = parmsDic['path'].split("/")
    if "ppy" in pathpart[0]:
        arg = "-rf " + pathpart[0]
    else:
        # "ppy" in pathpart[1]:
        arg = "-rf " + pathpart[1]

    os_do_cmd("rm", arg)

    if parmsDic['ding']:
        result = get_script_result(data['report'])
        text_cont = original_path + "\n" + result["result"]
        send_msg(parmsDic['webhook'], parmsDic['secret']) \
            .send_link('脚本运行结果', text_cont,
                       data['url'])
    return res


class HttpRunnerView(views.APIView):
    def post(self, request):
        """
        httprunner命令下发
        session和password至少上传一个。session上传通常由前端进行，password由接口
        ding参数作为是否发送脚本结果到钉钉群
        webhook和secret两个参数为钉钉群参数，设置默认值，可不上传
        """
        serializer = HttpRunnerTestSerializer(data=request.data)
        reportname = timeStr() + ".html"
        parmsList = ['env', 'cityCode', 'phone', 'password', 'session',
                     'path', 'ding', 'webhook', 'secret']
        if serializer.is_valid():
            parmsDic = {}
            for i in parmsList:
                parmsDic[i] = serializer.validated_data.get(i)
            original_path = parmsDic['path']
            # 复制一个备份的httprunner项目使用
            parmsDic['path'] = copyHttprunnerProject(parmsDic['path'])
            if parmsDic['path'] == 1:
                return Response(data={"message": "httprunner执行项目复制失败！"},
                                status=status.HTTP_400_BAD_REQUEST)
            elif parmsDic['path'] == 2:
                return Response(data={"message": "脚本路径不存在，请检查！"},
                                status=status.HTTP_400_BAD_REQUEST)
            pathpart = parmsDic['path'].split("/")
            envpath = pathpart[1] + "/env.py"

            # 提取写入env.py的参数，并写入
            if parmsDic['session'] is not None:
                sessionpath = pathpart[1] + "/envAll/envPPYApp.py"
                userid = parmsDic['env'] + parmsDic['cityCode'] + parmsDic['phone']
                with open(sessionpath, encoding='utf-8') as f:
                    lines = f.readlines()
                    s = None
                    for line in lines:
                        # 如果找到过期session，删除，重写
                        if userid in line and parmsDic['session'] not in line:
                            lines.remove(line)
                            strings = "'" + userid + "' : ['" + parmsDic['session'] + "'],\n"
                            lines.insert(1, strings)  # 插入第二行
                            s = ''.join(lines)
                            break
                        # 如果找到session，未过期，直接跳过
                        elif userid in line and parmsDic['session'] in line:
                            s = ''.join(lines)
                            break

                    if not s:
                        strings = "'" + userid + "' : ['" + parmsDic['session'] + "'],\n"
                        lines.insert(1, strings)  # 插入第二行
                        s = ''.join(lines)
                    with open(sessionpath, "w", encoding='utf-8') as f:
                        print(s)
                        f.write(s)
            # 其他配置参数写入env.py
            s = ''
            for parm in parmsList:
                if parmsDic[parm] is None:
                    parmsDic[parm] = ''
                s = parm + " = '" + str(parmsDic[parm]) + "'\n" + s
            with open(envpath, "w") as f:
                f.write(s)
            # 如果目标路径指向文件
            if os.path.isfile(parmsDic['path']):
                try:
                    """
                    1、复制项目内的ppy/envAll/scriptModel.py，到副本
                    2、关键信息写入到scriptModel.py副本，返回修改后的地址，供运行
                    """
                    scriptModel_path = pathpart[1] + "/envAll/scriptModel.py"
                    pathpart[-1] = pathpart[-1][0:-3]
                    # script_route  脚本引入路径 script_alias 脚本别名 script_class 脚本类名 script_datas 脚本参数
                    modify_datas = {"script_route": ".".join(pathpart[2:]),
                                    "script_alias": pathpart[-1][0:-5],
                                    "script_class": findString(parmsDic['path'], "class ", "\(HttpRunner\):"),
                                    "script_datas": serializer.validated_data.get("scriptData")}
                    parmsDic['path'] = modifyModel(scriptModel_path, modify_datas)
                except:
                    data = {"message": "脚本不存在或其他错误"}
                    return Response({"statusCode": 4000, "body": data},
                                    status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                # 执行脚本命令从web发起
            agrstr = parmsDic['path'] + ' --html=./templates/' + reportname
            data = {}
            data['message'] = "命令下发成功，稍后请使用以下链接查看结果"
            data['url'] = "https://autotestserver.pinpianyi.com/{}".format(reportname)
            data['report'] = reportname
            try:
                t = threading.Thread(target=doCmd, args=("hrun", agrstr, parmsDic, data, original_path))
                t.start()
            except:
                return Response({"statusCode": 5000, "body": {"message": "命令执行失败"}},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            return Response({"statusCode": 2000, "body": data},
                            status=status.HTTP_200_OK)
        else:

            return Response(data={"message": dict(serializer.errors)},
                            status=status.HTTP_400_BAD_REQUEST)


class GetCurrentPathView(views.APIView):
    """
    获取当前服务器内部执行路径，用于调试验证
    """

    def get(self, request):
        try:
            res = os.getcwd()
            return Response(data={"statusCode": 2000, "body": res}, status=status.HTTP_200_OK)
        except:
            return Response(data={"message": "出错了，请检查代码"}, status=status.HTTP_400_BAD_REQUEST)


class GetFileListView(views.APIView):
    def post(self, request):
        serializer = BasePathSerializer(data=request.data)
        if serializer.is_valid():
            path = serializer.validated_data.get('path')
            resp = os_do_cmd("ls", path)
            res = formatCmdRes(resp)
            res = [i for i in res if "__" not in i]  # 结果过滤"__init__.py"等文件
            return Response(data={"statusCode": 2000, "body": res}, status=status.HTTP_200_OK)
        else:
            return Response(data={"message": dict(serializer.errors)}, status=status.HTTP_400_BAD_REQUEST)


class MakeCmdView(views.APIView):
    def post(self, request):
        serializer = MakeCmdSerializer(data=request.data)
        if serializer.is_valid():
            cmd = serializer.validated_data.get('cmd')
            agrstr = serializer.validated_data.get('agrstr')
            try:
                resp = os_do_cmd(cmd, agrstr)
                res = formatCmdRes(resp)
                return Response(data={"statusCode": 2000, "body": res}, status=status.HTTP_200_OK)
            except:
                return Response(data={"message": "出错了，请检查代码"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data={"message": dict(serializer.errors)}, status=status.HTTP_400_BAD_REQUEST)


class GetScriptParamsView(views.APIView):
    def post(self, request):
        serializer = BasePathSerializer(data=request.data)
        if serializer.is_valid():
            path = serializer.validated_data.get('path')
            if os.path.isdir(path):
                return Response(data={"statusCode": 2004, "body": "这是个文件夹，执行功能敬请期待"}, status=status.HTTP_200_OK)
            else:
                dic = getScriptParams(path)
                return Response(data={"statusCode": 2000, "body": dic}, status=status.HTTP_200_OK)
        else:
            return Response(data={"message": dict(serializer.errors)}, status=status.HTTP_400_BAD_REQUEST)


class GetScriptTreeView(views.APIView):
    def post(self, request):
        serializer = GetScriptTreeSerializer(data=request.data)
        if serializer.is_valid():
            type = serializer.validated_data.get('type')
            try:
                pathForTree = os.getcwd()  # 记录初始工作目录
                workpath = pathForTree + "/ppy"
                if type:
                    res = check_file_totree(workpath, "0")
                else:
                    res = check_file_tolist(workpath)
                os.chdir(pathForTree)  # 使工作目录恢复到初始工作目录
                return Response(data={"statusCode": 2000, "body": res}, status=status.HTTP_200_OK)
            except Exception as r:
                return Response(data={"message": r}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data={"message": dict(serializer.errors)}, status=status.HTTP_400_BAD_REQUEST)


class GetScriptDetailView(views.APIView):
    def post(self, request):
        data = {}
        serializer = BasePathSerializer(data=request.data)
        if serializer.is_valid():
            path = serializer.validated_data.get('path')
            if os.path.isdir(path):
                files = check_file_tolist(path)
                file_list = []
                for f in files:
                    file_list.append(f['value'])
                data["request"] = None
                data["info"] = file_list
                return Response(data={"statusCode": 2000, "body": data}, status=status.HTTP_200_OK)
            else:
                data["request"] = getScriptParams(path)
                data["info"] = getScriptDetail(path)
                return Response(data={"statusCode": 2000, "body": data}, status=status.HTTP_200_OK)
        else:
            return Response(data={"message": dict(serializer.errors)}, status=status.HTTP_400_BAD_REQUEST)


class GetFileContentView(views.APIView):
    def post(self, request):
        data = {}
        serializer = BasePathSerializer(data=request.data)
        if serializer.is_valid():
            path = serializer.validated_data.get('path')
            if os.path.isdir(path):
                data["message"] = "这是个文件夹，无内容读取"
                return Response(data={"statusCode": 2004, "body": data},
                                status=status.HTTP_200_OK)
            else:
                with open(path) as f:
                    strings = f.read()
                data["content"] = strings
                return Response(data={"statusCode": 2000, "body": data}, status=status.HTTP_200_OK)
        else:
            return Response(data={"message": dict(serializer.errors)}, status=status.HTTP_400_BAD_REQUEST)


class GetScriptResultView(views.APIView):
    def post(self, request):
        serializer = GetScriptResultSerializer(data=request.data)
        if serializer.is_valid():
            try:
                report = serializer.validated_data.get('report')
                result = get_script_result(report)
                return Response({"statusCode": 2000, "body": result},
                                status=status.HTTP_200_OK)
            except:
                data = {"message": "命令执行失败"}
                return Response({"statusCode": 5000, "body": data},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(data={"message": dict(serializer.errors)}, status=status.HTTP_400_BAD_REQUEST)


def report(request, reportname):
    context = {}
    try:
        changeReportCssPath(reportname)
        return render(request, reportname, context)
    except:
        return render(request, "Notfound.html", context)


global num
num = 0
lock = threading.Lock()
