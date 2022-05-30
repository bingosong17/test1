import datetime
import platform
import re
import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def mailsend(filepath, receivers):
    # msg_from = 'bingosong17@163.com'
    # passwd = '741963sjb'
    # msg_to = 'songjingbin@pinpianyi.com'
    msg_from = 'songjingbin@pinpianyi.com'
    passwd = '741963Sjb'
    msg_to_list = ['806731834@qq.com', 'bingosong17@163.com']
    # 创建一个带附件的实例
    message = MIMEMultipart()
    message['From'] = msg_from
    message['To'] = ','.join(receivers) if isinstance(receivers, list) else receivers
    message['Subject'] = '测试结果通知'
    message['Date'] = Header(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'utf-8')

    # 邮件正文内容
    message.attach(MIMEText('以下为自动测试结果通知，如有疑问，请联系宋静斌', 'plain', 'utf-8'))

    # 构造附件1，传送当前目录下的test.txt文件
    att1 = MIMEText(open(filepath, 'rb').read(), 'base64', 'utf-8')
    att1['Content-Type'] = 'application/octet-stream'
    # 这里的filename可以任意写，写什么名字 邮件中就显示什么名字
    att1['Content-Disposition'] = "attachment;filename=" + filepath
    message.attach(att1)

    # mail_server = 'smtp.163.com'      #网易邮箱的服务
    mail_server = 'smtp.mxhichina.com'  # 钉钉邮箱的服务
    s = smtplib.SMTP(mail_server)
    s.login(msg_from, passwd)
    if not isinstance(receivers, list):
        receivers = receivers.split(",")
    s.sendmail(msg_from, receivers, message.as_string())


def formatCmdRes(res):
    """
    对系统命令返回的结果进行格式化
    :param res:系统返回结果串
    :return:
    """
    res = res.split("\n")  # 去除字符串结尾的换行符
    res = [i for i in res if i != '']  # 去除列表中的空
    try:
        res = [i.replace(" ", "-").replace('"', "") for i in res]
    except:
        pass
    # response = []
    # try:
    #     for i in res:
    #         for j in range(4):
    #             i = i[1:]
    #         response.append(i)
    # except:
    #     pass
    # return response
    return res


def timeStr():
    t = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    return t


def changeReportCssPath(name):
    """
    打开文件
    :return: 返回文件内容string
    """
    # path = "../templates/" +name   函数调试使用
    path = "templates/" + name  # 整体软件运行使用
    with open(path, 'r') as f:
        strings = f.read()
    # href="assets/style.css"
    # href="../static/style.css"
    result = re.findall("href" + ".*?" + "css\"", strings)
    strings = strings.replace(result[0], r'href="../static/style.css"')
    with open(path, 'w') as f:
        f.write(strings)


def modifyModel(path, dic=None):
    """
    复制模版文件，并对模版文件进行修改替换
    :param dic: 要替换的数据
    :param path: 模版文件路径
    :return: 返回生成的副本脚本路径，供用户实际使用
    """
    pathpart = path.split("/")
    pathpart[-1] = pathpart[-1][0:-3] + timeStr()[-5:-1] + "_test.py"
    copyedpath = "/".join(pathpart)
    with open(path) as f:
        strings = f.read()
    strings = strings.replace('"""', '')
    strings = strings.replace('<route>', dic["script_route"])
    strings = strings.replace('<class>', dic["script_class"])
    strings = strings.replace('<alias>', dic["script_alias"])
    strings = strings.replace('<datas>', str(dic["script_datas"]))

    with open(copyedpath, 'w') as f:
        f.write(strings)
    return copyedpath


def copyHttprunnerProject(path):
    """
    为了应对多用户同时请求使用httprunner脚本情况，复制项目，保证使用环境不受其他用户干扰
    :param path:路径
    :return 成功返回复制后的项目文件路径，否则1/2-项目复制失败/执行路径不存在
    """
    if os.path.exists(path):
        source_file = "./ppy"
        idd = timeStr()[-5:-1]
        target_file = "./ppy" + idd
        pathpart = path.split("ppy")
        pathpart[0] += idd
        arg = "-r " + source_file + " " + target_file
        try:
            os_do_cmd("cp", arg)
            projectpath = target_file + pathpart[1]
            return projectpath
        except:
            return 1
    else:
        return 2


def findString(path, startStr, endStr):
    """
    路径文件中，找出两个定位字符中间的内容
    :param path: 文件路径
    :param startStr: 提取字符的搜索字符开始处（最后结果不包含该部分）
    :param endStr: 提取字符的搜索字符结束处（最后结果不包含该部分）
    :return: 要寻找的字符
    """
    with open(path, encoding="utf-8") as f:
        strings = f.read()
    result = re.findall(startStr + "(.*?)" + endStr, strings)
    return result[0]


filter_list_for_params = ['env']


def getScriptParams(path):
    """
    获取运行的脚本需要输入的参数
    :param path:
    :return:
    """
    with open(path) as f:
        strings = f.read()
    comment = re.compile(r'\.variables((?:.|\n)*?)        }')
    result = comment.findall(strings)
    res = result[0].split("\n")
    res = res = [i.lstrip() for i in res if ":" in i]
    dic = {}
    for i in res:
        kav = i.split(":")
        key = kav[0].replace(" ", "").replace("'", "").replace('"', "")
        value = kav[1].replace(" ", "").replace("'", "").replace('"', "")
        # 删除末尾符号“,”而不删除中间可能存在的“,”
        if value[-1] == ",":
            value = value[0:-1]
        dic[key] = value
    # 将filter_list内的内容过滤，不输出到前端
    for i in filter_list_for_params:
        try:
            dic.pop(i)
        except:
            pass
    return dic


