# NOTE: Generated By HttpRunner v3.1.4
"""
    概要：
        无
    输入参数：
                display	---是否显示 0不显示 1显示
                receptionCategoryId	---前台类目ID
                traId	--商圈ID
    输出参数：
        无
    前置接口：
        无
"""


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCase前台类目展示列表(HttpRunner):

    config = Config("前台类目展示列表").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",
        }).export(*["display", "receptionCategoryId", "receptionCategoryName", "Name", "pageData"])

    teststeps = [
        Step(
            RunRequest("/test_t/mall/receptionCategory/page/list")
            .get(
                "/mall/receptionCategory/page/list"
            )
            .with_params(**{"pageNum": "1", "pageSize": "100", "traId": "11"})
            .with_headers(
                **{
                    "Connection": "keep-alive",
                    "sessionId": "$session",
                    "Sec-Fetch-Dest": "empty",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
                    "systemCode": "yypp",
                    "Accept": "*/*",
                    "Sec-Fetch-Site": "same-origin",
                    "Sec-Fetch-Mode": "cors",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                }
            ).extract()
            .with_jmespath("body.body.pageData[-1].receptionCategoryId", "receptionCategoryId")
            .with_jmespath("body.body.pageData[-1].display", "display")
            .with_jmespath("body.body.pageData[-1].receptionCategoryName", "receptionCategoryName")
            .with_jmespath("body.body.pageData[0].receptionCategoryName", "Name")
            .with_jmespath("body.body.pageData", "pageData")
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.statusCode", 2000)
        ),
    ]


if __name__ == "__main__":
    TestCase前台类目展示列表().test_start()
# {
# 	"statusCode": 2000,
# 	"msg": null,
# 	"traceMsg": "traceId: null",
# 	"timestamp": 1603159472,
# 	"signType": null,
# 	"sign": null,
# 	"body": {
# 		"pageNum": 1,
# 		"pageSize": 10,
# 		"pageCount": 2,
# 		"totalSize": 15,
# 		"pageData": [{
# 			"receptionCategoryId": 1,
# 			"receptionCategoryName": "水饮乳品",
# 			"depth": 0,
# 			"relationType": 0,
# 			"isHasChild": true,
# 			"valid": 1,
# 			"display": 1,
# 			"traId": 11,
# 			"parentId": null,
# 			"sortIndex": null
# 		}