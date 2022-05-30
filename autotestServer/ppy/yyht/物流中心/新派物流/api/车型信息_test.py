# NOTE: Generated By HttpRunner v3.1.4
"""
    概要：
        根据城市获取物流区域
    输入参数：
        无
    输出参数：
        无
    前置接口：
        无
"""


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCase车型信息(HttpRunner):

    config = Config("车型信息").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",
        })

    teststeps = [
        Step(
            RunRequest("/logis/api/mng/vehicle/info")
            .post("/logis/api/mng/vehicle/info")
            .with_headers(
                **{
                    "sessionId": "$session",
                    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36",
                    "Content-Type": "application/json",
                    "Sec-Fetch-Site": "same-site",
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
    TestCase车型信息().test_start()
"""
response:
body     : {
    "statusCode": 2000,
    "msg": null,
    "traceMsg": "traceId: 1605093752145",
    "timestamp": 1605093752,
    "signType": null,
    "sign": null,
    "body": [
        {
            "id": "11",
            "value": "小面包",
            "status": null,
            "load": 1000,
            "vehicleVolume": 3228428
        },
        {
            "id": "12",
            "value": "金杯",
            "status": null,
            "load": 2000,
            "vehicleVolume": 6456857
        },
        {
            "id": "13",
            "value": "中面",
            "status": null,
            "load": 1500,
            "vehicleVolume": 4304571
        },
        {
            "id": "14",
            "value": "高顶金杯",
            "status": null,
            "load": 2200,
            "vehicleVolume": 6456857
        },
        {
            "id": "15",
            "value": "全顺",
            "status": null,
            "load": 2500,
            "vehicleVolume": 6456857
        },
        {
            "id": "16",
            "value": "依维柯",
            "status": null,
            "load": 2200,
            "vehicleVolume": 6456857
        },
        {
            "id": "17",
            "value": "4.2箱货",
            "status": null,
            "load": 4000,
            "vehicleVolume": 10000000
        },
        {
            "id": "21",
            "value": "B类小面包",
            "status": null,
            "load": 1000,
            "vehicleVolume": 3228428
        },
        {
            "id": "22",
            "value": "B类金杯",
            "status": null,
            "load": 2000,
            "vehicleVolume": 6456857
        },
        {
            "id": "23",
            "value": "B类中面",
            "status": null,
            "load": 1500,
            "vehicleVolume": 4304571
        }
    ]
}
"""