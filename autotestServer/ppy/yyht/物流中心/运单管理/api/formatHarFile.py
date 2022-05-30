#! /usr/bin/env python
# -*- coding:utf-8 -*-

# author:bingo

from formatBase import formatHar

config = """verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "pd",
            "session": "${getSession($business)}",
        })"""


do_it = formatHar(config, 'cn', 's_to_s')
do_it.setHarName("aa.har")
do_it.doFormat()

