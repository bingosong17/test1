#! /usr/bin/env python
#-*- coding:utf-8 -*-

#author:bingo
# NOTE: Generated By HttpRunner v3.1.3
"""
    概要：
        用户对指定商品下单，使用账户余额付款
    输入参数：
        "goodsId": 商品id
        "goodsNu": 下单商品数量
    输出参数：
        无
    前置接口：
        验证码登陆
"""

from httprunner import HttpRunner, Config, Step, RunTestCase
from ppyApp.api.提交设备信息_test import TestCase提交设备信息 as 提交设备信息
from ppyApp.api.获取当前用户资料_test import TestCase获取当前用户资料 as 获取当前用户资料
from ppyApp.api.获取app广告页列表_test import TestCase获取App广告页列表 as 获取App广告页列表
from ppyApp.api.查询审核信息_test import TestCase查询审核信息 as 查询审核信息
from ppyApp.api.获取购物车信息_test import TestCase获取购物车信息 as 获取购物车信息
from ppyApp.api.首页BD业务员推送消息提醒_test import TestCase首页Bd业务员推送消息提醒 as 首页Bd业务员推送消息提醒
from ppyApp.api.新人商品显示模块_test import TestCase新人商品显示模块 as 新人商品显示模块
from ppyApp.api.首页订单消息_test import TestCase首页订单消息 as 首页订单消息
from ppyApp.api.首页导购_test import TestCase首页导购 as 首页导购
from ppyApp.api.获取app每天首次启动弹框列表_test import TestCase获取App每天首次启动弹框列表 as 获取App每天首次启动弹框列表
from ppyApp.api.APP首页背景图和浮窗_test import TestCaseApp首页背景图和浮窗 as App首页背景图和浮窗
from ppyApp.api.大家都在买查询_test import TestCase大家都在买查询 as 大家都在买查询
from ppyApp.api.为您推荐商品查询_test import TestCase为您推荐商品查询 as 为您推荐商品查询
from ppyApp.api.获取商品明细_test import TestCase获取商品明细 as 获取商品明细
from ppyApp.api.商品详情页相似推荐查询_test import TestCase商品详情页相似推荐查询 as 商品详情页相似推荐查询
from ppyApp.api.获取商品ID优惠明细_test import TestCase获取商品Id优惠明细 as 获取商品Id优惠明细
from ppyApp.api.添加商品_test import TestCase添加商品 as 添加商品
from ppyApp.api.特价活动引导_test import TestCase特价活动引导 as 特价活动引导
from ppyApp.api.获取购物车信息_分品类购物车结构_test import TestCase获取购物车信息分品类购物车结构 as 获取购物车信息分品类购物车结构
from ppyApp.api.猜您喜欢商品_test import TestCase猜您喜欢商品 as 猜您喜欢商品
from ppyApp.api.获取购物车结算信息_test import TestCase获取购物车结算信息 as 获取购物车结算信息
from ppyApp.api.创建订单_test import TestCase创建订单 as 创建订单
from ppyApp.api.获取订单摘要信息_test import TestCase获取订单摘要信息 as 获取订单摘要信息
from ppyApp.api.发起支付_test import TestCase发起支付 as 发起支付
from ppyApp.api.获取订单详情_test import TestCase获取订单详情 as 获取订单详情


class TestCase用户下单(HttpRunner):

    config = Config("testcase description").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "",
            "phone": "15355428100",
            "token": "${getSession($business,$phone)}",
            "goodsId": "6565",
            "goodsNu": 10
        }
    ).export(*["orderNo"])

    teststeps = [
        Step(
            RunTestCase("提交设备信息").call(提交设备信息)
        ),
        Step(
            RunTestCase("获取当前用户资料").setup_hook("${清空用户购物车($phone)}")
                .call(获取当前用户资料)
        ),
        Step(
            RunTestCase("获取app广告页列表").call(获取App广告页列表)
        ),
        Step(
            RunTestCase("查询审核信息").call(查询审核信息)
        ),
        Step(
            RunTestCase("获取购物车信息").call(获取购物车信息)
        ),
        Step(
            RunTestCase("首页BD业务员推送消息提醒").call(首页Bd业务员推送消息提醒)
        ),
        Step(
            RunTestCase("新人商品显示模块").call(新人商品显示模块)
        ),
        Step(
            RunTestCase("首页订单消息").call(首页订单消息)
        ),
        Step(
            RunTestCase("首页导购").call(首页导购)
        ),
        Step(
            RunTestCase("获取App每天首次启动弹框列表").call(获取App每天首次启动弹框列表)
        ),
        Step(
            RunTestCase("App首页背景图和浮窗").call(App首页背景图和浮窗)
        ),
        Step(
            RunTestCase("大家都在买查询").call(大家都在买查询)
        ),
        Step(
            RunTestCase("为您推荐商品查询").call(为您推荐商品查询)
        ),
        Step(
            RunTestCase("获取商品明细").call(获取商品明细)
        ),
        Step(
            RunTestCase("商品详情页相似推荐查询").call(商品详情页相似推荐查询)
        ),
        Step(
            RunTestCase("获取商品Id优惠明细").call(获取商品Id优惠明细)
        ),
        Step(
            RunTestCase("添加商品到购物车").call(添加商品)
        ),
        Step(
            RunTestCase("特价活动引导").call(特价活动引导)
        ),
        Step(
            RunTestCase("获取购物车信息分品类购物车结构").call(获取购物车信息分品类购物车结构)
        ),
        Step(
            RunTestCase("猜您喜欢商品").call(猜您喜欢商品)
        ),
        Step(
            RunTestCase("获取购物车结算信息").call(获取购物车结算信息)
        ),
        Step(
            RunTestCase("创建订单").call(创建订单).export(*["orderNo"])
        ),
        Step(
            RunTestCase("获取订单摘要信息").call(获取订单摘要信息)
        ),
        Step(
            RunTestCase("发起支付").call(发起支付).teardown_hook("${sleep_N_secs(4)}")
        ),
        Step(
            RunTestCase("获取订单详情").call(获取订单详情)
        ),

    ]


if __name__ == "__main__":
    TestCase用户下单().test_start()

