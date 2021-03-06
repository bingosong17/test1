# NOTE: Generated By HttpRunner v3.1.4
"""
    概要：
        公海列表查询
    输入参数：
        "status": 客户状态(0 已停业 1 正常 2 黑名单 3 注册中 4 未审核 5 审核未通过 6 待平台复审)
        "pageSize": 每页数量
        "longitude": 经度
        "manyDayNotOrder": 近多少天未下单
        "userSignStatus": 每日签到标识(0/null:关闭，1:为打开状态)
        "latitude": 纬度
        "type": 客户类型(1合作店铺2潜在店铺3合作供应商4潜在供应商)
        "manyDayNotLogin": 近多少天未登陆
    输出参数：
        "pageData":店铺
    前置接口：
        无
"""


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCase公海列表查询(HttpRunner):

    config = Config("公海列表查询").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "ppApp",
            "phone": "15757113586",
            "session": "${getSession($business,$phone)}",
            "status": 1,
            "pageSize": 10,
            "longitude": "120.260270",
            "manyDayNotOrder": 0,
            "userSignStatus": 0,
            "latitude": "30.203789",
            "type": "1",
            "manyDayNotLogin": 0,
        }).export(*["pageData", "longitude", "latitude"])

    teststeps = [
        Step(
            RunRequest("/ppy-pinpin/myCustomer/regionShopRelList")
            .post("/myCustomer/regionShopRelList")
            .with_headers(
                **{
                    "Accept": "*/*",
                    "Accept-Language": "zh-Hans-CN;q=1",
                    "Accept-Encoding": "gzip, deflate",
                    "Content-Type": "application/json",
                    "sessionId": "$session",
                    "deviceId": "0380efdbdb0938af0d7a3852519f361a86ff",
                    "User-Agent": "Pinpin/3.7.0 (iPhone; iOS 11.1.2; Scale/3.00)",
                    "Content-Length": "156",
                    "serviceName": "NEW-PP",
                    "Connection": "keep-alive",
                }
            )
            .with_json(
                {
                    "status": "$status",
                    "pageSize": "$pageSize",
                    "longitude": "$longitude",
                    "manyDayNotOrder": "$manyDayNotOrder",
                    "userSignStatus": "$userSignStatus",
                    "latitude": "$latitude",
                    "type": "$type",
                    "manyDayNotLogin": "$manyDayNotLogin",
                    "pageNum": 1,
                }
            ).extract()
            .with_jmespath("body.body.pageData", "pageData")
            .with_jmespath("body.body.pageData[0].longitude", "longitude")
            .with_jmespath("body.body.pageData[0].latitude", "latitude")
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.statusCode", 2000)
        ),
    ]


if __name__ == "__main__":
    TestCase公海列表查询().test_start()
