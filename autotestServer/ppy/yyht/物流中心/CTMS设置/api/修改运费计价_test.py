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


class TestCase修改运费计价(HttpRunner):

    config = Config("修改运费计价").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",
            "calculationRulesId": "1198962801147351544",
            "basicCharge": "120",
        })

    teststeps = [
        Step(
            RunRequest("/logis/api/mng/calculation/newModify")
            .post(
                "https://webapi.test.pinpianyi.cn/logis/api/mng/calculation/newModify"
            )
            .with_headers(
                **{
                    "Connection": "keep-alive",
                    "Content-Length": "731",
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
                    "basicCharge": "$basicCharge",
                    "driverType": 1,
                    "logisticsCalculationDetailParamList": [
                        {
                            "unitPrice": 0,
                            "startPrice": 0,
                            "calculationRulesId": "$calculationRulesId",
                            "rulesType": 3,
                            "startRules": 0,
                        },
                        {
                            "unitPrice": 0,
                            "startPrice": 0,
                            "calculationRulesId": "$calculationRulesId",
                            "rulesType": 4,
                            "startRules": 0,
                        },
                        {
                            "unitPrice": 1000,
                            "startPrice": 0,
                            "calculationRulesId": "$calculationRulesId",
                            "rulesType": 10,
                            "startRules": 0,
                            "minValue": 1000,
                            "maxValue": 10000,
                        },
                        {
                            "unitPrice": 5000,
                            "startPrice": 0,
                            "calculationRulesId": "$calculationRulesId",
                            "rulesType": 11,
                            "startRules": 0,
                        },
                        {
                            "unitPrice": 0,
                            "startPrice": 0,
                            "calculationRulesId": "$calculationRulesId",
                            "rulesType": 9,
                            "startRules": 0,
                        },
                    ],
                    "minimumCharge": 0,
                    "objId": "3310001",
                    "sortType": 2,
                    "vehicleType": "11",
                    "loadType": 2,
                    "mileageType": 2,
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.statusCode", 2000)
            .assert_equal("body.body", "操作成功")
        ),
    ]


if __name__ == "__main__":
    TestCase修改运费计价().test_start()

"""
{
	"statusCode": 2000,
	"msg": null,
	"traceMsg": "traceId: 1603096474407",
	"timestamp": 1603096474,
	"signType": null,
	"sign": null,
	"body": "操作成功"
}
"""
