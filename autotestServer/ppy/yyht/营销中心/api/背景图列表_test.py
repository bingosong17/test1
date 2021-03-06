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


class TestCase背景图列表(HttpRunner):

    config = Config("背景图列表").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",

        }).export(*["backgroundImageName", "backgroundImageId"])

    teststeps = [
        Step(
            RunRequest("/mall/backgroundImage")
            .get("/mall/backgroundImage")
            .with_params(
                **{
                    "traId": "",
                    "backgroundImageName": "",
                    "statusArray": "0,1,2,3,4",
                    "pageSize": "10",
                    "pageNum": "1",
                }
            )
            .with_headers(
                **{
                    "Connection": "keep-alive",
                    "Accept": "application/json, text/plain, */*",
                    "Sec-Fetch-Dest": "empty",
                    "sessionId": "$session",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
                    "Sec-Fetch-Site": "same-site",
                    "Sec-Fetch-Mode": "cors",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                }
            ).extract()
            .with_jmespath("body.body.pageData[0].backgroundImageName", "backgroundImageName")
            .with_jmespath("body.body.pageData[0].backgroundImageId", "backgroundImageId")
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.statusCode", 2000)
        ),
    ]


if __name__ == "__main__":
    TestCase背景图列表().test_start()
'''{
	"statusCode": 2000,
	"msg": null,
	"traceMsg": "traceId: null",
	"timestamp": 1600590193,
	"signType": null,
	"sign": null,
	"body": {
		"pageNum": 1,
		"pageSize": 10,
		"pageCount": 3,
		"totalSize": 24,
		"pageData": [{
			"backgroundImageId": 94,
			"status": 0,
			"cityCode": "330100",
			"startTime": "2020-09-21 00:00:00",
			"endTime": "2020-10-31 23:59:59",
			"backgroundImageName": "背景图_郑小和",
			"traNames": "滨江-商圈",
			"picUrl": "http://images.alpha.pinpianyi.cn/images/common/c2b52ecdf1b44d4e9b6365e5af842745.png",
			"searchPicUrl": "http://images.alpha.pinpianyi.cn/images/common/1c1d50b5a42a4128bd9168f4a3b67173.png",
			"updateUserName": "郑和",
			"updateTime": "2020-09-20 16:22:28",
			"remark": null,
			"statusText": "未生效"
		}, {
			"backgroundImageId": 86,
			"status": 2,
			"cityCode": "330100",
			"startTime": "2020-08-17 21:08:00",
			"endTime": "2020-08-18 23:59:59",
			"backgroundImageName": "818燃物节",
			"traNames": "滨江-商圈,城北西湖-商圈,下沙九堡-商圈,乔司临平-商圈,拼便宜-便利店,萧山-商圈",
			"picUrl": "https://images.pinpianyi.com/images/common/855b5e7e35584ef9b1c14c3a463a63f3.png",
			"searchPicUrl": "https://images.pinpianyi.com/images/common/714e74826a37486e9ef0cb217715e948.png",
			"updateUserName": "崔晓洁",
			"updateTime": "2020-08-17 21:07:26",
			"remark": null,
			"statusText": "已结束"
		}'''