
from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from kfht.api.获取已登录用户的信息_test import TestCase获取已登录用户的信息 as 获取已登录用户的信息
from kfht.api.获取用户信息列表_test import TestCase获取用户信息列表 as 获取用户信息列表
import env

class TestCase获取客服信息(HttpRunner):
    config = Config("testcase description").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "",
            "phone": "17629262213",
            "session": "${getSession($business,$phone)}",
        }
    )
    teststeps = [
        Step(
            RunTestCase("获取已登录用户的信息").call(获取已登录用户的信息)
        ),
        Step(
            RunTestCase("获取用户信息列表").call(获取用户信息列表)
        )
    ]


if __name__ == "__main__":
    TestCase获取客服信息().test_start()
