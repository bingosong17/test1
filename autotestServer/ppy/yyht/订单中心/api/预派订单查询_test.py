# NOTE: Generated By HttpRunner v3.1.3
"""
    概要：
        根据订单号进行预派订单查询
    输入参数：
        "orderNo": 订单号
    输出参数：
        无
    前置接口：
        无
"""


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase



class TestCase预派订单查询(HttpRunner):

    config = Config("预派订单查询").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "",
            "session": "",
            "orderNo": "2020082610413214718486",
        })

    teststeps = [
        Step(
            RunRequest("/alpha_t/ppy-op-api/order/searchPredistributeOrder")
            .get(
                "/ppy-op-api/order/searchPredistributeOrder"
            )
            .with_params(
                **{
                    "isPay": "",
                    "payType": "",
                    "status": "",
                    "queryType": "",
                    "cloudType": "",
                    "labelCode": "",
                    "orderSource": "",
                    "backGoodsType": "",
                    "settleStatus": "",
                    "spellZoneCode": "",
                    "logisticsStatus": "",
                    "isInsufficient": "",
                    "orderClassify": "",
                    "orderNo": "$orderNo",
                    "pageNum": "1",
                    "pageSize": "10",
                    "sort": "true",
                    "cStartTime": "2020-08-19 16:00:00",
                    "cEndTime": "2020-08-26 16:00:00",
                }
            )
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
    TestCase预派订单查询().test_start()
"""
response:
{
	"statusCode": 2000,
	"msg": null,
	"traceMsg": "traceId: 1598413801539",
	"timestamp": 1598413801,
	"signType": null,
	"sign": null,
	"body": {
		"pageNum": 1,
		"pageSize": 10,
		"pageCount": 1,
		"totalSize": 1,
		"pageData": [{
			"orderNo": "2020082610413214718486",
			"dmZoneName": "萧山区",
			"streetName": "新街镇",
			"spellZoneName": "城南-物流",
			"shopName": "家园超市",
			"orderCash": "787.00",
			"orderStatus": "210",
			"status": "已派单",
			"transOrderStatus": null,
			"payType": "在线支付",
			"supplierName": "拼便宜供应链",
			"driverName": null,
			"distributeTime": "2020-08-26 10:57:55",
			"markId": null,
			"shopType": "00",
			"shopLabel": "普通会员VIP1",
			"orderSource": null,
			"mallTraName": "萧山-商圈",
			"orderClassify": 2,
			"orderClassifyText": "B品类"
		}]
	}
}
"""