import os

filterlist = [".pytest_cache", '.DS_Store', 'demo.iml', '$CACHE_FILE$',
              'profiles_settings.xml', '$PRODUCT_WORKSPACE_FILE$', 'workspace.xml',
              'modules.xml', 'misc.xml', '.idea', '.env', 'debugtalk.py', '.gitignore',
              'formatHarFile.py', 'imgBase64Data.py', 'logs', 'formatBase.py', 'env.py',
              'sessionYYHT_test.py', 'readme', 'Test_test.py', 'tools.py', 'envAll', 'files']


def check_file_totree(file_path, idi):
    j = 1
    if idi == '0':
        idi = ''
    else:
        idi += "."
    os.chdir(file_path)
    all_file = os.listdir()
    all_file = [i for i in all_file if "__" not in i]
    all_file = [i for i in all_file if i not in filterlist]
    files = []
    for f in all_file:
        if os.path.isdir(f):
            files.append({"id": idi + str(j),
                          "label": f,
                          "path": os.getcwd(),
                          "children": check_file_totree(file_path + '/' + f, idi + str(j))})
            os.chdir(file_path)
        else:
            files.append({"id": idi + str(j),
                          "label": f,
                          "path": os.getcwd(), })
        j += 1

    return files


def check_file_tolist(file_path, files=None):
    """
    :param files:
    :param file_path: 文件路径
    :return: 文件列表
    """
    if files is None:
        files = []
    all_file = os.listdir(file_path)
    all_file = [i for i in all_file if "__" not in i]
    all_file = [i for i in all_file if i not in filterlist]

    own_filter_list = ['api', '业务脚本', 'wlApp', 'gysht', 'kfht',
                       'ppyApp', 'wlApp', 'yyht']
    for f in all_file:
        if os.path.isdir(file_path + '/' + f):
            if f not in own_filter_list:
                files.append({
                    "value": f,
                    "path": file_path,
                }
                )
            check_file_tolist(file_path + '/' + f, files)
            # os.chdir(file_path)  #改变当前工作目录到指定的路径
        else:
            files.append({
                "value": f,
                "path": file_path, })
    return files


def getScriptDetail(path):
    with open(path) as f:
        strings = f.read()
    try:
        comment = re.compile(r'"""((?:.|\n)*?)"""')
        result = comment.search(strings).group()
        result = result.replace('"""\n', "")
        result = result.replace('\n"""', "")
        return formatCmdRes(result)
        # return result
    except:
        return "未找到"


def os_do_cmd(cmd, argstr=""):
    """

    :param cmd: 命令，默认使用linux命令
    :param argstr: 参数，命令后面跟的参数
    :return: 命令执行结果
    """
    linux_to_windows = {
        "ls": "dir",
        "cd": "cd",
        "cp": "copy",
        "rm": "del",
        "rmdir": "rmdir",
        "cat": "type",
        "pwd": "cd",
        "clear": "cls",
        "history": "doskey /h",
        "vi": "edit",
        "diff": "fc",
        "grep": "find",
        "ftp": "ftp",
        "man": "help",
        "hostname": "hostname",
        "ifconfig": "ipconfig",
        "top": "men",
        "mkdir": "mkdir",
        "who": "net session",
        "uptime": "net statistics",
        "traceroute": "tracert",
        "find": "tree",
        "hrun": "hrun",
    }
    try:
        if platform.system() == 'Windows':
            cmd_str = linux_to_windows[cmd] + " " + argstr
        else:
            cmd_str = cmd + " " + argstr
        return os.popen(cmd_str).read()
    except:
        print("命令不正确")


def get_script_result(report):
    """
    获取报告中结果。主要使用字符提取，提取html文档中的关键信息
    :param report:报告名字
    :return:报告结果
    """
    # report_path = "../templates/"+report
    report_path = "./templates/" + report
    if not os.path.exists(report_path):
        return {"result": "报告未生成，请稍后查看"}
    with open(report_path, encoding='utf-8') as f:
        lines = f.readlines()
        result_url = lines[-18]
        result_line = lines[-4]
        summary = lines[262]
    r_passed = re.search('class="passed">(.*?passed)</span>', summary)
    r_skipped = re.search('class="skipped">(.*?skipped)</span>', summary)
    r_failed = re.search('class="failed">(.*?failed)</span>', summary)
    r_errors = re.search('class="error">(.*?errors)</span>', summary)
    r_xfailed = re.search('class="xfailed">(.*?expected failures)</span>', summary)
    r_xpassed = re.search('class="xpassed">(.*?unexpected passes)</span>', summary)
    result = "{},  {},  {},  {},  {},  {}" \
        .format(r_passed.group(1), r_failed.group(1),
                r_skipped.group(1), r_errors.group(1),
                r_xfailed.group(1), r_xpassed.group(1))
    # 格式处理
    try:
        result_line = result_line.replace("body: ", "")
    except:
        pass
    try:
        result_line = result_line.replace("&quot;", "")
    except:
        pass
    try:
        result_line = result_line.replace("&#x27;", "")
    except:
        pass
    try:
        result_url = result_url.replace("url: ", "")
    except:
        pass
    try:
        result_url = result_url.replace("\n", "")
    except:
        pass
    if "step end:" in result_line:
        return {"result": result}
    else:
        return {"result": result,
                "url": result_url,
                "message": result_line}

# print(get_script_result("20200921060834.html"))
# print(get_script_result("20200930034233.html"))
# copyHttprunnerProject("ppy/makedata/用户下单_test.py")
