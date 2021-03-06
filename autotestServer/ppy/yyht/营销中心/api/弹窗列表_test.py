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


class TestCase弹窗列表(HttpRunner):

    config = Config("弹窗列表").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",
        }).export(*["windowName"])

    teststeps = [
        Step(
            RunRequest("/mall/shopping/window/list")
            .get("/mall/shopping/window/list")
            .with_params(
                **{
                    "statusArray": "0",
                    "pageNum": "1",
                    "pageSize": "10",
                    "windowName": "",
                    "traId": "",
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
            .with_jmespath("body.body.pageData[0].windowName", "windowName")
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.statusCode", 2000)
        ),
    ]


if __name__ == "__main__":
    TestCase弹窗列表().test_start()
# {
# 	"statusCode": 2000,
# 	"msg": null,
# 	"traceMsg": "traceId: null",
# 	"timestamp": 1604556954,
# 	"signType": null,
# 	"sign": null,
# 	"body": {
# 		"pageNum": 1,
# 		"pageSize": 10,
# 		"pageCount": 1,
# 		"totalSize": 1,
# 		"pageData": [{
# 			"windowId": 3129,
# 			"windowName": "弹窗_郑小和",
# 			"actionText": "我的钱包",
# 			"picUrl": "http://images.alpha.pinpianyi.cn/images/common/cd5e91d4352b4521bde18bdb47321a86.png",
# 			"pushCount": 506,
# 			"popCount": null,
# 			"clickCount": null,
# 			"traNames": "滨江-商圈",
# 			"startTime": "2020-11-05 15:13:00",
# 			"endTime": "2020-11-09 18:13:00",
# 			"status": 0,
# 			"modifyUserName": "胡超",
# 			"modifyTime": "2020-11-05 14:13:30",
# 			"remark": null,
# 			"sortIndex": null
# 		}]
# 	}