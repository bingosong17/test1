# NOTE: Generated By HttpRunner v3.1.4
"""
    概要：
        商铺明细
    输入参数：
        "shopId": 店铺ID
    输出参数：
        "longitude": 经度
		"latitude": 纬度，
    前置接口：
        无
"""

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCase商铺明细(HttpRunner):
    config = Config("商铺明细").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",
            "shopId": 333938
        }).export(*["longitude", "latitude"])

    teststeps = [
        Step(
            RunRequest("/test_t/mall/user/shopDetail")
                .post("/mall/user/shopDetail")
                .with_headers(
                **{
                    "Connection": "keep-alive",
                    "Content-Length": "13",
                    "sessionId": "$session",
                    "systemCode": "yypp",
                    "Content-Type": "application/x-www-form-urlencoded",
                    "Accept": "*/*",
                    "Sec-Fetch-Site": "same-origin",
                    "Sec-Fetch-Mode": "cors",
                    "Sec-Fetch-Dest": "empty",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7",
                }
            )
            .with_data({"shopId": "$shopId"})
            .extract()
            .with_jmespath("body.body.longitude", "longitude")
            .with_jmespath("body.body.latitude", "latitude")
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.statusCode", 2000)
        ),
    ]


if __name__ == "__main__":
    TestCase商铺明细().test_start()
"""
response:
{
	"statusCode": 2000,
	"msg": null,
	"traceMsg": "traceId: null",
	"timestamp": 1603703635,
	"signType": null,
	"sign": null,
	"body": {
		"uid": "51602662347409442",
		"shopId": 343408,
		"shopName": "七月",
		"registerMobile": "13387525099",
		"contactMobilePhone": "13387525099",
		"contactUserName": "和",
		"zoneCode": "330109",
		"zoneName": "萧山区",
		"streetCode": "330109401",
		"streetName": "萧山经济技术开发区",
		"shopAddress": "详细地址在吃饭",
		"fullAddress": "杭州市市萧山区 萧山经济技术开发区 详细地址在吃饭",
		"headerPics": "https://images.alpha.pinpianyi.cn/images/common/3c7537195ad64173b063d88be514d0e8.jpg",
		"shopStatus": 1,
		"shopStatusName": "正常",
		"shopTags": "",
		"shopTagList": null,
		"shopTagName": null,
		"shopType": "00",
		"shopTypeName": "便利店",
		"longitude": 120.26033500000003,
		"latitude": 30.203654000000007,
		"bdId": -1,
		"regionId": 128,
		"regionName": "麒麟战队",
		"traName": "萧山-商圈",
		"logisTraName": "城南-物流",
		"stockFrequency": null,
		"stockChannels": "",
		"userClass": "",
		"shopArea": null,
		"registerType": "自主注册",
		"registerBd": null,
		"registerTime": "2020-10-14 15:59:07",
		"businesStart": "",
		"businesEnd": "",
		"cashOnDelivery": 1,
		"userBranchList": [],
		"businessLicense": null
	}
}
"""
