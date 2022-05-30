#! /usr/bin/env python
# -*- coding:utf-8 -*-

# author:bingo

from formatBase import formatHar

config = """verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "wlApp",
            "phoneNumber": "15997336112",
            "token": "${getSession($business,$phoneNumber)}",
            "userId": "${getWlAppUserId($phoneNumber)}",
        })"""

do_it = formatHar(config, 'cn', 't_to_t')
do_it.setHarName("送货单打印页搜索司机.har")
do_it.doFormat()
