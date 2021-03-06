# NOTE: Generated By HttpRunner v3.1.4
"""
    概要：
        爆品列表
    输入参数：
        queryType  状态 1 全部
    输出参数：
        无
    前置接口：
        无
"""


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCase爆品列表(HttpRunner):

    config = Config("爆品列表").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",
            "status": "0",
        }).export(*["goodsId", "id", "pageData"])

    teststeps = [
        Step(
            RunRequest("/test_t/mall/promo/list")
            .post("/mall/promo/list")
            .with_headers(
                **{
                    "Connection": "keep-alive",
                    "Content-Length": "89",
                    "sessionId": "$session",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
                    "systemCode": "yypp",
                    "Content-Type": "application/json",
                    "Accept": "*/*",
                    "Sec-Fetch-Site": "same-origin",
                    "Sec-Fetch-Mode": "cors",
                    "Sec-Fetch-Dest": "empty",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                }
            )
            .with_json(
                {
                    "pageNum": 1,
                    "pageSize": 10,
                    "traId": 11,
                    "status": "$status",
                    "queryType": 1,
                    "redPacketAvailable": "",
                }
            ).extract()
            .with_jmespath("body.body.pageData[0].goodsId", "goodsId")
            .with_jmespath("body.body.pageData[0].id", "id")
            .with_jmespath("body.body.pageData", "pageData")
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.statusCode", 2000)
        ),
    ]


if __name__ == "__main__":
    TestCase爆品列表().test_start()
# {
# 	"statusCode": 2000,
# 	"msg": null,
# 	"traceMsg": "traceId: null",
# 	"timestamp": 1603870121,
# 	"signType": null,
# 	"sign": null,
# 	"body": {
# 		"pageNum": 1,
# 		"pageSize": 10,
# 		"pageCount": 8078,
# 		"totalSize": 80773,
# 		"pageData": [{
# 			"goodsId": 58,
# 			"goodsName": "康师傅茉莉蜜茶1L*12瓶/箱",
# 			"id": 3220171,
# 			"startTime": "2020-11-10 00:00:00",
# 			"endTime": "2021-09-11 00:00:00",
# 			"orderPayNum": 0,
# 			"totalPayNum": 0,
# 			"initStock": 5,
# 			"redPacketAvailable": 0,
# 			"promotionsType": 0,
# 			"status": 0,
# 			"statusName": "未生效",
# 			"sellOut": 0,
# 			"traId": 11,
# 			"traName": "滨江-商圈",
# 			"specification": null,
# 			"promotionsPrice": 3500,
# 			"zeroPrice": null,
# 			"minNum": null,
# 			"maxNum": null,
# 			"batchNumber": null,
# 			"modifyUser": null,
# 			"modifyUserName": null,
# 			"createUser": 5015,
# 			"createUserName": "胡超",
# 			"createTime": "2020-10-28 15:25:55",
# 			"modifyTime": "2020-10-28 15:25:54"
# 		}
