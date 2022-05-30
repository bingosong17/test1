# NOTE: Generated By HttpRunner v3.1.4
"""
    概要：
        无
    输入参数：
         "operateCostDetailId": 运费单据id
    输出参数：
        无
    前置接口：
        无
"""


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCase业务审核通过(HttpRunner):

    config = Config("业务审核通过").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",
            "ids": ["1190367971144901704"]
        })

    teststeps = [
        Step(
            RunRequest("/logis/transBill/operateCost/bathBusinessReview")
            .post(
                "/logis/transBill/operateCost/bathBusinessReview"
            )
            .with_headers(
                **{
                    "Connection": "keep-alive",
                    "Content-Length": "31",
                    "Accept": "application/json, text/plain, */*",
                    "sessionId": "$session",
                    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
                    "Content-Type": "application/json;charset=UTF-8",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                }
            )
            .with_json({"ids":"$ids"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.statusCode", 2000)
            .assert_equal("body.body", "操作成功")
        ),
    ]


if __name__ == "__main__":
    TestCase业务审核通过().test_start()

"""
{
	"statusCode": 2000,
	"msg": null,
	"traceMsg": "traceId: 1603088325034",
	"timestamp": 1603088325,
	"signType": null,
	"sign": null,
	"body": "操作成功"
}
"""