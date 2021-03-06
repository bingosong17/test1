# NOTE: Generated By HttpRunner v3.1.3
"""
    概要：
        新增商品
    输入参数：
        "name": 商品名称
        "barCode": 条形码
        "barImageUrl": 条形码图片地址
        "barStatus": 是否验证 0未验证1已验证
        "recycled": 是否被回收：0-否,1-是
        "specialty": 是否特产 1:是 0:否
        "isImport": 是否进口 1:是 0:否
        "single": 是否单品 0否 1是
        "goodsPacknumUnit": 商品规格-包装内商品数量单位
        "goodsInsidePackUnit": 商品规格-包装内中内包的数量单位
        "goodsInsidePackNum": 商品规格-包装内中内包的商品数量
        "goodsPacknum": 商品规格-包装内商品数量
        "goodsCapacity": 商品规格-商品单个容量规格
        "theoryVolume": 虚拟体积
        "weight": 重量
        "scatteredPrice": 零批价,单位为元
        "retailPrice": 建议零售价,单位为元
        "guaranteePeriod": 保质期
        "brand": 品牌
        "brandId": 品牌ID
        "specificationDesc": 商品规格描述
        "manufacturer": 生产厂家
        "backstageCategoryId": 后台类目ID
        "logisticsPurchaseNum": 物流件数,商品件数(派物流)
        "storageMethod": 储藏方法
    输出参数：
        无
    前置接口：
        无
"""


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase,client
import random


class TestCase新增商品(HttpRunner):
    config = Config("新增商品").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "yyht",
            "session": "${getSession($business)}",
            "name": "可口可乐就这么地1ml/箱",
            "barImageUrl": "",
            "barCode": random.randint(111111111111, 999999999999),
            "barStatus": 1,
            "recycled": 0,
            "specialty": "0",
            "isImport": "0",
            "single": 1,
            "goodsPacknumUnit": "",
            "goodsInsidePackUnit": "",
            "goodsInsidePackNum": None,
            "goodsPacknum": None,
            "goodsCapacity": 1,
            "theoryVolume": 1,
            "weight": 1,
            "scatteredPrice": 1,
            "retailPrice": 1,
            "guaranteePeriod": 1,
            "brand": 4,
            "brandId": 4,
            "specificationDesc": "商品用于测试",
            "manufacturer": "1",
            "backstageCategoryId": 377,
            "logisticsPurchaseNum": 1,
            "storageMethod": "1",
        })

    teststeps = [
        Step(
            RunRequest("/alpha_t/ppy-op-api/goods/addGoods")
            .post("/ppy-op-api/goods/addGoods")
            .with_headers(
                **{
                    "Connection": "keep-alive",
                    "Content-Length": "945",
                    "sessionId": "$session",
                    "Sec-Fetch-Dest": "empty",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
                    "systemCode": "yypp",
                    "Content-Type": "application/json",
                    "Accept": "*/*",
                    "Sec-Fetch-Site": "same-origin",
                    "Sec-Fetch-Mode": "cors",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                }
            )
            .with_json(
                {
                    "specialty": "$specialty",
                    "isImport": "$isImport",
                    "single": "$single",
                    "dan": 1,
                    "id": None,
                    "mainImages": [
                        "https://images.pinpianyi.com/images/library/2d268fbf1e85455d921b52fcd6a7034b.jpg"
                    ],
                    "detailImages": [
                        "https://images.pinpianyi.com/images/library/2d268fbf1e85455d921b52fcd6a7034b.jpg"
                    ],
                    "goodsPacknumUnit": "$goodsPacknumUnit",
                    "goodsInsidePackUnit": "$goodsInsidePackUnit",
                    "goodsInsidePackNum": "$goodsInsidePackNum",
                    "goodsPacknum": "$goodsPacknum",
                    "goodsCapacity": "$goodsCapacity",
                    "theoryVolume": "$theoryVolume",
                    "weight": "$weight",
                    "scatteredPrice": "$scatteredPrice",
                    "retailPrice": "$retailPrice",
                    "guaranteePeriod": "$guaranteePeriod",
                    "brand": "$brand",
                    "brandId": "$brandId",
                    "goodsCapacityUnit": "ml",
                    "goodsPacketUnit": "箱",
                    "specificationDesc": "$specificationDesc",
                    "storageMethod": "$storageMethod",
                    "gatherUserName": 3328,
                    "gatherUserId": 3328,
                    "guaranteePeriodUnit": "年",
                    "manufacturer": "$manufacturer",
                    "backstageCategoryId": "$backstageCategoryId",
                    "logisticsPurchaseNum": "$logisticsPurchaseNum",
                    "lwh": "1x1x1",
                    "name": "$name",
                    "recycled": "$recycled",
                    "barCode": {
                        "barCode": "$barCode",
                        "barImageUrl": "$barImageUrl",
                        "barStatus": "$barStatus",
                    },
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.statusCode", 2000)
            .assert_equal("body.body", "操作成功")
        ),
    ]


if __name__ == "__main__":
    TestCase新增商品().test_start()
