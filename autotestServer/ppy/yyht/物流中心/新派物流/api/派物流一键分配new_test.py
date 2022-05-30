# NOTE: Generated By HttpRunner v3.1.4
"""
    概要：
        派物流一键分配new
    输入参数：
        "tempDistributeId": 调用运力匹配返回返回
        "orderIds": 订单列表
    输出参数：
        无
    前置接口：
        无
"""


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCase派物流一键分配New(HttpRunner):

    config = Config("派物流一键分配New").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",
            "orderIds": [],
            "tempDistributeId": None,
        }).export(*["executePageData"])

    teststeps = [
        Step(
            RunRequest("/ppy-op-api/transCapacitys/execute")
            .post("/ppy-op-api/transCapacitys/execute")
            .with_headers(
                **{
                    "Connection": "keep-alive",
                    "Content-Length": "26697",
                    "Accept": "application/json, text/plain, */*",
                    "key": "",
                    "sessionId": "$session",
                    "Content-Type": "application/json",
                    "Sec-Fetch-Site": "same-site",
                    "Sec-Fetch-Mode": "cors",
                    "Sec-Fetch-Dest": "empty",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7",
                }
            )
            .with_json(
                {
                    "orderIds": [
                        "2020110916021716016307-1",
                        "2020111008133116016822-6",
                    ],
                    "tempDistributeId": None,
                }
            ).extract()
            .with_jmespath("body.body[0].results", "executePageData")
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.statusCode", 2000)
        ),
    ]


if __name__ == "__main__":
    TestCase派物流一键分配New().test_start()
# response:
# {
# 	"statusCode": 2000,
# 	"msg": null,
# 	"traceMsg": "traceId: 1605000637151",
# 	"timestamp": 1605000644,
# 	"signType": null,
# 	"sign": null,
# 	"body": [{
# 		"logisticsArea": "3310001",
# 		"logisticsName": "杭州北区",
# 		"number": 1615,
# 		"foodTypeNum": 18,
# 		"foodNumber": 31,
# 		"results": [{
# 			"id": "1218006391944421304",
# 			"batchOn": "1218006381942621182",
# 			"vehicleType": 11,
# 			"vehicleTypeName": "小面包",
# 			"recommendNum": 0,
# 			"actualNum": null,
# 			"vehicleName": "小面包"
# 		}, {
# 			"id": "1218006391944421306",
# 			"batchOn": "1218006381942621182",
# 			"vehicleType": 12,
# 			"vehicleTypeName": "金杯",
# 			"recommendNum": 0,
# 			"actualNum": null,
# 			"vehicleName": "金杯"
# 		}, {
# 			"id": "1218006391944421313",
# 			"batchOn": "1218006381942621182",
# 			"vehicleType": 13,
# 			"vehicleTypeName": "中面",
# 			"recommendNum": 0,
# 			"actualNum": null,
# 			"vehicleName": "中面"
# 		}, {
# 			"id": "1218006391944421317",
# 			"batchOn": "1218006381942621182",
# 			"vehicleType": 14,
# 			"vehicleTypeName": "高顶金杯",
# 			"recommendNum": 0,
# 			"actualNum": null,
# 			"vehicleName": "高顶金杯"
# 		}, {
# 			"id": "1218006391944421322",
# 			"batchOn": "1218006381942621182",
# 			"vehicleType": 15,
# 			"vehicleTypeName": "全顺",
# 			"recommendNum": 7,
# 			"actualNum": null,
# 			"vehicleName": "全顺"
# 		}, {
# 			"id": "1218006391944421324",
# 			"batchOn": "1218006381942621182",
# 			"vehicleType": 16,
# 			"vehicleTypeName": "依维柯",
# 			"recommendNum": 1,
# 			"actualNum": null,
# 			"vehicleName": "依维柯"
# 		}, {
# 			"id": "1218006391944421333",
# 			"batchOn": "1218006381942621182",
# 			"vehicleType": 17,
# 			"vehicleTypeName": "4.2箱货",
# 			"recommendNum": 0,
# 			"actualNum": null,
# 			"vehicleName": "4.2箱货"
# 		}, {
# 			"id": "1218006391944421339",
# 			"batchOn": "1218006381942621182",
# 			"vehicleType": 21,
# 			"vehicleTypeName": "B类小面包",
# 			"recommendNum": 0,
# 			"actualNum": null,
# 			"vehicleName": "B类小面包"
# 		}, {
# 			"id": "1218006391944421344",
# 			"batchOn": "1218006381942621182",
# 			"vehicleType": 22,
# 			"vehicleTypeName": "B类金杯",
# 			"recommendNum": 0,
# 			"actualNum": null,
# 			"vehicleName": "B类金杯"
# 		}, {
# 			"id": "1218006391944421353",
# 			"batchOn": "1218006381942621182",
# 			"vehicleType": 23,
# 			"vehicleTypeName": "B类中面",
# 			"recommendNum": 0,
# 			"actualNum": null,
# 			"vehicleName": "B类中面"
# 		}]
# 	}]
# }