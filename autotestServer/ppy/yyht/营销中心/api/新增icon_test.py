# NOTE: Generated By HttpRunner v3.1.3
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



class TestCase新增Icon(HttpRunner):

    config = Config("新增Icon").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",
            "startTime": "${hapentime(1)}"+":00",
            "endTime": "${hapentime(100)}"+":00",
            "traIdsList": [11, 13, 14, 20, 104, 171, 173, 174, 177, 178, 386, 395],
        })

    teststeps = [
        Step(
            RunRequest("/alpha_t/mall/icon/add")
            .post("/mall/icon/add")
            .with_headers(
                **{
                    "Connection": "keep-alive",
                    "Content-Length": "355",
                    "sessionId": "$session",
                    "Sec-Fetch-Dest": "empty",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
                    "systemCode": "yypp",
                    "Content-Type": "application/json",
                    "Accept": "*/*",
                    "Sec-Fetch-Site": "same-origin",
                    "Sec-Fetch-Mode": "cors",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                }
            )
            .with_json(
                {
                    "actionContent": "1",
                    "actionType": "newMiNi",
                    "authorized": True,
                    "traIds": "$traIdsList",
                    "picUrl": "http://images.alpha.pinpianyi.cn/images/common/8dfc5cb149a34cf3bcea5521817012d3.png",
                    "searchPicUrl": "",
                    "actionParam": "",
                    "startTime": "$startTime",
                    "endTime": "$endTime",
                    "iconName": "test_郑小和",
                    "iconId": None,
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.statusCode", 2000)
            .assert_equal("body.body", True)
        ),
    ]


if __name__ == "__main__":
    TestCase新增Icon().test_start()
