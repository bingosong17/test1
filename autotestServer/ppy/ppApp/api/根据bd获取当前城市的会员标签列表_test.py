# NOTE: Generated By HttpRunner v3.1.4
"""
    概要：
        根据bd获取当前城市的会员标签列表
    输入参数：
        无
    输出参数：
        无
    前置接口：
        无
"""


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCase根据Bd获取当前城市的会员标签列表(HttpRunner):

    config = Config("根据Bd获取当前城市的会员标签列表").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "ppApp",
            "phone": "15757113586",
            "session": "${getSession($business,$phone)}",
        })

    teststeps = [
        Step(
            RunRequest("/ppy-pinpin/myCustomer/getBdCityMemberLevel")
            .get("/myCustomer/getBdCityMemberLevel")
            .with_headers(
                **{
                    "sessionId": "$session",
                    "deviceId": "0380efdbdb0938af0d7a3852519f361a86ff",
                    "serviceName": "NEW-PP",
                    "Accept": "*/*",
                    "Version": "3.7.1",
                    "User-Agent": "Pinpin/3.7.1 (iPhone; iOS 11.1.2; Scale/3.00)",
                    "Accept-Language": "zh-Hans-CN;q=1",
                    "Accept-Encoding": "gzip, deflate",
                    "Connection": "keep-alive",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.statusCode", 2000)
        ),
    ]


if __name__ == "__main__":
    TestCase根据Bd获取当前城市的会员标签列表().test_start()
"""
response:
{
	"statusCode": 2000,
	"msg": null,
	"traceMsg": "traceId: null",
	"timestamp": 1603424963,
	"signType": null,
	"sign": null,
	"body": [{
		"id": 1,
		"memberLevelName": "普通会员"
	}, {
		"id": 4,
		"memberLevelName": "黄金会员"
	}, {
		"id": 7,
		"memberLevelName": "铂金会员"
	}, {
		"id": 10,
		"memberLevelName": "钻石会员"
	}]
}
"""