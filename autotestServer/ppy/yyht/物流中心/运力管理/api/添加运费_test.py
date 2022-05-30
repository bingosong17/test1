# NOTE: Generated By HttpRunner v3.1.4
"""
    概要：
        添加运费
    输入参数：
         "description": 单据名称
    输出参数：
        无
    前置接口：
        无
"""


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCase添加运费(HttpRunner):

    config = Config("添加运费").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",
            "description": "name",
            "driverId":""  # 315865121300152286
        })

    teststeps = [
        Step(
            RunRequest("/logis/transBill/operateCost/add")
            .post("/logis/transBill/operateCost/add")
            .with_headers(
                **{
                    "Connection": "keep-alive",
                    "Content-Length": "78",
                    "Accept": "application/json, text/plain, */*",
                    "sessionId": "$session",
                    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
                    "Content-Type": "application/json;charset=UTF-8",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                }
            )
            .with_json(
                {
                    "amount": 1000,
                    "description": "$description",
                    "driverId": "$driverId",
                    "type": "020",
                    "remark": "1",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.statusCode", 2000)
            .assert_equal("body.body", "操作成功")
        ),
    ]


if __name__ == "__main__":
    TestCase添加运费().test_start()

"""
{
	"statusCode": 2000,
	"msg": null,
	"traceMsg": "traceId: 1603076869580",
	"timestamp": 1603076869,
	"signType": null,
	"sign": null,
	"body": "操作成功"
}
"""