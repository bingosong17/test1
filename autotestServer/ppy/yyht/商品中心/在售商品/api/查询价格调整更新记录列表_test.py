# NOTE: Generated By HttpRunner v3.1.4
"""
    概要：
        查询价格调整更新记录列表
    输入参数：
        "processingState":处理状态，1-待确认，2-已完成
        "checkStatus":更新状态，0-系统检验中，1-更新完成
        "goodsId": 商品id
        "adjustType":更新类型,01-拼单商品上架,02-拼单商品管理,03-导入拼单商品,04-导入拼单商品,05-导入拼单商品,06-导入拼单商品,07-导入拼单商品
    输出参数：
        无
    前置接口：
        无
"""


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCase查询价格调整更新记录列表(HttpRunner):

    config = Config("查询价格调整更新记录列表").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",
            "processingState": "",
            "checkStatus": "",
            "goodsId": "",
            "adjustType": ""
        })

    teststeps = [
        Step(
            RunRequest("/test_t/mall/priceAdjust/record")
            .get("/mall/priceAdjust/record")
            .with_params(
                **{
                    "pageNum": "1",
                    "pageSize": "10",
                    "processingState": "$processingState",
                    "checkStatus": "$checkStatus",
                    "goodsId": "$goodsId",
                    "adjustType": "$adjustType"
                }
            )
            .with_headers(
                **{
                    "Connection": "keep-alive",
                    "sessionId": "$session",
                    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36",
                    "systemCode": "yypp",
                    "Accept": "*/*",
                    "Sec-Fetch-Site": "same-origin",
                    "Sec-Fetch-Mode": "cors",
                    "Sec-Fetch-Dest": "empty",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.statusCode", 2000)
        ),
    ]


if __name__ == "__main__":
    TestCase查询价格调整更新记录列表().test_start()
