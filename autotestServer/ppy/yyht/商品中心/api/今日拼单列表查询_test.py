# NOTE: Generated By HttpRunner v3.1.3
"""
    概要：
        根据商品id查询获得商品的a,b品类
    输入参数：
        无
    输出参数：
        无
    前置接口：
        无
"""


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase



class TestCase今日拼单列表查询(HttpRunner):

    config = Config("今日拼单列表查询").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",
            "traId": 11,
            "goodsId": "18508",
        })

    teststeps = [
        Step(
            RunRequest("/alpha_t/mall/sell/list")
            .post("/mall/sell/list")
            .with_headers(
                **{
                    "Connection": "keep-alive",
                    "Content-Length": "169",
                    "sessionId": "$session",
                    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36",
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
                    "traId": "$traId",
                    "sellOut": "",
                    "statusList": [],
                    "tabLabelId": "",
                    "queryType": "goodsId",
                    "queryValue": "$goodsId",
                    "pageNum": 1,
                    "pageSize": 10,
                    "goodsType": "1",
                    "backstageCategoryId": None,
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.statusCode", 2000)
        ),
    ]


if __name__ == "__main__":
    TestCase今日拼单列表查询().test_start()
"""
response:

"""