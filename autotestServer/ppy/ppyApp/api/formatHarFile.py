#! /usr/bin/env python
# -*- coding:utf-8 -*-

# author:bingo

from formatBase import formatHar

config = """verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "ppyApp",
            "account": "",
            "token": "${getSession($business,$account)}",
        })"""

do_it = formatHar(config, 'all', 's_to_t')
do_it.setHarName("创建用户资料.har")
do_it.doFormat()
