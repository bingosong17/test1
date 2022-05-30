# NOTE: Generated By HttpRunner v3.1.4
"""
    概要：
        查看司机出勤状态
    输入参数：
        "driverId": "635"
        "date": "2020-09-17"
    输出参数：
       "content": "请假"
    前置接口：
        无
"""


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCase查看司机出勤状态(HttpRunner):

    config = Config("查看司机出勤状态").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",
            "driverId": "635",
            "date": "${hapentime(0,1)}",
        }).export(*["content"])

    teststeps = [
        Step(
            RunRequest("/logis/api/mng/attendance/dayStat")
            .post("/logis/api/mng/attendance/dayStat")
            .with_headers(
                **{
                    "Connection": "keep-alive",
                    "Content-Length": "28",
                    "Accept": "application/json, text/plain, */*",
                    "sessionId": "$session",
                    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
                    "Content-Type": "application/x-www-form-urlencoded",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                }
            )
            .with_data({"driverId": "$driverId", "date": "$date"}).extract()
            .with_jmespath("body.body.content", "content")

            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.statusCode", 2000)
        ),
    ]


if __name__ == "__main__":
    TestCase查看司机出勤状态().test_start()
"""
{
	"statusCode": 2000,
	"msg": null,
	"traceMsg": "traceId: 1600335324720",
	"timestamp": 1600335325,
	"signType": null,
	"sign": null,
	"body": {
		"attend": 1,
		"orders": 0,
		"content": "请假"
	}
}
"""