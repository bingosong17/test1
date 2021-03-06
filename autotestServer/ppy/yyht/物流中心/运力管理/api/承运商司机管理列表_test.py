# NOTE: Generated By HttpRunner v3.1.4
"""
    概要：
        承运商司机管理列表
    输入参数：
        driverName  司机名称
    输出参数：
        name    司机名称
        id      司机id
    前置接口：
        无
"""


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCase承运商司机管理列表(HttpRunner):

    config = Config("承运商司机管理列表").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",
            "driverName": "",
            "status": "",
            "carrierId": "",
            "vehicleType": "",
        }).export(*["name","id"])

    teststeps = [
        Step(
            RunRequest("/logis/api/mng/carriers/queryCarrierUnderlingDriverList")
            .post(
                "/logis/api/mng/carriers/queryCarrierUnderlingDriverList"
            )
            .with_headers(
                **{
                    "Connection": "keep-alive",
                    "Content-Length": "68",
                    "Accept": "application/json, text/plain, */*",
                    "sessionId": "$session",
                    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
                    "Content-Type": "application/x-www-form-urlencoded",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                }
            )
            .with_data(
                {
                    "carrierId": "$carrierId",
                    "driverName": "$driverName",
                    "vehicleType": "$vehicleType",
                    "status": "$status",
                    "pageNo": "1",
                    "pageSize": "15",
                }
            ).extract().with_jmespath("body.body.pageData[0].name","name")
                .with_jmespath("body.body.pageData[0].id", "id")
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.statusCode", 2000)
        ),
    ]


if __name__ == "__main__":
    TestCase承运商司机管理列表().test_start()
