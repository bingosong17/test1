from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from envAll.basic_test import TestCaseBasic as CaseBasic

import os
import sys

curPath = os.path.abspath(os.path.dirname(__file__))
sys.path.append(curPath[0])
from envAll import testData


class TestCase测试(HttpRunner):
    config = Config("testcase description").verify(False).variables(
        **{
            "pageData": testData.pageData,
            "jsonData": testData.jsonData,
            "regionPointsList": testData.regionPointsList,
            "status": '600',
        }
    ).export(*["status"])
    teststeps = [
        Step(
            RunTestCase("assert_contains函数使用示范").call(CaseBasic)
            # 表明 汪烽程，浙AK8M05两个值都必须在pageData中出现，参数不限
            .teardown_hook("${assert_contains($pageData,汪烽程,浙AK8M05)}")
            # 表明 汪烽程，浙AK8M05两个值一个或多个在pageData中出现，参数不限
            .teardown_hook("${assert_contains($pageData,allIn=0,汪烽程,浙AK8M05)}")
            # 表明pageData中的字典，存在一个字典同时有driverName=汪烽程和licensePlateNumber=浙A3G0T3，参数不限
            .teardown_hook("${assert_contains($pageData,driverName=汪烽程,licensePlateNumber=浙A3G0T3)}")
            # 表明pageData中的字典，存在一个字典内容包含driverName=汪烽程或licensePlateNumber=浙A3G0T3，参数不限
            .teardown_hook("${assert_contains($pageData,allIn=0,driverName=汪烽程,licensePlateNumber=浙A3G0T3)}")
            # 表明pageData中的字典，存在一个字典内容包含phoneNumber="13033711680"，参数不限，注意字符串表达方式
            .teardown_hook("${assert_contains($pageData,phoneNumber=strType13033711680)}")
            # 表明pageData中的字典，存在一个字典内容包含status=600，参数不限，注意整型表达方式
            .teardown_hook("${assert_contains($pageData,status=intType$status)}")
        ),
        Step(
            RunTestCase("assert_not_contains函数使用示范").call(CaseBasic)
            # 表明 汪烽程1，浙AK8M051两个值不在pageData中出现，参数不限
            .teardown_hook("${assert_not_contains($pageData,汪烽程1,浙AK8M051)}")
            # 表明pageData中的字典，任意字典都不满足driverName=汪烽程1或licensePlateNumber=浙A3G0T31，参数不限
            .teardown_hook("${assert_not_contains($pageData,driverName=汪烽程1,licensePlateNumber=浙A3G0T31)}")
        ),
        Step(
            RunTestCase("assert_pageDataLength函数使用示范").call(CaseBasic)
            # 判定pageData列表中的字典数为10
            .teardown_hook("${assert_pageDataLength($pageData,10)}")
        ),
        Step(
            RunTestCase("makeGoodPoint函数使用示范")
            # 先调用makeGoodPoint找到有效点，随后调用getLongitude和getLatitude函数获取经纬度。
            .setup_hook("${makeGoodPoint($regionPointsList)}")
            .call(CaseBasic)
            .teardown_hook("${getLongitude()}")
            .teardown_hook("${getLatitude()}")
        ),
        Step(
            RunTestCase("exportValue函数使用示范").with_variables(
                **{
                    # 从pageData中寻找一个字典，字典phoneNumber="13738113393"，expectedIncome="24.11"，最后返回得该字典的id的值
                    # 注意strType的使用
                    "id": "${exportValue($pageData,id,phoneNumber=strType13738113393,expectedIncome=strType24.11)}"
                }
            )
            .call(CaseBasic)
        ),
        Step(
            RunTestCase("modifyPageData函数使用示范").with_variables(
                **{
                    # 修改pageData中的每个字典，为每个字典增加logisticsArea="3310001"键值对，把修改后的返回，注意，增加
                    # 是在前面添加ADD，还有值的字型定义strType，目前仅有增加，修改/删除需要时再添加
                    "id1": "${modifyPageData($pageData,ADDlogisticsArea=strType3310001)}"
                }
            ).call(CaseBasic)
        ),
        Step(
            RunTestCase("getPageDataToList函数使用示范").with_variables(
                **{
                    # 提取pageData中的每个字典中key为id的键值对的值，组成列表返回
                    "id1": "${getPageDataToList($pageData,id)}"
                }
            ).call(CaseBasic)
        ),
        Step(
            RunTestCase("hapentime函数使用示范").with_variables(
                **{
                    # 生成一个时间为当前时间增加两个小时，时间格式为：'%Y-%m-%d %H:%M'，即:2020-12-11 15:30
                    # 参数中，第一位为时间参数，第二位为类型参数，第三位为时间单位
                    # 第一位时间参数: 默认转成int类型使用
                    # 第二位类型参数: 0-'%Y-%m-%d %H:%M',1-'%Y-%m-%d',2-'%Y-%m-%d %H:%M:%S',3-'%Y-%m'
                    # 第三位时间单位: h-hours,s-secondes,d-days,y-years,mon-months,min-minutes
                    "time1": "${hapentime(2,0,h)}"
                }
            ).call(CaseBasic)
        ),
        Step(
            RunTestCase("exportJsonValue函数使用示范").with_variables(
                **{
                    # 在jsonData中，寻找键值为id的值，并返回，jsonData为json的数据
                    "id": "${exportJsonValue($jsonData,id)}"
                }
            ).call(CaseBasic)
        ),
    ]


if __name__ == "__main__":
    TestCase测试().test_start()
