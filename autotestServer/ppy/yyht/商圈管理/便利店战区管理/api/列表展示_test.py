# NOTE: Generated By HttpRunner v3.1.4
"""
    概要：
        便利店战区列表显示
    输入参数：
        "principalName": 负责人名称
        "regionName": 战区名称
        "disable": 是否可用，0-可用，1-不可用
        "businessLine": 业务线, 0-城市站, 1-卫星城
    输出参数：
        "regionId":战区id
    前置接口：
        无
"""


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCase列表展示(HttpRunner):

    config = Config("列表展示").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",
            "principalName": "",
            "regionName": "",
            "disable": "",
            "businessLine": "",
        }).export(*["regionId"])

    teststeps = [
        Step(
            RunRequest("/test_t/pinpin/region/list")
            .post("/pinpin/region/list")
            .with_headers(
                **{
                    "Connection": "keep-alive",
                    "Content-Length": "98",
                    "sessionId": "$session",
                    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36",
                    "systemCode": "yypp",
                    "Content-Type": "application/json",
                    "Accept": "*/*",
                    "Sec-Fetch-Site": "same-origin",
                    "Sec-Fetch-Mode": "cors",
                    "Sec-Fetch-Dest": "empty",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7",
                }
            )
            .with_json(
                {
                    "principalName": "$principalName",
                    "regionName": "$regionName",
                    "disable": "$disable",
                    "businessLine": "$businessLine",
                    "pageNum": 1,
                    "pageSize": 10,
                }
            )
            .extract()
            .with_jmespath("body.body.pageData[0].regionId","regionId")
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.statusCode", 2000)
        ),
    ]


if __name__ == "__main__":
    TestCase列表展示().test_start()
"""
response:
{
	"statusCode": 2000,
	"msg": null,
	"traceMsg": "traceId: null",
	"timestamp": 1602814333,
	"signType": null,
	"sign": null,
	"body": {
		"pageNum": 1,
		"pageSize": 10,
		"pageCount": 2,
		"totalSize": 13,
		"pageData": [{
			"regionId": 95,
			"regionName": "雄鹰战队",
			"regionArea": "105474358",
			"cityCode": "330100",
			"disable": false,
			"createTime": "2020-10-12 23:49:22",
			"updateTime": "2020-10-12 23:49:22",
			"operatorId": 4753,
			"operatorName": "宋静斌",
			"shopRelNum": 2996,
			"bdBdRelNum": 7,
			"shopEventNum": 779,
			"principalName": "王鹤",
			"businessLine": 0
		}, {
			"regionId": 104,
			"regionName": "王牌战队",
			"regionArea": "177497504",
			"cityCode": "330100",
			"disable": false,
			"createTime": "2020-09-10 22:08:24",
			"updateTime": "2020-09-10 22:08:24",
			"operatorId": 4750,
			"operatorName": "王月新",
			"shopRelNum": 2881,
			"bdBdRelNum": 5,
			"shopEventNum": 907,
			"principalName": "王月新",
			"businessLine": 0
		}, {
			"regionId": 116,
			"regionName": "野狼战队",
			"regionArea": "501965430",
			"cityCode": "330100",
			"disable": false,
			"createTime": "2020-09-01 09:08:58",
			"updateTime": "2020-09-01 09:08:58",
			"operatorId": 4135,
			"operatorName": "王鹤",
			"shopRelNum": 2606,
			"bdBdRelNum": 6,
			"shopEventNum": 1049,
			"principalName": "王鹤",
			"businessLine": 0
		}, {
			"regionId": 122,
			"regionName": "火炮战队",
			"regionArea": "411368411",
			"cityCode": "330100",
			"disable": false,
			"createTime": "2020-09-21 11:27:20",
			"updateTime": "2020-09-21 11:27:20",
			"operatorId": 4135,
			"operatorName": "王鹤",
			"shopRelNum": 2164,
			"bdBdRelNum": 5,
			"shopEventNum": 889,
			"principalName": "王鹤",
			"businessLine": 0
		}, {
			"regionId": 128,
			"regionName": "麒麟战队",
			"regionArea": "988092231",
			"cityCode": "330100",
			"disable": false,
			"createTime": "2020-09-29 15:35:33",
			"updateTime": "2020-09-29 15:35:33",
			"operatorId": 3295,
			"operatorName": "喻松海",
			"shopRelNum": 3966,
			"bdBdRelNum": 26,
			"shopEventNum": 1349,
			"principalName": "王月新",
			"businessLine": 0
		}, {
			"regionId": 247,
			"regionName": "荣耀战队",
			"regionArea": "336022219",
			"cityCode": "330100",
			"disable": false,
			"createTime": "2020-01-31 23:16:48",
			"updateTime": "2020-01-31 23:16:48",
			"operatorId": 3487,
			"operatorName": "凌侃",
			"shopRelNum": 806,
			"bdBdRelNum": 0,
			"shopEventNum": 0,
			"principalName": null,
			"businessLine": 0
		}, {
			"regionId": 283,
			"regionName": "巅峰战队",
			"regionArea": "150220618",
			"cityCode": "330100",
			"disable": false,
			"createTime": "2020-09-15 14:36:21",
			"updateTime": "2020-09-15 14:36:21",
			"operatorId": 4750,
			"operatorName": "王月新",
			"shopRelNum": 1720,
			"bdBdRelNum": 6,
			"shopEventNum": 894,
			"principalName": "王月新",
			"businessLine": 0
		}, {
			"regionId": 433,
			"regionName": "临安卫星城",
			"regionArea": "947638323",
			"cityCode": "330100",
			"disable": false,
			"createTime": "2020-09-23 15:06:05",
			"updateTime": "2020-09-27 09:49:25",
			"operatorId": 4714,
			"operatorName": "test",
			"shopRelNum": 38,
			"bdBdRelNum": 8,
			"shopEventNum": 139,
			"principalName": "王鹤",
			"businessLine": 1
		}, {
			"regionId": 436,
			"regionName": "卫星城湖州南浔",
			"regionArea": "659745850",
			"cityCode": "330100",
			"disable": false,
			"createTime": "2020-08-13 09:10:28",
			"updateTime": "2020-10-08 16:28:47",
			"operatorId": 4021,
			"operatorName": "胡飞",
			"shopRelNum": 7,
			"bdBdRelNum": 0,
			"shopEventNum": 0,
			"principalName": null,
			"businessLine": 0
		}, {
			"regionId": 439,
			"regionName": "卫星城湖州吴兴",
			"regionArea": "761789014",
			"cityCode": "330100",
			"disable": false,
			"createTime": "2020-09-16 20:42:02",
			"updateTime": "2020-09-29 11:00:42",
			"operatorId": 4135,
			"operatorName": "王鹤",
			"shopRelNum": 90,
			"bdBdRelNum": 7,
			"shopEventNum": 196,
			"principalName": "王鹤",
			"businessLine": 1
		}]
	}
}
"""