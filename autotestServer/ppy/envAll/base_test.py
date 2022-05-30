import logging
from yyht.用户中心.api.店铺列表_test import TestCase店铺查询 as a

if __name__ == '__main__':
    classA = a()
    data = {
        "userphone": "13819857342",
    }
    classA.config.variables(**data)
    classA.test_start()
    data1 = classA.get_export_variables()
    data2 = classA.get_step_datas()
    data3 = classA.get_summary()
    data4 = classA.config.name
    data5 = classA.config.path
    data6 = classA.get_summary().in_out.config_vars
    logging.error(data1)
    logging.error(data2)
    logging.error(data3)
    logging.error(data4)
    logging.error(data5)
    logging.error(data6)
