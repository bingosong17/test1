# NOTE: Generated By HttpRunner v3.1.4
"""
    概要：
        无
    输入参数：
        无
    输出参数：
        无
    前置接口：
        无
"""


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCase根据红包Id查询红包详情(HttpRunner):

    config = Config("根据红包Id查询红包详情").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",
            "redPacketId": "",
        })

    teststeps = [
        Step(
            RunRequest("/mall/user/member/redPacket/detail/$redPacketId")
            .get(
                "/mall/user/member/redPacket/detail/233776"
            )
            .with_headers(
                **{
                    "Connection": "keep-alive",
                    "Accept": "application/json, text/plain, */*",
                    "Sec-Fetch-Dest": "empty",
                    "sessionId": "$session",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
                    "Sec-Fetch-Site": "same-site",
                    "Sec-Fetch-Mode": "cors",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.statusCode", 2000)
        ),
    ]


if __name__ == "__main__":
    TestCase根据红包Id查询红包详情().test_start()
