# NOTE: Generated By HttpRunner v3.1.4
"""
    概要：
        无
    输入参数：
        无
    输出参数：
        无
    前置接口：
        无
"""


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCase司机钱包流水结算单详情(HttpRunner):

    config = Config("司机钱包流水结算单详情").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",
            "settlementCode": "1015925068042200099"
        }).export(*["settlementCode"])

    teststeps = [
        Step(
            RunRequest("/ppy-finance-settle-api/logistics/settlement/detail")
            .post(
                "https://webapi.test.pinpianyi.cn/ppy-finance-settle-api/logistics/settlement/detail"
            )
            .with_headers(
                **{
                    "Connection": "keep-alive",
                    "Content-Length": "66",
                    "Accept": "application/json, text/plain, */*",
                    "sessionId": "$session",
                    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
                    "Content-Type": "application/json;charset=UTF-8",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                }
            )
            .with_json(
                {"settlementType": "driver", "settlementCode": "$settlementCode"}
            ).extract().with_jmespath("body.body.logisticsSettlementInfo.settlementCode", "settlementCode")
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.statusCode", 2000)
        ),
    ]


if __name__ == "__main__":
    TestCase司机钱包流水结算单详情().test_start()
"""
{
	"statusCode": 2000,
	"msg": null,
	"traceMsg": "traceId: 1603179285889",
	"timestamp": 1603179285,
	"signType": null,
	"sign": null,
	"body": {
		"logisticsSettlementInfo": {
			"settlementCode": "1015925068042200099",
			"settlementType": "driver",
			"settlerName": "周兰涛",
			"settlerPhone": "13738113393",
			"driverType": 1,
			"settlementPeriodStartTime": "2020-06-01",
			"settlementPeriodEndTime": "2020-06-15",
			"settlementTime": "2020-06-30"
		},
		"logisticsSettlementRemarkList": null,
		"logisticsSettlementAttachmentList": null,
		"logisticsFeeInfoList": [{
			"id": "132196",
			"subBizCode": "115672",
			"bizCode": "33010020200601102555168",
			"driverId": null,
			"driverName": "周兰涛",
			"driverType": null,
			"feeChannel": "trans",
			"feeAmount": 32456,
			"feeType": "010",
			"feeTypeName": "运费-基础费",
			"feeName": "运费费用",
			"feeDesc": null,
			"feeEvidenceImgUrl": null,
			"feeEvidenceImgUrlList": [],
			"settleStatus": 20,
			"generateTime": "2020-06-02 13:04:42",
			"createTime": "2020-06-05 16:49:04"
		}, {
			"id": "132490",
			"subBizCode": "117289",
			"bizCode": "33010020200602102601168",
			"driverId": null,
			"driverName": "周兰涛",
			"driverType": null,
			"feeChannel": "trans",
			"feeAmount": 31545,
			"feeType": "010",
			"feeTypeName": "运费-基础费",
			"feeName": "运费费用",
			"feeDesc": null,
			"feeEvidenceImgUrl": null,
			"feeEvidenceImgUrlList": [],
			"settleStatus": 20,
			"generateTime": "2020-06-03 13:08:23",
			"createTime": "2020-06-05 16:49:04"
		}, {
			"id": "132757",
			"subBizCode": "118546",
			"bizCode": "33010020200603102634068",
			"driverId": null,
			"driverName": "周兰涛",
			"driverType": null,
			"feeChannel": "trans",
			"feeAmount": 31027,
			"feeType": "010",
			"feeTypeName": "运费-基础费",
			"feeName": "运费费用",
			"feeDesc": null,
			"feeEvidenceImgUrl": null,
			"feeEvidenceImgUrlList": [],
			"settleStatus": 20,
			"generateTime": "2020-06-04 12:18:50",
			"createTime": "2020-06-05 16:49:04"
		}, {
			"id": "135619",
			"subBizCode": "119695",
			"bizCode": "33010020200604102686868",
			"driverId": null,
			"driverName": "周兰涛",
			"driverType": null,
			"feeChannel": "trans",
			"feeAmount": 30224,
			"feeType": "010",
			"feeTypeName": "运费-基础费",
			"feeName": "运费费用",
			"feeDesc": null,
			"feeEvidenceImgUrl": null,
			"feeEvidenceImgUrlList": [],
			"settleStatus": 20,
			"generateTime": "2020-06-05 12:30:20",
			"createTime": "2020-06-08 15:20:48"
		}, {
			"id": "135913",
			"subBizCode": "121141",
			"bizCode": "33010020200605102757668",
			"driverId": null,
			"driverName": "周兰涛",
			"driverType": null,
			"feeChannel": "trans",
			"feeAmount": 31278,
			"feeType": "010",
			"feeTypeName": "运费-基础费",
			"feeName": "运费费用",
			"feeDesc": null,
			"feeEvidenceImgUrl": null,
			"feeEvidenceImgUrlList": [],
			"settleStatus": 20,
			"generateTime": "2020-06-06 13:22:56",
			"createTime": "2020-06-08 15:20:48"
		}, {
			"id": "136117",
			"subBizCode": "122446",
			"bizCode": "33010020200606102819468",
			"driverId": null,
			"driverName": "周兰涛",
			"driverType": null,
			"feeChannel": "trans",
			"feeAmount": 26160,
			"feeType": "010",
			"feeTypeName": "运费-基础费",
			"feeName": "运费费用",
			"feeDesc": null,
			"feeEvidenceImgUrl": null,
			"feeEvidenceImgUrlList": [],
			"settleStatus": 20,
			"generateTime": "2020-06-07 11:58:49",
			"createTime": "2020-06-08 15:20:48"
		}, {
			"id": "140455",
			"subBizCode": "125269",
			"bizCode": "33010020200608102892868",
			"driverId": null,
			"driverName": "周兰涛",
			"driverType": null,
			"feeChannel": "trans",
			"feeAmount": 32906,
			"feeType": "010",
			"feeTypeName": "运费-基础费",
			"feeName": "运费费用",
			"feeDesc": null,
			"feeEvidenceImgUrl": null,
			"feeEvidenceImgUrlList": [],
			"settleStatus": 20,
			"generateTime": "2020-06-09 14:27:24",
			"createTime": "2020-06-11 16:08:10"
		}, {
			"id": "140662",
			"subBizCode": "126283",
			"bizCode": "33010020200609102958568",
			"driverId": null,
			"driverName": "周兰涛",
			"driverType": null,
			"feeChannel": "trans",
			"feeAmount": 31655,
			"feeType": "010",
			"feeTypeName": "运费-基础费",
			"feeName": "运费费用",
			"feeDesc": null,
			"feeEvidenceImgUrl": null,
			"feeEvidenceImgUrlList": [],
			"settleStatus": 20,
			"generateTime": "2020-06-10 13:58:05",
			"createTime": "2020-06-11 16:08:10"
		}, {
			"id": "142822",
			"subBizCode": "127480",
			"bizCode": "33010020200610103007868",
			"driverId": null,
			"driverName": "周兰涛",
			"driverType": null,
			"feeChannel": "trans",
			"feeAmount": 31934,
			"feeType": "010",
			"feeTypeName": "运费-基础费",
			"feeName": "运费费用",
			"feeDesc": null,
			"feeEvidenceImgUrl": null,
			"feeEvidenceImgUrlList": [],
			"settleStatus": 20,
			"generateTime": "2020-06-11 13:19:45",
			"createTime": "2020-06-14 15:39:05"
		}, {
			"id": "143050",
			"subBizCode": "128731",
			"bizCode": "33010020200611103098568",
			"driverId": null,
			"driverName": "周兰涛",
			"driverType": null,
			"feeChannel": "trans",
			"feeAmount": 30698,
			"feeType": "010",
			"feeTypeName": "运费-基础费",
			"feeName": "运费费用",
			"feeDesc": null,
			"feeEvidenceImgUrl": null,
			"feeEvidenceImgUrlList": [],
			"settleStatus": 20,
			"generateTime": "2020-06-12 13:45:59",
			"createTime": "2020-06-14 15:39:05"
		}, {
			"id": "143197",
			"subBizCode": "129505",
			"bizCode": "33010020200612103133068",
			"driverId": null,
			"driverName": "周兰涛",
			"driverType": null,
			"feeChannel": "trans",
			"feeAmount": 30889,
			"feeType": "010",
			"feeTypeName": "运费-基础费",
			"feeName": "运费费用",
			"feeDesc": null,
			"feeEvidenceImgUrl": null,
			"feeEvidenceImgUrlList": [],
			"settleStatus": 20,
			"generateTime": "2020-06-13 12:20:34",
			"createTime": "2020-06-14 15:39:05"
		}, {
			"id": "146137",
			"subBizCode": "131035",
			"bizCode": "33010020200613103174768",
			"driverId": null,
			"driverName": "周兰涛",
			"driverType": null,
			"feeChannel": "trans",
			"feeAmount": 32013,
			"feeType": "010",
			"feeTypeName": "运费-基础费",
			"feeName": "运费费用",
			"feeDesc": null,
			"feeEvidenceImgUrl": null,
			"feeEvidenceImgUrlList": [],
			"settleStatus": 20,
			"generateTime": "2020-06-14 12:17:16",
			"createTime": "2020-06-16 20:39:50"
		}],
		"operationLogList": [{
			"operatorName": "system",
			"operationContext": "司机自动结算,付款到司机钱包",
			"createTime": "2020-06-30 03:00:04"
		}, {
			"operatorName": "孙益锋",
			"operationContext": "钉钉审批通过",
			"createTime": "2020-06-24 17:18:16"
		}, {
			"operatorName": "祝邦东",
			"operationContext": "发起结算单审批批次,批次号[1015926163452200075]",
			"createTime": "2020-06-20 09:25:45"
		}, {
			"operatorName": "system",
			"operationContext": "自动生成结算单",
			"createTime": "2020-06-19 03:00:04"
		}],
		"feeTypetatisticsMap": {
			"运费-基础费": 372785,
			"合计": 372785
		}
	}
}
"""