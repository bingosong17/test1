import requests, json

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