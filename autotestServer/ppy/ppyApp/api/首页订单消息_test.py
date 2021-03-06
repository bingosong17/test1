# NOTE: Generated By HttpRunner v3.1.3
"""
    概要：
        首页订单消息
    输入参数：
        无
    输出参数：
        无
    前置接口：
        验证码登陆
"""

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCase首页订单消息(HttpRunner):

    config = Config("testcase description").verify(False).base_url("${testEnv($business)}").variables(
        **{
            "business": "",
            "token": "",
        })

    teststeps = [
        Step(
            RunRequest("首页订单消息")
            .get("/app/home/orderNotices")
            .with_headers(
                **{
                    "serviceName": "MALL",
                    "channel": "app",
                    "deviceId": "2cdf701146c959d296b4b455f9623536",
                    "version": "4.4.0",
                    "sessionId": "$token",
                    "Connection": "close",
                    "Accept-Encoding": "gzip",
                    "User-Agent": "okhttp/3.12.0",
                    "Content-Type": "application/json",
                    "Accept-Language": "zh-CN,zh;q=0.8",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.statusCode", 2000)
        ),
    ]


if __name__ == "__main__":
    TestCase首页订单消息().test_start()


"""
response:
{
	"statusCode": 2000,
	"msg": null,
	"traceMsg": "traceId: null",
	"timestamp": 1597136571,
	"signType": null,
	"sign": null,
	"body": {
		"interval": 5,
		"details": [{
			"text": "杭州市左邻右舍...刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com/images/common/03678934e27a4dd7a27dd25d9cfd1d4f.jpg"
		}, {
			"text": "杭州市左邻右舍...刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com/images/common/03678934e27a4dd7a27dd25d9cfd1d4f.jpg"
		}, {
			"text": "杭州市左邻右舍...刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com/images/common/03678934e27a4dd7a27dd25d9cfd1d4f.jpg"
		}, {
			"text": "杭州市左邻右舍...刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com/images/common/03678934e27a4dd7a27dd25d9cfd1d4f.jpg"
		}, {
			"text": "杭州市左邻右舍...刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com/images/common/03678934e27a4dd7a27dd25d9cfd1d4f.jpg"
		}, {
			"text": "杭州市彩芬超市刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com/images/face/d5622fac0ff74974b9101a70dc33984d.jpg"
		}, {
			"text": "杭州市左邻右舍...刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com/images/common/03678934e27a4dd7a27dd25d9cfd1d4f.jpg"
		}, {
			"text": "杭州市啦啦刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com/images/common/da1cae98571e4eac833fbeadbf2fe2df.jpg"
		}, {
			"text": "杭州市玛玛哈哈刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com/images/common/998c48d2a63a4bf0937008cc8354ca6b.jpg"
		}, {
			"text": "杭州市啦啦刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com/images/common/da1cae98571e4eac833fbeadbf2fe2df.jpg"
		}, {
			"text": "杭州市玛玛哈哈刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com/images/common/998c48d2a63a4bf0937008cc8354ca6b.jpg"
		}, {
			"text": "杭州市啦啦刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com/images/common/da1cae98571e4eac833fbeadbf2fe2df.jpg"
		}, {
			"text": "杭州市技术测试...刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com/images/common/d16098e5f739434eb2f2705e7d0a2b29.jpg"
		}, {
			"text": "杭州市迎众便利...刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com//images/face/d5622fac0ff74974b9101a70dc33984d.jpg"
		}, {
			"text": "杭州市哈喽～小...刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com/images/common/1b086bdacf6b49c497894af53e50cd23.jpg"
		}, {
			"text": "杭州市玛玛哈哈刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com/images/common/998c48d2a63a4bf0937008cc8354ca6b.jpg"
		}, {
			"text": "杭州市玛玛哈哈刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com/images/common/998c48d2a63a4bf0937008cc8354ca6b.jpg"
		}, {
			"text": "杭州市左邻右舍...刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com/images/common/03678934e27a4dd7a27dd25d9cfd1d4f.jpg"
		}, {
			"text": "杭州市左邻右舍...刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com/images/common/03678934e27a4dd7a27dd25d9cfd1d4f.jpg"
		}, {
			"text": "杭州市左邻右舍...刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com/images/common/03678934e27a4dd7a27dd25d9cfd1d4f.jpg"
		}, {
			"text": "杭州市左邻右舍...刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com/images/common/03678934e27a4dd7a27dd25d9cfd1d4f.jpg"
		}, {
			"text": "杭州市左邻右舍...刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com/images/common/03678934e27a4dd7a27dd25d9cfd1d4f.jpg"
		}, {
			"text": "杭州市左邻右舍...刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com/images/common/03678934e27a4dd7a27dd25d9cfd1d4f.jpg"
		}, {
			"text": "杭州市杭州新塘...刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com/images/common/263d3822af9a4508a57389c4d68ada50.jpg"
		}, {
			"text": "杭州市哈喽～小...刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com/images/common/1b086bdacf6b49c497894af53e50cd23.jpg"
		}, {
			"text": "杭州市玛玛哈哈刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com/images/common/998c48d2a63a4bf0937008cc8354ca6b.jpg"
		}, {
			"text": "杭州市哈喽～小...刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com/images/common/1b086bdacf6b49c497894af53e50cd23.jpg"
		}, {
			"text": "杭州市哈喽～小...刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com/images/common/1b086bdacf6b49c497894af53e50cd23.jpg"
		}, {
			"text": "杭州市哈喽～小...刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com/images/common/1b086bdacf6b49c497894af53e50cd23.jpg"
		}, {
			"text": "杭州市玛玛哈哈刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com/images/common/998c48d2a63a4bf0937008cc8354ca6b.jpg"
		}, {
			"text": "杭州市测试-技...刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com/images/common/bb6ba9f3a5a34576aeda408940057a6b.jpg"
		}, {
			"text": "杭州市玛玛哈哈刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com/images/common/998c48d2a63a4bf0937008cc8354ca6b.jpg"
		}, {
			"text": "杭州市玛玛哈哈刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com/images/common/998c48d2a63a4bf0937008cc8354ca6b.jpg"
		}, {
			"text": "杭州市玛玛哈哈刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com/images/common/998c48d2a63a4bf0937008cc8354ca6b.jpg"
		}, {
			"text": "杭州市哦好的刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com/images/common/3dc4756ae03f4074aa94a301c249d4cd.jpg"
		}, {
			"text": "杭州市龙华超市刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com/images/face/d5622fac0ff74974b9101a70dc33984d.jpg"
		}, {
			"text": "杭州市兴盛超市刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com/http://images.pinpianyi.com//images/common/367137a73c9d444eb7b599a6916e9ddd.jpg"
		}, {
			"text": "杭州市兴盛超市刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com/http://images.pinpianyi.com//images/common/367137a73c9d444eb7b599a6916e9ddd.jpg"
		}, {
			"text": "杭州市兴盛超市刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com/http://images.pinpianyi.com//images/common/367137a73c9d444eb7b599a6916e9ddd.jpg"
		}, {
			"text": "杭州市兴盛超市刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com/http://images.pinpianyi.com//images/common/367137a73c9d444eb7b599a6916e9ddd.jpg"
		}, {
			"text": "杭州市兴盛超市刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com/http://images.pinpianyi.com//images/common/367137a73c9d444eb7b599a6916e9ddd.jpg"
		}, {
			"text": "杭州市兴盛超市刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com/http://images.pinpianyi.com//images/common/367137a73c9d444eb7b599a6916e9ddd.jpg"
		}, {
			"text": "杭州市哦好的刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com/images/common/3dc4756ae03f4074aa94a301c249d4cd.jpg"
		}, {
			"text": "杭州市哦好的刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com/images/common/3dc4756ae03f4074aa94a301c249d4cd.jpg"
		}, {
			"text": "杭州市哦好的刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com/images/common/3dc4756ae03f4074aa94a301c249d4cd.jpg"
		}, {
			"text": "杭州市哦好的刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com/images/common/3dc4756ae03f4074aa94a301c249d4cd.jpg"
		}, {
			"text": "杭州市龙华超市刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com/images/face/d5622fac0ff74974b9101a70dc33984d.jpg"
		}, {
			"text": "杭州市测试-技...刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com/images/common/bb6ba9f3a5a34576aeda408940057a6b.jpg"
		}, {
			"text": "杭州市龙华超市刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com/images/face/d5622fac0ff74974b9101a70dc33984d.jpg"
		}, {
			"text": "杭州市龙华超市刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com/images/face/d5622fac0ff74974b9101a70dc33984d.jpg"
		}, {
			"text": "杭州市龙华超市刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com/images/face/d5622fac0ff74974b9101a70dc33984d.jpg"
		}, {
			"text": "杭州市哦好的刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com/images/common/3dc4756ae03f4074aa94a301c249d4cd.jpg"
		}, {
			"text": "杭州市哦好的刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com/images/common/3dc4756ae03f4074aa94a301c249d4cd.jpg"
		}, {
			"text": "杭州市哦好的刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com/images/common/3dc4756ae03f4074aa94a301c249d4cd.jpg"
		}, {
			"text": "杭州市江河便利...刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com/images/common/9c1b5594d15a44cca7efd43228e4c0a0.jpg"
		}, {
			"text": "杭州市江河便利...刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com/images/common/9c1b5594d15a44cca7efd43228e4c0a0.jpg"
		}, {
			"text": "武汉市各种小家...刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com///images/common/ec505bb0cc50402da0b41cb01089e2ec.jpg"
		}, {
			"text": "苏州市雅堂小超刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com//images/common/6409e04112924784b058959aba9186ae.jpg"
		}, {
			"text": "苏州市家佳便利...刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com/images/face/sign1047fc13655640c096a02078c6c5bb8c388799.jpg"
		}, {
			"text": "杭州市世纪华联刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com//images/face/91fc3cc013f543d59ab664e0bd570a82.jpg"
		}, {
			"text": "杭州市东升超市刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com/images/face/defe3cde90304b44aab8a3237cc22552.jpg"
		}, {
			"text": "杭州市琼琼烟酒刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com/images/face/3d57775a608145b083dbebceecb81a48.jpg"
		}, {
			"text": "武汉市天天烟酒...刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com//images/common/8776504860414732895fbb65f2a47548.jpg"
		}, {
			"text": "武汉市春光超市刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com///images/common/78b5f55b616f4d6d9e374f7a885577e8.jpg"
		}, {
			"text": "宁波市宏美烟酒刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com//images/face/4ddcce275dd84455b883d684fa77f2de.jpg"
		}, {
			"text": "杭州市麻台传说刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com//images/face/1ddcacd216b04635987ad4639c107222.jpg"
		}, {
			"text": "无锡市锡东超市刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com/images/common/5f683fcb2fec45dc8873e4d0664537d4.jpg"
		}, {
			"text": "成都市时时果蔬刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com/images/common/49a54363c6394ce59c25cb1f941a5777.jpg"
		}, {
			"text": "苏州市百邻汇生...刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com/images/common/e43bee18d1e94b389890e58b3f7a83b4.jpg"
		}, {
			"text": "宁波市菜场超市刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com/images/face/7090cde0536c4039b12c5f432e650128.jpg"
		}, {
			"text": "杭州市烟酒超市刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com///images/common/d3e4a323146444f89c3ef86d662728fe.jpg"
		}, {
			"text": "武汉市芙蓉兴盛刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com//images/face/sign41721a9e60364908abed65799b1c088b170589.jpg"
		}, {
			"text": "杭州市世纪华联刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com/images/face/d5622fac0ff74974b9101a70dc33984d.jpg"
		}, {
			"text": "杭州市手抓排骨...刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com/images/face/09f8fc8881434ab58f4e707996de36a6.jpg"
		}, {
			"text": "广州市芙蓉兴盛...刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com/images/common/c5a3f1935ac64137ab44d9c0c1d356a2.jpg"
		}, {
			"text": "杭州市洗衣液刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com/images/face/4fd2395d16c644ecbcd8d9fcadc7cbf3.jpg"
		}, {
			"text": "杭州市便利超市刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com/images/face/d5622fac0ff74974b9101a70dc33984d.jpg"
		}, {
			"text": "苏州市好又多超...刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com/images/common/2261e72d4e4f49d89a8cebb087825364.jpg"
		}, {
			"text": "杭州市雅堂小超刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com/images/common/d141aaa2fc504202a91d6067f8693ab0.jpg"
		}, {
			"text": "武汉市银丰超市刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com//images/common/324c64427efc4633bcb62111796d7ea8.jpg"
		}, {
			"text": "武汉市等你喜糖...刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com/images/face/2c31a43a9b464350b49f9be5274ae048.jpg"
		}, {
			"text": "杭州市杭州世纪...刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com///images/common/03cc8686bbc24540a0b92e40f8aab8be.jpg"
		}, {
			"text": "郑州市金龙烟酒刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com/images/common/51a94ad540804feebdf9561431d787cb.jpg"
		}, {
			"text": "佛山市荣惠商店刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com/images/common/4e4d1db48c3940f2bdda6e53afb88f3d.jpg"
		}, {
			"text": "宁波市颐家便利...刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com/images/common/be990b94375a4359a10e16931b2684d1.jpg"
		}, {
			"text": "广州市好运来超...刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com/images/common/8d489c0b01a74d3f892d22e750f33d40.jpg"
		}, {
			"text": "苏州市诚价商行刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com//images/common/da0c0fe8087447448551a834ccb583c8.jpg"
		}, {
			"text": "杭州市浙诚烟酒刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com/images/face/d5622fac0ff74974b9101a70dc33984d.jpg"
		}, {
			"text": "宁波市富发超市刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com//images/face/9b3b2d535f9a4e72938973d895303433.jpg"
		}, {
			"text": "南京市小方超市刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com//images/common/0a780230cdda4065b09ebbb5a72ac318.jpg"
		}, {
			"text": "南京市烟酒超市刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com//images/common/efa73f31ea9842c0891dd2c444eb24a8.jpg"
		}, {
			"text": "苏州市江南百货...刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com/images/common/5d831caa78b041ed985ab996e1b85857.jpg"
		}, {
			"text": "杭州市子旭便利...刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com/images/face/9031be89dd50464ea3430e1a5ea01134.jpg"
		}, {
			"text": "佛山市银坳日用...刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com/images/face/yypp/1eedf503ab5a4d53a4df775b17d0aa89.jpg"
		}, {
			"text": "宁波市称心烟酒...刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com/images/face/a6712ef6d79143a390109ba66a8ba58c.jpg"
		}, {
			"text": "无锡市晨光文具...刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com/images/face/yypp/63d40adfe81c4f76bde7fd4c8a1e73cf.jpg"
		}, {
			"text": "杭州市云蚂蚁便...刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com/images/face/02336495f7e741dc8b6ca4b1d11ef785.jpg"
		}, {
			"text": "杭州市杭州华联刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com/images/face/2e385df562044e27a1c48f65cd24936a.jpg"
		}, {
			"text": "杭州市大众粮油...刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com/images/face/1502c6beb80440da9eaa957e52373508.jpg"
		}, {
			"text": "杭州市雨凯烟酒...刚刚下单成功",
			"headerPics": "https://images.pinpianyi.com/images/face/d5622fac0ff74974b9101a70dc33984d.jpg"
		}]
	}
}
"""