"""
response:
body     : {
    "statusCode": 2000,
    "msg": null,
    "traceMsg": "traceId: null",
    "timestamp": 1603785432,
    "signType": null,
    "sign": null,
    "body": {
        "pageNum": 1,
        "pageSize": 10,
        "pageCount": 3,
        "totalSize": 29,
        "pageData": [
            {
                "id": 26914,
                "shopName": "便利店",
                "specificAddress": "绍兴路400弄6号浙报智库创意产业园",
                "pics": "https://images.alpha.pinpianyi.cn/images/face/fc56f245391a4aa7aae4824a50ff0a83.jpg",
                "shopStatus": 3,
                "shopStatusText": "存活用户",
                "longitude": "120.166039646306100000",
                "latitude": "30.302026529001350000",
                "status": "1",
                "statusText": "正常",
                "distance": 14186.01,
                "picUrl": null,
                "shopType": "00",
                "shopTypeText": "便利店",
                "payOrderEndDate": "2020-09-13 21:40:07",
                "loginEndDate": "2020-09-13 21:40:07",
                "operatorId": -1,
                "thisMonthOrderNum": 0,
                "lastMonthOrderNum": 1,
                "type": 1,
                "memberLevelName": null,
                "shopLevel": "V1",
                "shopTasks": null
            },
            {
                "id": 29284,
                "shopName": "华联超市",
                "specificAddress": "中粮方圆府楼底1号",
                "pics": "https://images.alpha.pinpianyi.cn/images/face/d855eb533b87466ca6b4555b0a9c8d52.jpg",
                "shopStatus": 3,
                "shopStatusText": "低频用户",
                "longitude": "120.169766575668530000",
                "latitude": "30.314864258575770000",
                "status": "1",
                "statusText": "正常",
                "distance": 15103.15,
                "picUrl": null,
                "shopType": "00",
                "shopTypeText": "便利店",
                "payOrderEndDate": "2020-09-15 10:10:46",
                "loginEndDate": "2020-09-15 10:10:46",
                "operatorId": -1,
                "thisMonthOrderNum": 0,
                "lastMonthOrderNum": 4,
                "type": 1,
                "memberLevelName": null,
                "shopLevel": "V2",
                "shopTasks": null
            },
            {
                "id": 30175,
                "shopName": "拼便宜-客服部-马娜娜",
                "specificAddress": "华业大厦801-806",
                "pics": "https://images.alpha.pinpianyi.cn/images/common/6cc562ec46174696ad01ef4cb5f798d0.jpg",
                "shopStatus": 1,
                "shopStatusText": "休眠用户",
                "longitude": "120.161057660572300000",
                "latitude": "30.241709340541460000",
                "status": "1",
                "statusText": "正常",
                "distance": 10423.33,
                "picUrl": null,
                "shopType": "00",
                "shopTypeText": "便利店",
                "payOrderEndDate": null,
                "loginEndDate": null,
                "operatorId": -1,
                "thisMonthOrderNum": 0,
                "lastMonthOrderNum": 0,
                "type": 1,
                "memberLevelName": null,
                "shopLevel": null,
                "shopTasks": null
            },
            {
                "id": 36848,
                "shopName": "豫杭酒水",
                "specificAddress": "横塘村三组103号",
                "pics": "https://images.alpha.pinpianyi.cn/images/common/31931a6770594870ba19ce0ebb13ff55.jpg",
                "shopStatus": 2,
                "shopStatusText": "休眠用户",
                "longitude": "120.196809000000000000",
                "latitude": "30.323722000000000000",
                "status": "1",
                "statusText": "正常",
                "distance": 14662.69,
                "picUrl": null,
                "shopType": "08",
                "shopTypeText": "拼易购",
                "payOrderEndDate": null,
                "loginEndDate": null,
                "operatorId": null,
                "thisMonthOrderNum": 0,
                "lastMonthOrderNum": 0,
                "type": 1,
                "memberLevelName": null,
                "shopLevel": null,
                "shopTasks": null
            },
            {
                "id": 50422,
                "shopName": "玉勇批发",
                "specificAddress": "观巷63号玉勇批发",
                "pics": "https://images.alpha.pinpianyi.cn/images/face/a5b2ff009b12406eb0cc45223887e0c1.jpg",
                "shopStatus": 1,
                "shopStatusText": "注册未激活",
                "longitude": "120.179333000000000000",
                "latitude": "30.278510000000000000",
                "status": "1",
                "statusText": "正常",
                "distance": 11379.1,
                "picUrl": null,
                "shopType": "08",
                "shopTypeText": "拼易购",
                "payOrderEndDate": null,
                "loginEndDate": null,
                "operatorId": -1,
                "thisMonthOrderNum": 0,
                "lastMonthOrderNum": 0,
                "type": 1,
                "memberLevelName": null,
                "shopLevel": null,
                "shopTasks": null
            },
            {
                "id": 67567,
                "shopName": "西湖区测试",
                "specificAddress": "华业大厦806",
                "pics": "https://images.alpha.pinpianyi.cn/images/face/b58f865c2ac843f49b7d4b6711ea852d.jpg",
                "shopStatus": 1,
                "shopStatusText": "注册未激活",
                "longitude": "120.173770000000000000",
                "latitude": "30.333270000000000000",
                "status": "1",
                "statusText": "正常",
                "distance": 16622.27,
                "picUrl": null,
                "shopType": "00",
                "shopTypeText": "便利店",
                "payOrderEndDate": null,
                "loginEndDate": null,
                "operatorId": -1,
                "thisMonthOrderNum": 0,
                "lastMonthOrderNum": 0,
                "type": 1,
                "memberLevelName": null,
                "shopLevel": null,
                "shopTasks": null
            },
            {
                "id": 106360,
                "shopName": "杭州肯道贸易有限公司",
                "specificAddress": "德胜路28号c区11号",
                "pics": "https://images.alpha.pinpianyi.cn//images/common/c847efc703614aa792c5940b86517613.jpg",
                "shopStatus": 1,
                "shopStatusText": "注册未激活",
                "longitude": "120.172361612846070000",
                "latitude": "30.301048115762594000",
                "status": "1",
                "statusText": "正常",
                "distance": 13720.61,
                "picUrl": null,
                "shopType": "08",
                "shopTypeText": "拼易购",
                "payOrderEndDate": null,
                "loginEndDate": null,
                "operatorId": null,
                "thisMonthOrderNum": 0,
                "lastMonthOrderNum": 0,
                "type": 1,
                "memberLevelName": null,
                "shopLevel": null,
                "shopTasks": null
            },
            {
                "id": 106414,
                "shopName": "港侠酒水",
                "specificAddress": "德胜路28号",
                "pics": "https://images.alpha.pinpianyi.cn/images/common/33d053221f5640cda4803a84a46ffb83.jpg",
                "shopStatus": 1,
                "shopStatusText": "注册未激活",
                "longitude": "120.173071057118380000",
                "latitude": "30.301310956727920000",
                "status": "1",
                "statusText": "正常",
                "distance": 13701.89,
                "picUrl": null,
                "shopType": "08",
                "shopTypeText": "拼易购",
                "payOrderEndDate": null,
                "loginEndDate": null,
                "operatorId": -1,
                "thisMonthOrderNum": 0,
                "lastMonthOrderNum": 0,
                "type": 1,
                "memberLevelName": null,
                "shopLevel": null,
                "shopTasks": null
            },
            {
                "id": 116983,
                "shopName": "有爱社区集市",
                "specificAddress": "西牌楼社区8幢警务室旁（望江路慧娟面馆旁边入口进入50米左右",
                "pics": "https://images.alpha.pinpianyi.cn/images/common/c742adf360b74bf29f16861753d2188c.jpg",
                "shopStatus": 5,
                "shopStatusText": "低频用户",
                "longitude": "120.176708132480340000",
                "latitude": "30.237434955026610000",
                "status": "1",
                "statusText": "正常",
                "distance": 8857.74,
                "picUrl": null,
                "shopType": "08",
                "shopTypeText": "拼易购",
                "payOrderEndDate": null,
                "loginEndDate": null,
                "operatorId": -1,
                "thisMonthOrderNum": 0,
                "lastMonthOrderNum": 0,
                "type": 1,
                "memberLevelName": null,
                "shopLevel": null,
                "shopTasks": null
            },
            {
                "id": 145900,
                "shopName": "测试999",
                "specificAddress": "哈哈哈哈哈哈哈哈哈哈",
                "pics": "https://images.alpha.pinpianyi.cn/images/common/45c60d531cd74f6da7be8744de19861e.jpg",
                "shopStatus": 1,
                "shopStatusText": "注册未激活",
                "longitude": "120.188220173375310000",
                "latitude": "30.226974180285640000",
                "status": "1",
                "statusText": "正常",
                "distance": 7387.56,
                "picUrl": null,
                "shopType": "00",
                "shopTypeText": "便利店",
                "payOrderEndDate": null,
                "loginEndDate": null,
                "operatorId": null,
                "thisMonthOrderNum": 0,
                "lastMonthOrderNum": 0,
                "type": 1,
                "memberLevelName": null,
                "shopLevel": null,
                "shopTasks": null
            }
        ]
    }
}
"""