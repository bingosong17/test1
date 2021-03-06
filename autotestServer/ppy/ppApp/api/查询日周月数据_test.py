# NOTE: Generated By HttpRunner v3.1.4
"""
    概要：
        查询日周月数据
    输入参数：
        无
    输出参数：
        无
    前置接口：
        无
"""


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCase查询日周月数据(HttpRunner):

    config = Config("查询日周月数据").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "ppApp",
            "phone": "13797912089",
            "session": "${getSession($business,$phone)}",
        })

    teststeps = [
        Step(
            RunRequest("/ppy-pinpin/stats/total")
            .get("/stats/total")
            .with_headers(
                **{
                    "sessionId": "$session",
                    "deviceId": "0380efdbdb0938af0d7a3852519f361a86ff",
                    "serviceName": "NEW-PP",
                    "Content-Type": "application/json",
                    "Accept": "*/*",
                    "User-Agent": "Pinpin/3.7.0 (iPhone; iOS 11.1.2; Scale/3.00)",
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
    TestCase查询日周月数据().test_start()
"""
response:
{
	"statusCode": 2000,
	"msg": null,
	"traceMsg": "traceId: null",
	"timestamp": 1603007959,
	"signType": null,
	"sign": null,
	"body": {
		"tOrderShops": 0,       今日下单用户
		"tOrders": 0,       今日订单数
		"tGmv": "0.00",     今日GMV
		"tRegister": 0,     今日注册数
		"tVisit": 0,        今日拜访数
		"tOfv": 0,      今日转化订单数
		"tRecharge": "0.00",        今日充值
		"tAvgOrderPrice": "0.00",       今日客单价
		"tAvgShopSkuCount": "0.00",     今日人均SKU
		"tRegisteredActivateNum": 0,        今日注册激活数
		"tDormancyActivateNum": 0,      今日休眠激活数
		"tSevenDormancyActivateNum": 0,     今日7天激活数
		"tGmvA": "0.00",
		"tGmvB": "0.00",
		"yOrderShops": 0,
		"yOrders": 0,
		"yGmv": "0.00",
		"yRegister": 0,
		"yVisit": 0,
		"yOfv": 0,
		"yRecharge": "0.00",
		"yAvgOrderPrice": "0.00",
		"yAvgShopSkuCount": "0.00",
		"yRegisteredActivateNum": 0,
		"yDormancyActivateNum": 0,
		"ySevenDormancyActivateNum": 0,
		"yGmvA": "0.00",
		"yGmvB": "0.00",
		"wOrderShops": 0,
		"wOrders": 0,
		"wGmv": "0.00",
		"wRegister": 0,
		"wVisit": 0,
		"wOfv": 0,
		"wRecharge": "0.00",
		"wAvgOrderPrice": "0.00",
		"wAvgShopSkuCount": "0.00",
		"wRegisteredActivateNum": 0,
		"wDormancyActivateNum": 0,
		"wSevenDormancyActivateNum": 0,
		"wGmvA": "0.00",
		"wGmvB": "0.00",
		"mOrderShops": 0,
		"mOrders": 0,
		"mGmv": "0.00",
		"mRegister": 0,
		"mVisit": 0,
		"mOfv": 0,
		"mRecharge": "0.00",
		"mAvgOrderPrice": "0.00",
		"mAvgShopSkuCount": "0.00",
		"mRegisteredActivateNum": 0,
		"mDormancyActivateNum": 0,
		"mSevenDormancyActivateNum": 0,
		"mGmvA": "0.00",
		"mGmvB": "0.00",
		"categoryGmvVOS": [{
			"categoryName": "方便速食GMV(万）",
			"tgmv": "0.00",
			"ygmv": "0.00",
			"wgmv": "0.00",
			"mgmv": "0.00"
		}, {
			"categoryName": "个人护理GMV(万）",
			"tgmv": "0.00",
			"ygmv": "0.00",
			"wgmv": "0.00",
			"mgmv": "0.00"
		}, {
			"categoryName": "家居清洁GMV(万）",
			"tgmv": "0.00",
			"ygmv": "0.00",
			"wgmv": "0.00",
			"mgmv": "0.00"
		}, {
			"categoryName": "冷冻食品GMV(万）",
			"tgmv": "0.00",
			"ygmv": "0.00",
			"wgmv": "0.00",
			"mgmv": "0.00"
		}, {
			"categoryName": "日用杂百GMV(万）",
			"tgmv": "0.00",
			"ygmv": "0.00",
			"wgmv": "0.00",
			"mgmv": "0.00"
		}, {
			"categoryName": "休闲食品GMV(万）",
			"tgmv": "0.00",
			"ygmv": "0.00",
			"wgmv": "0.00",
			"mgmv": "0.00"
		}, {
			"categoryName": "母婴玩具GMV(万）",
			"tgmv": "0.00",
			"ygmv": "0.00",
			"wgmv": "0.00",
			"mgmv": "0.00"
		}, {
			"categoryName": "组合商品GMV(万）",
			"tgmv": "0.00",
			"ygmv": "0.00",
			"wgmv": "0.00",
			"mgmv": "0.00"
		}, {
			"categoryName": "自配商品GMV(万）",
			"tgmv": "0.00",
			"ygmv": "0.00",
			"wgmv": "0.00",
			"mgmv": "0.00"
		}, {
			"categoryName": "乳品冲饮GMV(万）",
			"tgmv": "0.00",
			"ygmv": "0.00",
			"wgmv": "0.00",
			"mgmv": "0.00"
		}, {
			"categoryName": "酒类GMV(万）",
			"tgmv": "0.00",
			"ygmv": "0.00",
			"wgmv": "0.00",
			"mgmv": "0.00"
		}, {
			"categoryName": "酱菜干调GMV(万）",
			"tgmv": "0.00",
			"ygmv": "0.00",
			"wgmv": "0.00",
			"mgmv": "0.00"
		}, {
			"categoryName": "粮油米面GMV(万）",
			"tgmv": "0.00",
			"ygmv": "0.00",
			"wgmv": "0.00",
			"mgmv": "0.00"
		}, {
			"categoryName": "测试看看GMV(万）",
			"tgmv": "0.00",
			"ygmv": "0.00",
			"wgmv": "0.00",
			"mgmv": "0.00"
		}]
	}
}
"""