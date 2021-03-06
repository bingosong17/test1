# NOTE: Generated By HttpRunner v3.1.4
"""
    概要：
        查询拜访记录
    输入参数：
        "shopId": 商店id
        "signType": 拜访对象类型 1表示店铺,2虚拟店铺,3表示供应商,4虚拟供应商
    输出参数：
        无
    前置接口：
        无
"""


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCase查询拜访记录(HttpRunner):

    config = Config("查询拜访记录").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "ppApp",
            "phone": "15757113586",
            "session": "${getSession($business,$phone)}",
            "shopId": 1073,
            "signType": 1
        })

    teststeps = [
        Step(
            RunRequest("/ppy-pinpin/visitRecord/queryVisitRecord")
            .post("/visitRecord/queryVisitRecord")
            .with_headers(
                **{
                    "Accept": "*/*",
                    "channel": "app",
                    "appname": "",
                    "Accept-Language": "zh-cn",
                    "Accept-Encoding": "gzip, deflate",
                    "platform": "ios",
                    "Content-Type": "application/json",
                    "sessionid": "$session",
                    "deviceid": "1F8ED797-D036-4BA3-BEAA-A176B0E08BD6",
                    "Content-Length": "15",
                    "User-Agent": "Pinpin/3.7.1.20201023100053 CFNetwork/889.9 Darwin/17.2.0",
                    "appchannel": "appstore",
                    "servicename": "NEW-PP",
                    "Connection": "keep-alive",
                }
            )
            .with_json({"shopId": "$shopId", "signType": "$signType"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.statusCode", 2000)
        ),
    ]


if __name__ == "__main__":
    TestCase查询拜访记录().test_start()
"""
response:
{
	"statusCode": 2000,
	"msg": null,
	"traceMsg": "traceId: null",
	"timestamp": 1603433499,
	"signType": null,
	"sign": null,
	"body": {
		"signId": null,
		"shopName": "华联超市",
		"longitude": "120.183406",
		"latitude": "30.263564",
		"hasAfterSale": -1,
		"signTime": null,
		"picUrl": null,
		"visitRecordTaskVOList": [{
			"id": null,
			"subTaskId": "100001",
			"subTaskName": "手抄单",
			"subTaskType": "push_order",
			"requiredFlag": "N",
			"status": "undone"
		}, {
			"id": null,
			"subTaskId": "100003",
			"subTaskName": "盘库存理货",
			"subTaskType": "customize",
			"requiredFlag": "N",
			"status": "undone"
		}, {
			"id": null,
			"subTaskId": "100002",
			"subTaskName": "店铺完善信息",
			"subTaskType": "shop_info",
			"requiredFlag": "Y",
			"status": "undone"
		}, {
			"id": null,
			"subTaskId": "100004",
			"subTaskName": "拜访总结",
			"subTaskType": "customize",
			"requiredFlag": "Y",
			"status": "undone"
		}],
		"leaveTime": null,
		"leavePicUrl": null,
		"shopNewTaskVO": null
	}
}
"""