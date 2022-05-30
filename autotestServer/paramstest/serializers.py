from rest_framework import serializers


class ParamTestSerializer(serializers.Serializer):
    path = serializers.CharField()
    email = serializers.CharField()


class HttpRunnerTestSerializer(serializers.Serializer):
    """
        session和password至少上传一个。session上传通常由前端进行，password由接口
        ding参数作为是否发送脚本结果到钉钉群
        webhook和secret两个参数为钉钉群参数，设置默认值，可不上传
    """
    path = serializers.CharField(required=True)
    env = serializers.CharField(required=True)
    cityCode = serializers.CharField(required=True)
    phone = serializers.CharField(required=True, max_length=11, min_length=11)
    password = serializers.CharField(default=None)
    session = serializers.CharField(default=None)
    ding = serializers.BooleanField(default=False)
    webhook = serializers.CharField(default="https://oapi.dingtalk.com/robot/send?access_token"
                                            "=d420e168fe54b6269b616a5c85d770ab1e23295933ff65f73ec92c5f5f06d4a3")
    secret = serializers.CharField(default='Hi:')
    scriptData = serializers.DictField(required=True)

    def validate(self, attrs):
        """
        验证判定password和session不能同时为空
        :param attrs:
        """
        if (attrs["password"] is None) and (attrs["session"] is None):
            raise serializers.ValidationError("参数password和参数session不能同时为空")
        return attrs


class InFileSerializer(serializers.Serializer):
    file = serializers.CharField(required=True)


class MakeCmdSerializer(serializers.Serializer):
    cmd = serializers.CharField(required=True)
    agrstr = serializers.CharField(required=False, allow_null=True, allow_blank=True)


class GetScriptResultSerializer(serializers.Serializer):
    report = serializers.CharField(required=True)


class BasePathSerializer(serializers.Serializer):
    path = serializers.CharField(required=True)


class GetScriptTreeSerializer(serializers.Serializer):
    """
    :type为真时，返回tree，为假时，返回list
    """
    type = serializers.BooleanField(required=True)
