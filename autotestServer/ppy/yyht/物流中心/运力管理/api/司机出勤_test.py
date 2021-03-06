# NOTE: Generated By HttpRunner v3.1.4
"""
    概要：
        操作司机出勤
    输入参数：
            "driverId":"", 司机id
            "date":"",      日期
            "type":""       出勤状态
    输出参数：
        无
    前置接口：
        无
"""


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCase操作司机出勤(HttpRunner):

    config = Config("司机出勤").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",
            "driverId": "",
            "date": "${hapentime(0,1)}",
            "type": ""

        })

    teststeps = [
        Step(
            RunRequest("/logis/api/mng/attendance/execute")
            .post("/logis/api/mng/attendance/execute")
            .with_headers(
                **{
                    "Content-Length": "35",
                    "Accept": "application/json, text/plain, */*",
                    "sessionId": "$session",
                    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
                    "Content-Type": "application/x-www-form-urlencoded",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                    "Connection": "keep-alive",
                }
            )
            .with_data({"driverId": "$driverId", "date": "$date", "type": "$type"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.statusCode", 2000)
        ),
    ]


if __name__ == "__main__":
    TestCase操作司机出勤().test_start()
