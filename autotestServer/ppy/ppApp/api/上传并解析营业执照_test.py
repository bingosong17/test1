# NOTE: Generated By HttpRunner v3.1.4
"""
    概要：
        上传并解析营业执照
    输入参数：
        无
    输出参数：
        无
    前置接口：
        无
"""


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from files import fileData


class TestCase上传并解析营业执照(HttpRunner):

    config = Config("上传并解析营业执照").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "ppApp",
            "phone": "13797912089",
            "session": "${getSession($business,$phone)}",
        })

    teststeps = [
        Step(
            RunRequest("/ppy-pinpin/myCustomer/businessLicensePhoto")
            .post("/myCustomer/businessLicensePhoto")
            .with_headers(
                **{
                    "Accept": "application/json",
                    "channel": "app",
                    "Accept-Language": "zh-Hans-CN;q=1",
                    "Accept-Encoding": "gzip, deflate",
                    "Content-Type": "application/json",
                    "sessionId": "$session",
                    "deviceId": "0380efdbdb0938af0d7a3852519f361a86ff",
                    "Content-Length": "949241",
                    "serviceName": "NEW-PP",
                    "Connection": "keep-alive",
                }
            )
            .with_json(
                {
                    "fileBase64Data": fileData.有效营业执照
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.statusCode", 2000)
        ),
    ]


if __name__ == "__main__":
    TestCase上传并解析营业执照().test_start()
"""
response:
{
	"statusCode": 2000,
	"msg": null,
	"traceMsg": "traceId: null",
	"timestamp": 1603078810,
	"signType": null,
	"sign": null,
	"body": {
		"possessType": null,
		"recordType": null,
		"recordRemark": null,
		"picUrl": "https://images.alpha.pinpianyi.cn/images/common/10ef5eb288b6429c9e9d18d861cbea89.jpg",
		"socialCreditCode": "91110108MA01EBFH9B",
		"registrationNumber": null,
		"companyName": "北京妙树托育服务有限公司",
		"companyAddress": "北京市朝阳区狮家坡村156号3幢1层06号",
		"legalRepresentative": "孙期",
		"establishDate": "20180829",
		"validity": "长期",
		"companyType": "其他有限责任公司"
	}
}
"""