# NOTE: Generated By HttpRunner v3.1.4
"""
    概要：
        店铺签到分页列表查询
    输入参数：
        "startTime": 开始时间
        "endTime": 结束时间
        "operatorIds": Bd id列表
        "signRecordResultTypes": 签到类型(签到结果类型valid:有离店打卡时间的有效拜访,lost_follow-up:失访上报数据,not_leave:没有离店打卡记录)
    输出参数：
        无
    前置接口：
        无
"""


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCase店铺签到分页列表查询(HttpRunner):

    config = Config("店铺签到分页列表查询").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "ppApp",
            "phone": "15757113586",
            "session": "${getSession($business,$phone)}",
            "startTime": "2020-11-10",
            "endTime": "2020-11-10",
            "operatorIds": ["161"],
            "signRecordResultTypes": ["valid"],
        }).export(*["SignShopPageData"])

    teststeps = [
        Step(
            RunRequest("/ppy-pinpin/sign/pageSignShopList")
            .post("/sign/pageSignShopList")
            .with_headers(
                **{
                    "Accept": "*/*",
                    "channel": "app",
                    "appname": "",
                    "Accept-Language": "zh-cn",
                    "Accept-Encoding": "gzip, deflate",
                    "platform": "ios",
                    "Content-Type": "application/json",
                    "sessionid": "$session",
                    "deviceid": "1F8ED797-D036-4BA3-BEAA-A176B0E08BD6",
                    "Content-Length": "97",
                    "User-Agent": "Pinpin/3.7.0.20201023215334 CFNetwork/889.9 Darwin/17.2.0",
                    "appchannel": "appstore",
                    "servicename": "NEW-PP",
                    "Connection": "keep-alive",
                }
            )
            .with_json(
                {
                    "pageNum": 1,
                    "pageSize": 100,
                    "startTime": "$startTime",
                    "endTime": "$endTime",
                    "operatorIds": "$operatorIds",
                    "signRecordResultTypes": "$signRecordResultTypes",
                }
            ).extract()
            .with_jmespath("body.body.pageData", "SignShopPageData")
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.statusCode", 2000)
        ),
    ]


if __name__ == "__main__":
    TestCase店铺签到分页列表查询().test_start()
