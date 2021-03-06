# NOTE: Generated By HttpRunner v3.1.4
"""
   概要：
        添加店铺到拜访计划
    输入参数：
        “shopId”：店铺id
        "type": 客户类型(1合作店铺2潜在店铺3合作供应商4潜在供应商)
        "visitTime": 拜访时间
    输出参数：
        无
    前置接口：
        用户登录；获取公、私海店铺列表
"""


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCase添加拜访计划(HttpRunner):

    config = Config("添加拜访计划").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "ppApp",
            "phone": "15757113586",
            "session": "${getSession($business,$phone)}",
            "shopId": "",
            "type": "1",
            "visitTime": "${hapentime(0,1)}"
        }).export(*["拜访Id"])

    teststeps = [
        Step(
            RunRequest("/ppy-pinpin/visit/saveVisit")
            .post("/visit/saveVisit")
            .with_headers(
                **{
                    "sessionId": "$session",
                    "serviceName": "NEW-PP",
                    "Content-Length": "54",
                    "Connection": "Keep-Alive",
                    "Accept-Encoding": "gzip",
                    "User-Agent": "okhttp/3.12.1",
                    "Content-Type": "application/json",
                    "Accept-Language": "zh-CN,zh;q=0.8",
                    "deviceId": "3834e10b-cb2a-34c6-85f2-2ae3b365eb14",
                }
            )
            .with_json({"shopId": "$shopId", "type": "$type", "visitTime": "$visitTime"})
            .extract()
            .with_jmespath("body.body", "拜访Id")
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.statusCode", 2000)
        ),
    ]


if __name__ == "__main__":
    TestCase添加拜访计划().test_start()
"""
response:
{
{
	"statusCode": 2000,
	"msg": null,
	"traceMsg": "traceId: null",
	"timestamp": 1600312686,
	"signType": null,
	"sign": null,
	"body": 3044785
}
}
"""