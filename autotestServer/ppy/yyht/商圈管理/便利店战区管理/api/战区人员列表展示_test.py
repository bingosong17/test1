# NOTE: Generated By HttpRunner v3.1.4
"""
    概要：
        战区人员列表展示
    输入参数：
        "countEnabled": 是否开启行数统计,默认:true
        "regionId": 战区id
    输出参数：
        无
    前置接口：
        无
"""


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCase战区人员列表展示(HttpRunner):

    config = Config("战区人员列表展示").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",
            "countEnabled": True,
            "regionId": 498
        })

    teststeps = [
        Step(
            RunRequest("/test_t/pinpin/regionBdRel/selectRegionBdList")
            .post(
                "/pinpin/regionBdRel/selectRegionBdList"
            )
            .with_headers(
                **{
                    "Connection": "keep-alive",
                    "Content-Length": "62",
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
                {"countEnabled": "$countEnabled", "pageNum": 1, "pageSize": 10, "regionId": "$regionId"}
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.statusCode", 2000)
        ),
    ]


if __name__ == "__main__":
    TestCase战区人员列表展示().test_start()
"""
response:
{
	"statusCode": 2000,
	"msg": null,
	"traceMsg": "traceId: null",
	"timestamp": 1602835241,
	"signType": null,
	"sign": null,
	"body": {
		"pageNum": 1,
		"pageSize": 10,
		"pageCount": 1,
		"totalSize": 1,
		"pageData": [{
			"relId": 4777,
			"regionId": 498,
			"bdId": 1,
			"bdName": "测试是的",
			"bdPosition": "BD",
			"maxCapacity": 100,
			"operatorId": 4753,
			"operatorName": "宋静斌",
			"disable": null,
			"createTime": "2020-10-16 13:49:17",
			"updateTime": "2020-10-16 16:00:41",
			"capacity": 0,
			"businessLine": 0
		}]
	}
}
"""