"""
response:
body     : {
    "statusCode": 2000,
    "msg": null,
    "traceMsg": "traceId: null",
    "timestamp": 1603956231,
    "signType": null,
    "sign": null,
    "body": {
        "pageNum": 1,
        "pageSize": 10,
        "pageCount": 1,
        "totalSize": 6,
        "pageData": [
            {
                "signId": 3633609,
                "signPicUrl": "https://images.alpha.pinpianyi.cn/images/face/yypp/93c4ff1d7a7f4065832969df33c0dbc0.png",
                "shopId": 1339,
                "shopName": "宜宝便利店",
                "signTime": "2020-10-28 16:57",
                "leaveTime": 1603875478000,
                "leaveTimeDesc": "16:57",
                "activeFlag": "N",
                "orderFlag": "N",
                "shopStatus": 1,
                "shopStatusName": "正常",
                "currentMonthVisitCount": 1,
                "currentMonthVisitCountDesc": "10月第1次拜访",
                "operatorId": 161,
                "operatorName": "陈庆玉",
                "regionName": "雄鹰战队",
                "operatorNameDesc": "陈庆玉-雄鹰战队",
                "signRecordResultType": "valid",
                "unnormal": 0,
                "shopType": "00",
                "shopTypeName": "便利店",
                "shopLevelName": "V2",
                "lostFollowUpReason": ""
            },
            {
                "signId": 3633600,
                "signPicUrl": "https://images.alpha.pinpianyi.cn/images/face/yypp/93c4ff1d7a7f4065832969df33c0dbc0.png",
                "shopId": 477,
                "shopName": "云蚂蚁超市",
                "signTime": "2020-10-28 15:45",
                "leaveTime": 1603871157000,
                "leaveTimeDesc": "15:45",
                "activeFlag": "N",
                "orderFlag": "N",
                "shopStatus": 1,
                "shopStatusName": "正常",
                "currentMonthVisitCount": 7,
                "currentMonthVisitCountDesc": "10月第7次拜访",
                "operatorId": 161,
                "operatorName": "陈庆玉",
                "regionName": "雄鹰战队",
                "operatorNameDesc": "陈庆玉-雄鹰战队",
                "signRecordResultType": "valid",
                "unnormal": 0,
                "shopType": "00",
                "shopTypeName": "便利店",
                "shopLevelName": null,
                "lostFollowUpReason": ""
            },
            {
                "signId": 3633599,
                "signPicUrl": "https://images.alpha.pinpianyi.cn/images/face/yypp/93c4ff1d7a7f4065832969df33c0dbc0.png",
                "shopId": 477,
                "shopName": "云蚂蚁超市",
                "signTime": "2020-10-28 15:45",
                "leaveTime": 1603871105000,
                "leaveTimeDesc": "15:45",
                "activeFlag": "N",
                "orderFlag": "N",
                "shopStatus": 1,
                "shopStatusName": "正常",
                "currentMonthVisitCount": 6,
                "currentMonthVisitCountDesc": "10月第6次拜访",
                "operatorId": 161,
                "operatorName": "陈庆玉",
                "regionName": "雄鹰战队",
                "operatorNameDesc": "陈庆玉-雄鹰战队",
                "signRecordResultType": "valid",
                "unnormal": 0,
                "shopType": "00",
                "shopTypeName": "便利店",
                "shopLevelName": null,
                "lostFollowUpReason": ""
            },
            {
                "signId": 3633581,
                "signPicUrl": "https://images.alpha.pinpianyi.cn/images/face/yypp/93c4ff1d7a7f4065832969df33c0dbc0.png",
                "shopId": 477,
                "shopName": "云蚂蚁超市",
                "signTime": "2020-10-28 11:05",
                "leaveTime": null,
                "leaveTimeDesc": null,
                "activeFlag": "N",
                "orderFlag": "N",
                "shopStatus": 1,
                "shopStatusName": "正常",
                "currentMonthVisitCount": 0,
                "currentMonthVisitCountDesc": "10月第0次拜访",
                "operatorId": 161,
                "operatorName": "陈庆玉",
                "regionName": "雄鹰战队",
                "operatorNameDesc": "陈庆玉-雄鹰战队",
                "signRecordResultType": "time_out_leave_clock_in",
                "unnormal": 0,
                "shopType": "00",
                "shopTypeName": "便利店",
                "shopLevelName": null,
                "lostFollowUpReason": null
            },
            {
                "signId": 3633580,
                "signPicUrl": "https://images.alpha.pinpianyi.cn/images/face/yypp/93c4ff1d7a7f4065832969df33c0dbc0.png",
                "shopId": 625,
                "shopName": "家友超市",
                "signTime": "2020-10-28 11:04",
                "leaveTime": 1603854283000,
                "leaveTimeDesc": "11:04",
                "activeFlag": "N",
                "orderFlag": "N",
                "shopStatus": 1,
                "shopStatusName": "正常",
                "currentMonthVisitCount": 2,
                "currentMonthVisitCountDesc": "10月第2次拜访",
                "operatorId": 161,
                "operatorName": "陈庆玉",
                "regionName": "雄鹰战队",
                "operatorNameDesc": "陈庆玉-雄鹰战队",
                "signRecordResultType": "valid",
                "unnormal": 0,
                "shopType": "00",
                "shopTypeName": "便利店",
                "shopLevelName": "V1",
                "lostFollowUpReason": null
            },
            {
                "signId": 3633577,
                "signPicUrl": "https://images.alpha.pinpianyi.cn/images/face/yypp/93c4ff1d7a7f4065832969df33c0dbc0.png",
                "shopId": 477,
                "shopName": "云蚂蚁超市",
                "signTime": "2020-10-28 10:22",
                "leaveTime": 1603851772000,
                "leaveTimeDesc": "10:22",
                "activeFlag": "N",
                "orderFlag": "N",
                "shopStatus": 1,
                "shopStatusName": "正常",
                "currentMonthVisitCount": 5,
                "currentMonthVisitCountDesc": "10月第5次拜访",
                "operatorId": 161,
                "operatorName": "陈庆玉",
                "regionName": "雄鹰战队",
                "operatorNameDesc": "陈庆玉-雄鹰战队",
                "signRecordResultType": "valid",
                "unnormal": 0,
                "shopType": "00",
                "shopTypeName": "便利店",
                "shopLevelName": "V2",
                "lostFollowUpReason": null
            }
        ]
    }
}
"""