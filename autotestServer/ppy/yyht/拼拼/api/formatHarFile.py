#! /usr/bin/env python
# -*- coding:utf-8 -*-

# author:bingo

from formatBase import formatHar

config = """verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",
        })"""

do_it = formatHar(config, '_t', 's_to_s')
do_it.setHarName("规则管理删除充值规则.har")
do_it.doFormat()
