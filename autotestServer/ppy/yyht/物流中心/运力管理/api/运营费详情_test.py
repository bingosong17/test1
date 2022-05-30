# NOTE: Generated By HttpRunner v3.1.4
"""
    概要：
        运营费详情
    输入参数：
        id  运营单据 id
    输出参数：
        "id",运费单据id
        "description" 单据名称
    前置接口：
        无
"""


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCase运营费详情(HttpRunner):

    config = Config("运营费详情").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",
            "id": "1198741091140351807"
        }).export(*["id","description"])

    teststeps = [
        Step(
            RunRequest("/logis/transBill/operateCost/detail")
            .post("/logis/transBill/operateCost/detail")
            .with_params(**{"id": "$id"})
            .with_headers(
                **{
                    "Connection": "keep-alive",
                    "Content-Length": "0",
                    "Accept": "application/json, text/plain, */*",
                    "sessionId": "$session",
                    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                }
            ).extract()
                .with_jmespath("body.body.id","id")
                .with_jmespath("body.body.description", "description")
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.statusCode", 2000)
        ),
    ]


if __name__ == "__main__":
    TestCase运营费详情().test_start()

"""
{
	"statusCode": 2000,
	"msg": null,
	"traceMsg": "traceId: 1603076657448",
	"timestamp": 1603076657,
	"signType": null,
	"sign": null,
	"body": {
		"id": "1198741091140351807",
		"driverId": "68",
		"driverName": "周兰涛1111",
		"driverPhone": "13738113393",
		"vehicleName": "金杯",
		"driverType": 1,
		"type": "020",
		"typeValue": "运营费",
		"amount": 100,
		"status": 10,
		"valid": 1,
		"description": "nice",
		"remark": "1",
		"voucherList": null,
		"createTime": "2020-10-19 10:21:49",
		"updateTime": "2020-10-19 10:55:18",
		"operationLogVOList": [{
			"operator": "李浩",
			"operateTime": "2020-10-19 10:55",
			"content": "单据更新状态【待确认】至【待业务审核】"
		}, {
			"operator": "李浩",
			"operateTime": "2020-10-19 10:28",
			"content": "修改运营费用：司机【68-周兰涛1111】,金额【1.00】,原因【运营费】,名称【nice】,详细描述【1】,凭证【null】"
		}, {
			"operator": "李浩",
			"operateTime": "2020-10-19 10:21",
			"content": "新增运营费用：司机【68-周兰涛1111】,金额【1.00】,原因【运营费】,名称【11】,详细描述【1】,凭证【null】"
		}]
	}
}
"""