"""
<SCRIPTNAME> API TEST </SCRIPTNAME>
<DESCRIPTION>
    完成指定接口的参数测试，运算效率测试
</DESCRIPTION>
<AUTHOR>
    Bingo
</AUTHOR>
<HISTORY>
</HISTORY>
"""
import requests
import json, random, copy
from optparse import OptionParser

def initData(p,typ):

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    character = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 's', 'y', 'z']
    special = ['~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '{', '}', '|', '\\', '[',
               ']', '\'', ':', '"', ';', '<', '>', '?', '?', ',', '.', '/', ' ']
    if typ == 'string':
        return random.choice(character)
    if typ == 'integer':
        return int(random.choice(numbers))

def getLog(way,*args):
    if way == True:   #如果方式为0，直接输出到控制台
        for message in args:
            print(message)
    else:
        for message in args:
            with open("Result.txt", "a+") as f:
                f.write(message)
                f.write('\r\n')

def transHttp(ConfigHttp,method):
    global maxtime,resdict
    if method == "get":
        resp = ConfigHttp.get()
    else:
        resp = ConfigHttp.post()
    tim = resp.elapsed.total_seconds() * 1000  # 接口效率
    if int(tim) > maxtime:
        maxtime = int(tim)
        resdict = ConfigHttp.data
    return json.loads(str(resp.content, 'utf-8'))

class ConfigHttp:
    def __init__(self):
        global timeout
        timeout = 2
        self.headers = {}
        self.params = {}
        self.data = {}
        self.host = None
        self.url = None
        self.files = {}
        self.response={}
        self.path = None

    def set_url(self, url):
        self.url = self.host + url

    def set_headers(self, header):
        self.headers = header

    def set_params(self, param):
        self.params = param

    def set_host(self, host):
        self.host = host

    def set_data(self, data):
        self.data = data

    def set_files(self, file):
        self.files = file

        # defined http get method
    def get(self):
        try:
            # response = requests.get(self.url, params=self.params, headers=self.headers, timeout=float(timeout))
            response = requests.get(self.url, params=self.data, headers=self.headers, timeout=float(timeout))

            # response.raise_for_status()

            #return json.loads(str(response.content, 'utf-8'))
            return response  #返回response，提取其中的响应时间，做效率判定
        except TimeoutError:
            # self.logger.error("Time out!")
            return None


    # defined http post method
    def post(self):
        try:
            response = requests.post(self.url, headers=self.headers, data=self.data, files=self.files,
                                     timeout=float(timeout))
            # response.raise_for_status()
            #return json.loads(str(response.content, 'utf-8'))
            return response
        except TimeoutError:
            # self.logger.error("Time out!")
            return None

special = ['~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '{', '}', '|', '\\', '[',
               ']', '\'', ':', '"', ';', '<', '>', '?', '?', ',', '.', '/', ' ']
status = {"success": 2000, "fail":5000,"missarg":4010}
argType = ['string', 'integer']
limiTime = 500  #接口返回效率限制，超过该值将print提醒
geShi = {"tab": "      "}


if __name__ == '__main__':

    optparser = OptionParser()
    #  add the private options here:
    optparser.add_option("-c", action="store_true", dest="way", help="Log打印直接输出到控制台")
    optparser.add_option("-t", action="store_false", dest="way", help="Log打印输入至result.txt")
    optparser.add_option("-p","--path", type=str, dest="path", help="要测试的接口路径，例如：/search/goods")

    (options, args) = optparser.parse_args()
    way = options.way
    path = options.path

    # 需要输入way,path参数，否则退出
    if way == None or path == None:
        optparser.print_help()
        exit()


    API = ConfigHttp()
    url = "http://172.16.31.42:7211/v2/api-docs"
    res_html = requests.get(url)
    res_dict = json.loads(res_html.text)
    host = res_dict["host"]
    API.set_host("http://"+host)
    header = {"x-uc-userdata": "{id:1}"}
    API.set_headers(header)
    paths = res_dict["paths"]
    path_will_test = []
    # path_will_test.append("/search/goods/associativeWords")
    # path_will_test.append("/search/goods")
    path_will_test.append(path)

    for i, j in paths.items():
        if i in path_will_test:
            global maxtime,resdict
            maxtime = 0    #记录接口性能时间，只保留最长时间
            resdict = {}   #记录耗时最长时的请求参数
            API.path = i
            API.set_url(i)  #初始化 url
            api_methods = list(j.keys())[0]
            dict_values = list(j.values())[0]
            getLog(way,dict_values["summary"], "路径："+API.path, "方法："+api_methods)

            API.data = {}

            # 初始化生成正确的data，暂时不处理header参数，并进行正确参数测试
            for parameter in dict_values["parameters"]:
                if parameter['in'] != 'header':
                    API.data[parameter['name']] = initData(parameter, parameter['type'])
            dataRight = copy.deepcopy(API.data) #基准正确参数保留
            res = transHttp(API, api_methods)
            if res['statusCode'] == status["success"]:
                getLog(way, "pass————冒烟测试")

            else:
                getLog(way, "fail————冒烟测试", geShi["tab"]+"错误返回："+json.dumps(res))
                getLog(way, geShi["tab"] + "请求数据：" + str(API.data))

            getLog(way,"<<<<<<<参数类型异常测试>>>>>>")
            for parameter in dict_values["parameters"]:
                if parameter['in'] != 'header':
                    for typ in argType:
                        if typ != parameter['type']:
                            API.data[parameter['name']] = initData(parameter, typ)
                            res = transHttp(API, api_methods)
                            if res['statusCode'] == status["fail"]:
                                getLog(way,"pass————"+ parameter["name"]+"参数要求类型为"+parameter['type']+"，使用"+typ+"类型测试")
                            else:
                                getLog(way,"fail————"+parameter["name"]+"参数要求类型为"+parameter['type']+"，使用"+typ+"类型测试", geShi["tab"]+"错误返回：" + json.dumps(res))
                                getLog(way,geShi["tab"]+"请求数据：" + str(API.data))
                API.data = copy.deepcopy(dataRight)  #重置数据，进行下一个参数修改测试

            getLog(way,"<<<<<<参数必要性测试>>>>>>：")
            for parameter in dict_values["parameters"]:
                if parameter['in'] != 'header':
                    API.data.pop(parameter['name'])
                    res = transHttp(API, api_methods)
                    if parameter['required'] == True:
                        if res['statusCode'] == status["missarg"]:
                            getLog(way,"pass————"+parameter["name"] + "参数要求为必要，缺失类型测试")
                        else:
                            getLog(way,"fail————"+parameter["name"] + "参数要求为必要，缺失类型测试",
                                   geShi["tab"]+"错误返回：" + json.dumps(res))
                            getLog(way,geShi["tab"]+"请求数据：" + str(API.data))
                    else:
                        if res['statusCode'] == status["success"]:
                            getLog(way,"pass————"+parameter["name"] + "参数要求为非必要，缺失类型测试")
                        else:
                            getLog(way,"fail————"+parameter["name"] + "参数要求为非必要，缺失类型测试",
                                   geShi["tab"]+"错误返回：" + json.dumps(res))
                            getLog(way,geShi["tab"]+"请求数据：" + str(API.data))
                API.data = copy.deepcopy(dataRight)  #重置数据，进行下一个参数修改测试
            for parameter in dict_values["parameters"]:
                if parameter['in'] != 'header':
                    if parameter['required'] == False:
                        API.data.pop(parameter['name'])
            res = transHttp(API, api_methods)
            if res['statusCode'] != status["success"]:
                getLog(way,"fail——非必要参数全部缺失测试：",
                       "错误返回：" + json.dumps(res))
                getLog(way,"请求数据：" + str(API.data))
            API.data = copy.deepcopy(dataRight)  # 重置数据，进行下一个参数修改测试

            getLog("<<<<<<参数特殊字符遍历测试>>>>>>") #当参数类型为string则进行该测试
            for parameter in dict_values["parameters"]:
                tag = 0  #作为全部通过标志
                if parameter['in'] != 'header':
                    if parameter['type'] =="string":
                        for c in special:
                            API.data[parameter['name']] = c
                            res = transHttp(API, api_methods)
                            if res['statusCode'] != status["success"]:
                                tag = 1
                                getLog(
                                    way,"fail————"+parameter["name"] + "特殊字符<"+c + ">测试",
                                    geShi["tab"]+"错误返回：" + json.dumps(res))
                                getLog(way,geShi["tab"]+"请求数据：" + str(API.data))
                        if tag == 0:
                            getLog(way,"pass————"+parameter["name"] + "特殊字符测试")
                API.data = copy.deepcopy(dataRight)  # 重置数据，进行下一个参数修改测试

            getLog("<<<<<<接口性能测试>>>>>>")  # 当参数类型为string则进行该测试
            if maxtime > limiTime:
                getLog(
                    way,"fail————接口耗时最长为："+str(maxtime)+"ms,超过设定限定值"+str(limiTime)+"ms",
                    geShi["tab"] + "请求数据：" + json.dumps(resdict))
            else:
                getLog(way,"pass————接口耗时最长为："+str(maxtime)+"ms,小于设定限定值"+str(limiTime)+"ms")







