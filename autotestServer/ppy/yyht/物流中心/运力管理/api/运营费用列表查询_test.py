# NOTE: Generated By HttpRunner v3.1.4
"""
    概要：
        运营费用列表查询
    输入参数：
        无
    输出参数：
        "id", 运营费单据号
        "driverId",司机id
        "description",单据名称
        "status",单据状态
        "totalSize" 返回数据条数
    前置接口：
        无
"""


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCase运营费用列表查询(HttpRunner):

    config = Config("运营费用列表查询").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",
            "startDate":"${hapentime(-240)}"+":00",
            "endDate": "${hapentime(24)}"+":00",
            "id": "",
            "statusList": [],
        }).export(*["id","driverId","description","status","totalSize","pageData"])

    teststeps = [
        Step(
            RunRequest("/logis/transBill/operateCost/list")
            .post("/logis/transBill/operateCost/list")
            .with_headers(
                **{
                    "Connection": "keep-alive",
                    "Content-Length": "160",
                    "Accept": "application/json, text/plain, */*",
                    "sessionId": "$session",
                    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
                    "Content-Type": "application/json;charset=UTF-8",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                }
            )
            .with_json(
                {
                    "pageNum": 1,
                    "pageSize": 5000,
                    "startDate": "$startDate",
                    "endDate": "$endDate",
                    "driverTypeList": [],
                    "statusList": "$statusList",
                    "id": "$id",
                    "valid": 1,
                    "cityCode": "330100",
                }
            ).extract()
                .with_jmespath("body.body.pageData[-1].id","id")
                .with_jmespath("body.body.pageData[-1].driverId", "driverId")
                .with_jmespath("body.body.pageData[-1].description", "description")
                .with_jmespath("body.body.pageData[-1].status", "status")
                .with_jmespath("body.body.totalSize", "totalSize")
                .with_jmespath("body.body.pageData", "pageData")
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.statusCode", 2000)
        ),
    ]


if __name__ == "__main__":
    TestCase运营费用列表查询().test_start()

"""
{
	"statusCode": 2000,
	"msg": null,
	"traceMsg": "traceId: 1603076910123",
	"timestamp": 1603076910,
	"signType": null,
	"sign": null,
	"body": {
		"pageNum": 1,
		"pageSize": 500,
		"pageCount": 1,
		"totalSize": 9,
		"pageData": [{
			"id": "1190367091147421027",
			"driverId": "174",
			"driverName": "拼便宜测试号",
			"driverPhone": "15605811626",
			"vehicleName": "金杯",
			"driverType": 40,
			"type": "021",
			"typeValue": "罚款",
			"amount": -13247,
			"status": 5,
			"valid": 1,
			"description": "test.",
			"remark": "-132.48",
			"createTime": "2020-10-09 17:45:09",
			"updateTime": "2020-10-19 11:08:30"
		}, {
			"id": "1190367971144901704",
			"driverId": "68",
			"driverName": "周兰涛1111",
			"driverPhone": "13738113393",
			"vehicleName": "金杯",
			"driverType": 1,
			"type": "020",
			"typeValue": "运营费",
			"amount": -13247,
			"status": 5,
			"valid": 1,
			"description": "-132.48",
			"remark": "-132.48",
			"createTime": "2020-10-09 17:46:37",
			"updateTime": "2020-10-09 17:46:38"
		}, {
			"id": "1192072841140181142",
			"driverId": "174",
			"driverName": "拼便宜测试号",
			"driverPhone": "15605811626",
			"vehicleName": "金杯",
			"driverType": 40,
			"type": "021",
			"typeValue": "罚款",
			"amount": 13248,
			"status": 5,
			"valid": 1,
			"description": "33",
			"remark": "33",
			"createTime": "2020-10-11 17:08:04",
			"updateTime": "2020-10-11 17:08:04"
		}, {
			"id": "1198735221142991043",
			"driverId": "68",
			"driverName": "周兰涛1111",
			"driverPhone": "13738113393",
			"vehicleName": "金杯",
			"driverType": 1,
			"type": "020",
			"typeValue": "运营费",
			"amount": 11100,
			"status": 5,
			"valid": 1,
			"description": "1111",
			"remark": "111",
			"createTime": "2020-10-19 10:12:02",
			"updateTime": "2020-10-19 10:12:02"
		}, {
			"id": "1198735571143311803",
			"driverId": "68",
			"driverName": "周兰涛1111",
			"driverPhone": "13738113393",
			"vehicleName": "金杯",
			"driverType": 1,
			"type": "020",
			"typeValue": "运营费",
			"amount": 12300,
			"status": 5,
			"valid": 1,
			"description": "23231",
			"remark": "123",
			"createTime": "2020-10-19 10:12:37",
			"updateTime": "2020-10-19 10:12:37"
		}, {
			"id": "1198736321143731450",
			"driverId": "68",
			"driverName": "周兰涛1111",
			"driverPhone": "13738113393",
			"vehicleName": "金杯",
			"driverType": 1,
			"type": "020",
			"typeValue": "运营费",
			"amount": 100,
			"status": 5,
			"valid": 1,
			"description": "12",
			"remark": "1",
			"createTime": "2020-10-19 10:13:52",
			"updateTime": "2020-10-19 10:58:02"
		}, {
			"id": "1198736401145811111",
			"driverId": "68",
			"driverName": "周兰涛1111",
			"driverPhone": "13738113393",
			"vehicleName": "金杯",
			"driverType": 1,
			"type": "020",
			"typeValue": "运营费",
			"amount": 100,
			"status": 5,
			"valid": 1,
			"description": "1",
			"remark": "1",
			"createTime": "2020-10-19 10:14:00",
			"updateTime": "2020-10-19 10:14:01"
		}, {
			"id": "1198741091140351807",
			"driverId": "68",
			"driverName": "周兰涛1111",
			"driverPhone": "13738113393",
			"vehicleName": "金杯",
			"driverType": 1,
			"type": "020",
			"typeValue": "运营费",
			"amount": 100,
			"status": 10,
			"valid": 1,
			"description": "nice",
			"remark": "1",
			"createTime": "2020-10-19 10:21:49",
			"updateTime": "2020-10-19 10:55:18"
		}, {
			"id": "1198768691145811566",
			"driverId": "68",
			"driverName": "周兰涛1111",
			"driverPhone": "13738113393",
			"vehicleName": "金杯",
			"driverType": 1,
			"type": "020",
			"typeValue": "运营费",
			"amount": 100,
			"status": 5,
			"valid": 1,
			"description": "1",
			"remark": "1",
			"createTime": "2020-10-19 11:07:49",
			"updateTime": "2020-10-19 11:07:50"
		}]
	}
}
"""
