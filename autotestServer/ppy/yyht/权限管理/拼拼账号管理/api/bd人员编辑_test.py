# NOTE: Generated By HttpRunner v3.1.4
"""
    概要：
        bd人员编辑
    输入参数：
        "id": bd id
        "user": 运营人员姓名,
        "businessLine": 业务线, 0-城市站, 1-卫星城
        "position": 职位-BD,BDM,CM,城市总,省总,总监,其他
        "department": 部门-市场,采购,技术,产品,物流,其他
        "cityCode": 城市编码
        "sex": 性别,0-男,1-女
        "phone": 运营人员手机号
        "leaderName": 上级姓名
        "leaderId": 上级id
    输出参数：
        无
    前置接口：
        无
"""


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
import env


class TestCaseBd人员编辑(HttpRunner):

    config = Config("Bd人员编辑").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",
            "id": 2,
            "user": "王子铭",
            "phone": "13758178214",
            "department": "市场",
            "position": "BD",
            "sex": "false",
            "businessLine": "0",
            "cityCode": env.cityCode,
            "leaderName": "邓虹雨",
            "leaderId": 619,
        })

    teststeps = [
        Step(
            RunRequest("/test_t/pinpin/operator/edit")
            .post("/pinpin/operator/edit")
            .with_headers(
                **{
                    "Connection": "keep-alive",
                    "Content-Length": "180",
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
                {
                    "id": "$id",
                    "user": "$user",
                    "phone": "$phone",
                    "department": "$department",
                    "position": "$position",
                    "sex": "$sex",
                    "businessLine": "$businessLine",
                    "cityCode": "330100",
                    "leaderName": "$leaderName",
                    "leaderId": "$leaderId",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.statusCode", 2000)
            .assert_equal("body.body", True)
        ),
    ]


if __name__ == "__main__":
    TestCaseBd人员编辑().test_start()
