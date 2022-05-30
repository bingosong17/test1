#! /usr/bin/env python
# -*- coding:utf-8 -*-

# author:bingo

from formatBase import formatHar

config = """verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "ppApp",
            "phone": "13861683296",
            "session": "${getSession($business,$phone)}",
        })"""

do_it = formatHar(config, 'pinpin', 's_to_s')
do_it.setHarName("店铺签到分页列表查询.har")
do_it.doFormat()
