#! /usr/bin/env python
# -*- coding:utf-8 -*-

# author:bingo

from formatBase import formatHar

config = """verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "",
            "session": "",
        })"""

do_it = formatHar(config, '_t', 's_to_s')
do_it.setHarName("T123.har")
do_it.doFormat()


