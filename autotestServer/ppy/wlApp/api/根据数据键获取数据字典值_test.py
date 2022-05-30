# NOTE: Generated By HttpRunner v3.1.3


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCase根据数据键获取数据字典值(HttpRunner):

    config = Config("testcase description").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "",
            "token": "",
            "userId": "",
        }
    )

    teststeps = [
        Step(
            RunRequest("根据数据键获取数据字典值")
            .post(
                "/ppy-logis-driver-api/api/dict/dataval"
            )
            .with_headers(
                **{
                    "Content-Length": "169",
                    "Connection": "Keep-Alive",
                    "Accept-Encoding": "gzip",
                    "User-Agent": "okhttp/3.14.1",
                    "Content-Type": "application/json",
                    "Accept-Language": "zh-CN,zh;q=0.8",
                }
            )
            .with_json(
                {
                    "body": {"dataCode": "PICKUP_DISTANCE_LIMIT"},
                    "head": {
                        "channelId": "",
                        "platform": "Android",
                        "token": "$token",
                        "userId": "$userId",
                        "version": "${wlversion()}"},
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.statusCode", 2000)
        ),
    ]


if __name__ == "__main__":
    TestCase根据数据键获取数据字典值().test_start()

"""
request:
{
	"body": {
		"dataCode": "PICKUP_DISTANCE_LIMIT"
	},
	"head": {
		"channelId": "",
		"platform": "Android",
		"token": "a6495678-47fa-494c-a575-16e1ebcc7894",
		"userId": 256,
		"version": "2.11.2"
	}
}

response:
{
	"statusCode": 2000,
	"msg": null,
	"traceMsg": "traceId: 1597127051882",
	"timestamp": 1597127051,
	"signType": null,
	"sign": null,
	"body": {
		"id": null,
		"pId": null,
		"dataType": null,
		"dataCode": null,
		"dataValue": null,
		"sortNo": null,
		"dataDesc": null,
		"createTime": null,
		"updateTime": null
	}
}
"""