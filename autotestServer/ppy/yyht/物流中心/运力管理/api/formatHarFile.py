#! /usr/bin/env python
# -*- coding:utf-8 -*-

# author:bingo

from formatBase import formatHar

config = """verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",
        })"""

do_it = formatHar(config, 'cn', 's_to_s')
do_it.setHarName("运营费财务审核驳回.har")
do_it.doFormat()
