#! /usr/bin/env python
# -*- coding:utf-8 -*-

# author:bingo

import os
import platform
import re
import time
from optparse import OptionParser


class formatHar:
    """
    格式化har的基本类
    """
    def __init__(self, config, add_str, auth_way):
        self.config = config
        self.har_path = ""
        self.py_file_path = ""
        self.strings = ""
        self.add_str = add_str  # 删除地址的末尾符号
        self.auth = auth_way  # s_to_s,s_to_t,t_to_t
        self.telling = '''"""
    概要：
        无
    输入参数：
        无
    输出参数：
        无
    前置接口：
        无
"""
'''

    def setHarName(self, name):
        """
        输入要处理的har名字
        :param name:
        """
        self.har_path = name

    def openFile(self):
        with open(self.py_file_path, encoding="utf-8") as f:
            self.strings = f.read()

    def writeFile(self):
        with open(self.py_file_path, 'w', encoding="utf-8") as f:
            f.write(self.strings)

    def deleteBetweenTwo(self, startStr, endStr, replaceStr=""):
        """
        :param startStr: 要处理的字符串开始部分（最后结果包含该部分）
        :param endStr: 要处理的字符串结束部分（最后结果包含该部分）
        :param replaceStr: 用该部分内容替换要处理的部分，默认为空，代表删除意思
        """
        result = re.findall(startStr + ".*?" + endStr, self.strings)
        self.strings = self.strings.replace(result[0], replaceStr)

    def getWordsAndUseItToReplace(self, startStr, endStr, replaceStr):
        """
        :param startStr: 提取字符的搜索字符开始处（最后结果不包含该部分）
        :param endStr: 提取字符的搜索字符结束处（最后结果不包含该部分）
        :param replaceStr: 需要被替换的字符处
        """
        result = re.findall(startStr + "(.*?)" + endStr, self.strings)
        self.strings = self.strings.replace(replaceStr, result[0])

    def har2casefile(self):
        cmd = "har2case " + self.har_path
        os.popen(cmd)

    def deleteHarFile(self):
        if platform.system() == 'Windows':
            cmd = "del " + self.har_path
        else:
            cmd = "rm " + self.har_path
        os.popen(cmd)

    def doFormat(self):
        optparser = OptionParser()
        #  add the private options here:
        optparser.add_option("-f", "--file", type=str, dest="path", help="要处理的文件路径")
        (options, args) = optparser.parse_args()
        if options.path:
            self.har_path = options.path
        self.har2casefile()
        self.py_file_path = self.har_path[0:-4] + "_test.py"
        while not os.path.exists(self.py_file_path):
            time.sleep(1)
        time.sleep(4)
        self.openFile()
        self.deleteBetweenTwo("# FROM:", "\.har\n", self.telling)
        self.deleteBetweenTwo("verify\(", "alse\)", self.config)
        self.getWordsAndUseItToReplace("TestCase", "\(", "testcase description")
        self.deleteBetweenTwo("            ", 'TF-8"\)\n')
        self.deleteBetweenTwo('            \.assert_equal\("body\.timestamp', '\)\n')

        try:
            if self.auth == "s_to_s":
                self.deleteBetweenTwo('"sessionId": "', '\"', '"sessionId": "$session"')
            elif self.auth == 's_to_t':
                self.deleteBetweenTwo('"sessionId": "', '\"', '"sessionId": "$token"')
            else:
                self.deleteBetweenTwo('"token": "', '\"', '"token": "$token"')
        except:
            pass
        while True:
            try:
                self.deleteBetweenTwo("            ", 'None\)\n')
            except:
                break
        while True:
            try:
                self.deleteBetweenTwo("            ", 'null"\)\n')
            except:
                break
        while True:
            try:
                self.deleteBetweenTwo("            ", '""\)\n')
            except:
                break
        try:
            self.deleteBetweenTwo('                    "Host"', ',\n')
        except:
            pass
        try:
            self.deleteBetweenTwo('                    "Cookie"', ',\n')
        except:
            pass
        try:
            self.deleteBetweenTwo('                    "Origin', ',\n')
        except:
            pass
        try:
            self.deleteBetweenTwo('                    "Referer"', ',\n')
        except:
            pass
        try:
            self.deleteBetweenTwo('            \.assert_equal\("body\.traceMsg', '\)\n')
        except:
            pass
        try:
            self.deleteBetweenTwo('http', self.add_str)
        except:
            pass
        # 删除with_cookies部分，由于换行，要使用这种方式
        try:
            comment = re.compile(r'            \.with_cookies(?:.|\n)*?\)\n')
            result = comment.findall(self.strings)
            self.strings = self.strings.replace(result[0], "")
        except:
            pass
        self.writeFile()
        self.deleteHarFile()


config = """verify(False).base_url("${testEnv(yyht_$env)}").variables(
        **{
            "env":"alpha",
            "session": "",
        })"""
