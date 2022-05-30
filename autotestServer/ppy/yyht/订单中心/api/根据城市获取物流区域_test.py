# NOTE: Generated By HttpRunner v3.1.3
"""
    概要：
        根据城市获取物流区域
    输入参数：
        "cityCode": 城市编码
    输出参数：
        无
    前置接口：
        无
"""


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
import env


class TestCase根据城市获取物流区域(HttpRunner):

    config = Config("根据城市获取物流区域").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "",
            "session": "",
            "cityCode": env.cityCode
        })

    teststeps = [
        Step(
            RunRequest("/dev2_t/ppy-op-api/common/cityCode")
            .get("/ppy-op-api/common/cityCode")
            .with_params(**{"cityCode": "$cityCode"})
            .with_headers(
                **{
                    "Connection": "keep-alive",
                    "sessionId": "$session",
                    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36",
                    "systemCode": "yypp",
                    "Accept": "*/*",
                    "Sec-Fetch-Site": "same-origin",
                    "Sec-Fetch-Mode": "cors",
                    "Sec-Fetch-Dest": "empty",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.statusCode", 2000)
        ),
    ]


if __name__ == "__main__":
    TestCase根据城市获取物流区域().test_start()

"""
{
	"statusCode": 2000,
	"msg": null,
	"traceMsg": "traceId: 1598405728280",
	"timestamp": 1598405728,
	"signType": null,
	"sign": null,
	"body": [{
		"logisTraId": 14,
		"logisticsArea": "3310001",
		"areaName": "北区-物流",
		"distributionInTime": null
	}, {
		"logisTraId": 17,
		"logisticsArea": "3310002",
		"areaName": "城东-物流",
		"distributionInTime": null
	}, {
		"logisTraId": 20,
		"logisticsArea": "3310003",
		"areaName": "城南-物流",
		"distributionInTime": null
	}, {
		"logisTraId": 23,
		"logisticsArea": "3310004",
		"areaName": "拼便宜-物流",
		"distributionInTime": null
	}]
}
"""