# NOTE: Generated By HttpRunner v3.1.3
"""
    概要：
        根据Id查询虚拟运单信息
    输入参数：
        "tempDistributeId": 临时唯一派单ID
    输出参数：
        无
    前置接口：
        用户登陆
"""

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCase根据Id查询虚拟运单信息(HttpRunner):

    config = Config("testcase description").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "",
            "session": "",
            "tempDistributeId": "1139128741300791106"
        })

    teststeps = [
        Step(
            RunRequest("根据Id查询虚拟运单信息")
            .post(
                "/logis/mng/virtual/queryVirtualDistributeOrderList"
            )
            .with_headers(
                **{
                    "Connection": "keep-alive",
                    "Content-Length": "42",
                    "Accept": "application/json, text/plain, */*",
                    "key": "",
                    "sessionId": "$session",
                    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36",
                    "Content-Type": "application/json",
                    "Sec-Fetch-Site": "same-site",
                    "Sec-Fetch-Mode": "cors",
                    "Sec-Fetch-Dest": "empty",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7",
                }
            )
            .with_json({"tempDistributeId": "$tempDistributeId"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.statusCode", 2000)
          ),
    ]


if __name__ == "__main__":
    TestCase根据Id查询虚拟运单信息().test_start()
"""
request:
{
	"tempDistributeId": "1139128741300791106"
}

response:
{
	"statusCode": 2000,
	"msg": null,
	"traceMsg": "traceId: 1597110545556",
	"timestamp": 1597110545,
	"signType": null,
	"sign": null,
	"body": {
		"tempDistributeId": "1139128741300791106",
		"virtualTransportationVOList": [{
			"id": "1139128741300791517",
			"tempDistributeId": "1139128741300791106",
			"vehicleId": "12",
			"driverId": null,
			"driver": null,
			"vehicleName": "金杯",
			"goodsAmount": 10,
			"volume": "0.1200",
			"volumeRate": "3.35",
			"load": 80.0,
			"loadRate": 4.0,
			"pickTotal": 1,
			"deliveryTotal": 1,
			"pickupMileage": 0.0,
			"deliveryMileage": 7025.0,
			"mileage": 7025.0,
			"freight": 2097,
			"freightRate": 2.66,
			"goodsTotalPrice": 787.0,
			"virtualCarsOrderVOList": [{
				"id": "1139128741301611195",
				"orderId": "2020081021034011214556",
				"virtualTransportationId": "1139128741300791517",
				"shopId": 322022,
				"shopName": "左邻右舍5115店",
				"shopBdLon": "120.299770421791140000",
				"shopBdLat": "30.179018551539150000",
				"supplierId": 9,
				"supplierName": "拼便宜供应链(自备仓)",
				"supplierAddress": "西兴",
				"supplierLongitude": "120.31327020160872",
				"supplierLatitude": "30.211272345386675",
				"orderCash": 787.0,
				"weight": 80.0,
				"volume": "0.1200",
				"goodsTypeAmount": 1,
				"typeAmount": 1,
				"totalAmount": 10,
				"phrchaseNumOfLogistics": 10,
				"zoneCode": "3310003",
				"zoneName": "城南-物流",
				"firstDelivery": 0
			}],
			"centerShopBdLon": 120.29977042179114,
			"centerShopBdLat": 30.17901855153915,
			"uuid": "329457",
			"calculateStatus": 0,
			"createTime": "2020-08-11T01:49:03.000+0000",
			"modifyTime": null,
			"cityCode": "330100",
			"errorMsg": null,
			"phrchaseNumOfLogistics": 10
		}],
		"orderNumSum": 1,
		"goodNumSum": 10,
		"carsTotalSum": 1,
		"vehicleInfoVOList": [{
			"vehicleId": "12",
			"vehicleName": "金杯",
			"num": 1
		}],
		"priceTotalSum": 787.0,
		"freightTotal": 2097.0,
		"freightRateTotal": 2.66,
		"deliveryTotalSum": 1,
		"pickupTotalSum": 1
	}
}
"""
