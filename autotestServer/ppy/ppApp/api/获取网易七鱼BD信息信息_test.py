# NOTE: Generated By HttpRunner v3.1.4
"""
    概要：
        获取网易七鱼BD信息信息
    输入参数：
        无
    输出参数：
        无
    前置接口：
        无
"""


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCase获取网易七鱼Bd信息信息(HttpRunner):

    config = Config("获取网易七鱼Bd信息信息").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "ppApp",
            "phone": "13797912089",
            "session": "${getSession($business,$phone)}",
        })

    teststeps = [
        Step(
            RunRequest("/ppy-pinpin/user/account/operatorInfoQiyu")
            .get("/user/account/operatorInfoQiyu")
            .with_headers(
                **{
                    "channel": "app",
                    "Accept-Language": "zh-Hans-CN;q=1",
                    "Accept-Encoding": "gzip, deflate",
                    "Accept": "application/json",
                    "sessionId": "$session",
                    "deviceId": "0380efdbdb0938af0d7a3852519f361a86ff",
                    "User-Agent": "Pinpin/3.7.0 (iPhone; iOS 11.1.2; Scale/3.00)",
                    "serviceName": "NEW-PP",
                    "Connection": "keep-alive",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.statusCode", 2000)
        ),
    ]


if __name__ == "__main__":
    TestCase获取网易七鱼Bd信息信息().test_start()
"""
response:
{
	"statusCode": 2000,
	"msg": null,
	"traceMsg": "traceId: null",
	"timestamp": 1603073343,
	"signType": null,
	"sign": null,
	"body": [{
		"key": "bdId",
		"value": "706",
		"label": "BdId",
		"index": null,
		"href": "",
		"edit": false,
		"map": "",
		"save": false,
		"zone": false,
		"select": false,
		"check": false
	}, {
		"key": "bdName",
		"value": "王迪",
		"label": "BD名称",
		"index": null,
		"href": "",
		"edit": false,
		"map": "",
		"save": false,
		"zone": false,
		"select": false,
		"check": false
	}, {
		"key": "bdPhone",
		"value": "13797912089",
		"label": "手机号",
		"index": null,
		"href": "",
		"edit": false,
		"map": "",
		"save": false,
		"zone": false,
		"select": false,
		"check": false
	}, {
		"key": "businessLineDes",
		"value": "城市站",
		"label": "业务线",
		"index": null,
		"href": "",
		"edit": false,
		"map": "",
		"save": false,
		"zone": false,
		"select": false,
		"check": false
	}, {
		"key": "cityName",
		"value": "武汉站",
		"label": "城市站",
		"index": null,
		"href": "",
		"edit": false,
		"map": "",
		"save": false,
		"zone": false,
		"select": false,
		"check": false
	}, {
		"key": "position",
		"value": "BDM",
		"label": "职级",
		"index": null,
		"href": "",
		"edit": false,
		"map": "",
		"save": false,
		"zone": false,
		"select": false,
		"check": false
	}, {
		"key": "regionName",
		"value": "武昌战队",
		"label": "战区",
		"index": null,
		"href": "",
		"edit": false,
		"map": "",
		"save": false,
		"zone": false,
		"select": false,
		"check": false
	}, {
		"key": "leaderName",
		"value": "詹元辉",
		"label": "上级主管",
		"index": null,
		"href": "",
		"edit": false,
		"map": "",
		"save": false,
		"zone": false,
		"select": false,
		"check": false
	}, {
		"key": "shopId",
		"value": null,
		"label": "咨询店铺Id",
		"index": null,
		"href": "",
		"edit": false,
		"map": "",
		"save": false,
		"zone": false,
		"select": false,
		"check": false
	}, {
		"key": "shopName",
		"value": null,
		"label": "咨询店铺",
		"index": null,
		"href": "",
		"edit": false,
		"map": "",
		"save": false,
		"zone": false,
		"select": false,
		"check": false
	}]
}
"""