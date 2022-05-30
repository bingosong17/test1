
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from httprunner import HttpRunner, Config, Step, RunTestCase
from project.物流web.T6_1_6查看车型计价信息_test import TestCase获取计价表信息 as 获取计价表信息


class TestCase获取计价表信息(HttpRunner):

    config = Config("testcase description").verify(False).variables(

        )

    teststeps = [
        Step(
            RunTestCase("获取计价表信息").call(获取计价表信息)
        ),
    ]

