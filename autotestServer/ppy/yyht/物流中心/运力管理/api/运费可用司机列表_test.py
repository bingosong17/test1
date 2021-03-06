# NOTE: Generated By HttpRunner v3.1.4
"""
    概要：
        运费可用司机列表
    输入参数：
        无
    输出参数：
        driverId 司机id
    前置接口：
        无
"""


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCase运费可用司机列表(HttpRunner):

    config = Config("运费可用司机列表").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",
        }).export(*["driverId"])

    teststeps = [
        Step(
            RunRequest("/logis/api/mng/drivers/list")
            .post("/logis/api/mng/drivers/list")
            .with_headers(
                **{
                    "Connection": "keep-alive",
                    "Content-Length": "85",
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
                    "name": "",
                    "pageNum": 1,
                    "pageSize": 9999,
                    "accountStatus": 50,
                    "driverTypeList": [1, 50, 40],
                }
            ).extract()
                .with_jmespath("body.body.pageData[0].id","driverId")
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.statusCode", 2000)
        ),
    ]


if __name__ == "__main__":
    TestCase运费可用司机列表().test_start()

"""
{
	"statusCode": 2000,
	"msg": null,
	"traceMsg": "traceId: 1603076908140",
	"timestamp": 1603076908,
	"signType": null,
	"sign": null,
	"body": {
		"pageNum": 1,
		"pageSize": 9999,
		"pageCount": 1,
		"totalSize": 454,
		"pageData": [{
			"id": "68",
			"name": "周兰涛1111",
			"phoneNumber": "13738113393",
			"homeZoneCode": "330108",
			"cooperationStatus": 50,
			"vehicleTypeName": "金杯",
			"serviceManagerName": "高道林",
			"serviceId": 268,
			"vehicleType": 12,
			"licensePlateNumber": "浙AK8M05",
			"signDate": null,
			"accountStatus": 50,
			"driverType": 1
		}, {
			"id": "174",
			"name": "拼便宜测试号",
			"phoneNumber": "15605811626",
			"homeZoneCode": "330108",
			"cooperationStatus": 50,
			"vehicleTypeName": "金杯",
			"serviceManagerName": "高道林",
			"serviceId": 268,
			"vehicleType": 12,
			"licensePlateNumber": "",
			"signDate": null,
			"accountStatus": 50,
			"driverType": 40
		}]
	}
}
"""