#! /usr/bin/env python
# -*- coding:utf-8 -*-

# author:bingo
import os
import re

filterlist = [".pytest_cache", '.DS_Store', 'demo.iml', '$CACHE_FILE$',
              'profiles_settings.xml', '$PRODUCT_WORKSPACE_FILE$', 'workspace.xml',
              'modules.xml', 'misc.xml', '.idea', '.env', 'debugtalk.py', '.gitignore',
              'imgBase64Data.py', 'logs', 'formatBase.py', 'env.py',
              'readme', 'Test_test.py', 'tools.py', '.git', 'files', 'envAll']


def toReplace(file_path, stringB, string1, string2=None):
    """
    :param string2:
    :param string1:
    :param stringB:使用该值替换
    :param file_path: 文件路径
    :return: 文件列表
    """
    if os.path.isdir(file_path):
        all_file = os.listdir(file_path)
        all_file = [i for i in all_file if "__" not in i]
        all_file = [i for i in all_file if i not in filterlist]
        for f in all_file:
            toReplace(file_path + '/' + f, stringB, string1, string2)
    else:
        replace(file_path, stringB, string1, string2)


def replace(file, stringB, string1, string2):
    """
    在文件中查找，用stringB替换stringA的值
    :param string2:
    :param string1:
    :param file: 文件名
    :param stringB: 新字符串
    """
    if os.path.isfile(file):
        with open(file, encoding='utf-8') as f:
            s = f.read()
            # 如果string2不为空，说明要通过前字符串string1和后字符串string2查找一个字符串，并将最后查找到的结果赋值给string1
            if string2 is not None:
                message = string1 + "((?:.|\n)*?)" + string2
                # comment = re.compile(r'base_url((?:.|\n)*?),')
                comment = re.compile(message)
                result = comment.search(s)
                if result is not None:
                    string1 = result.group()
            if string1 in s:
                s = s.replace(string1, stringB)
                print("文件替换成功：", file)
            # else:
            #     print("文件无需替换：", file)
        with open(file, "w", encoding='utf-8') as f:
            f.write(s)
    else:
        print("不是文件：", file)


def toFind(file_path, strings1, strings2=None, files=None):
    """
    查找路径下所有文件内容，并打印位置
    :param strings1:
    :param strings2:
    :param files:文件计数
    :param file_path: 目标路径
    """
    if files is None:
        files = []
    all_file = os.listdir(file_path)
    all_file = [i for i in all_file if "__" not in i]
    all_file = [i for i in all_file if i not in filterlist]

    for f in all_file:
        if os.path.isdir(file_path + '/' + f):
            # print(number)
            toFind(file_path + '/' + f, strings1, strings2, files)
        else:
            path_f = file_path + "/" + f
            if do_find(path_f, strings1, strings2):
                files.append(path_f)
    return len(files)


def do_find(file, strings1, strings2=None):
    """
    在文件内查找内容
    :param strings2:如果该值不为none，则以string1内容为头，string2内容为尾，查询区间字符串内容
    :param strings1:如果只单独有该参数值，则以该内容进行查询
    :param file: 目标文件
    """
    if os.path.isfile(file):
        with open(file, encoding='utf-8') as f:
            s = f.read()
            if strings2 is None:
                if strings1 in s:
                    print("此文件包含内容：", file)
                    return True
            else:
                message = strings1 + "((?:.|\n)*?)" + strings2
                # comment = re.compile(r'base_url((?:.|\n)*?),')
                comment = re.compile(message)
                result = comment.search(s)
                # strings = s.replace(result, "**" + dicstr)  # 使用传入的dic替换副本的全局传参部分
                if result is not None:
                    # print(result.group())
                    # print("此文件包含内容：", file)
                    return True
                else:
                    print("此文件不包含内容：", file)
    return False


# toReplace("./yyht", '', "import env")
print(toFind(".", "transportation/transOrderDetail"))
# print(toFind(".", "base_url", ","))



# stringB = '''base_url("${testEnv($business)}").variables(
#         **{
#             "business": "",'''
# toReplace("./yyht", stringB, "base_url", ",")

