# NOTE: Generated By HttpRunner v3.1.3
"""
    概要：
        司机app端提供二维码给客户扫描确认取货
    输入参数：
        "orderRelId": 包裹id,
    输出参数：
        无
    前置接口：
        用户登陆
"""

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCase生成用户确认二维码(HttpRunner):

    config = Config("testcase description").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "",
            "token": "",
            "userId": "",
            "orderRelId": 1137694291309851766,
        }
    )

    teststeps = [
        Step(
            RunRequest("/ppy-logis-driver-api/api/delivery/commitConfirmInfo")
            .post(
                "/ppy-logis-driver-api/api/delivery/commitConfirmInfo"
            )
            .with_headers(
                **{
                    "Content-Length": "166",
                    "Connection": "Keep-Alive",
                    "Accept-Encoding": "gzip",
                    "User-Agent": "okhttp/3.14.1",
                    "Content-Type": "application/json",
                    "Accept-Language": "zh-CN,zh;q=0.8",
                }
            )
            .with_json(
                {
                    "body": {"orderRelId": "$orderRelId"},
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
    TestCase生成用户确认二维码().test_start()

"""
request:
{
	"body": {
		"orderRelId": 1137694291309851766
	},
	"head": {
		"channelId": "",
		"platform": "Android",
		"token": "14e6704b-154f-492d-a7ce-d7571211dac4",
		"userId": 68,
		"version": "2.11.2"
	}
}

response:
{
	"statusCode": 2000,
	"msg": null,
	"traceMsg": "traceId: 1597027355951",
	"timestamp": 1597027356,
	"signType": null,
	"sign": null,
	"body": {
		"orderRelId": 1137694291309851766,
		"payAmount": null,
		"paymentURL": "https://logis.alpha.pinpianyi.cn/ppy-logis-driver-api/api/user/auth?orderRelId=1137694291309851766&payType=1",
		"takePhotoSwitch": 1,
		"isWaitingPay": 1,
		"orderNo": "514444"
	}
}
"""