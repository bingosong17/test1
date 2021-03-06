# NOTE: Generated By HttpRunner v3.1.4
"""
    概要：
        送货单打印页搜索司机
    输入参数：
        driverNameOrPhone 司机名称后手机号
    输出参数：
        "name", 司机名称
        "phoneNumber"   手机号
    前置接口：
        无
"""


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCase送货单打印页搜索司机(HttpRunner):

    config = Config("送货单打印页搜索司机").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "wlApp",
            "phoneNumber": "15997336112",
            "token": "${getSession($business,$phoneNumber)}",
            "userId": "${getWlAppUserId($phoneNumber)}",
            "driverNameOrPhone": "杨杨"  # 15997336112
        }).export(*["name", "phoneNumber"])

    teststeps = [
        Step(
            RunRequest("/ppy-logis-driver-api/api/drivers/queryDriver")
            .post(
                "/ppy-logis-driver-api/api/drivers/queryDriver"
            )
            .with_headers(
                **{
                    "Content-Length": "164",
                    "Connection": "Keep-Alive",
                    "Accept-Encoding": "gzip",
                    "User-Agent": "okhttp/3.12.1",
                    "Content-Type": "application/json",
                    "Accept-Language": "zh-CN,zh;q=0.8",
                }
            )
            .with_json(
                {
                    "body": {"driverNameOrPhone": "$driverNameOrPhone"},
                    "head": {
                        "channelId": "",
                        "platform": "Android",
                        "token": "$token",
                        "userId": "$userId",
                        "version": "${wlversion()}"
                    },
                }
            ).extract()
                .with_jmespath("body.body[0].name", "name")
                .with_jmespath("body.body[0].phoneNumber", "phoneNumber")
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.statusCode", 2000)
        ),
    ]


if __name__ == "__main__":
    TestCase送货单打印页搜索司机().test_start()
"""
{
	"statusCode": 2000,
	"msg": null,
	"traceMsg": "traceId: 1603882283820",
	"timestamp": 1603882283,
	"signType": null,
	"sign": null,
	"body": [{
		"id": 2587,
		"name": "杨杨",
		"phoneNumber": "15997336112"
	}]
}
"""