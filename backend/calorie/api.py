import json
from rest_framework.response import Response
from rest_framework.views import APIView as RestfulAPIView
from rest_framework.exceptions import APIException
from rest_framework import status


class ContentType(object):
    json_request = "application/json"
    json_response = "application/json;charset=UTF-8"
    url_encoded_request = "application/x-www-form-urlencoded"
    binary_response = "application/octet-stream"


class JSONParser(object):
    content_type = ContentType.json_request

    @staticmethod
    def parse(body):
        return json.loads(body.decode("utf-8"))


class JSONResponse(object):
    content_type = ContentType.json_response

    @classmethod
    def response(cls, data):
        resp = HttpResponse(json.dumps(data, indent=4), content_type=cls.content_type)
        resp.data = data
        return resp


class APIView(RestfulAPIView):
    """
    Django view的父类, 和django-rest-framework的用法基本一致
     - request.data获取解析之后的json或者urlencoded数据, dict类型
     - self.success, self.error和self.invalid_serializer可以根据业需求修改,
        写到父类中是为了不同的人开发写法统一,不再使用自己的success/error格式
     - self.response 返回一个django HttpResponse, 具体在self.response_class中实现
     - parse请求的类需要定义在request_parser中, 目前只支持json和urlencoded的类型, 用来解析请求的数据
    """

    @staticmethod
    def success(data=None, status=status.HTTP_200_OK):
        return Response({"error": None, "data": data}, status=status)

    @staticmethod
    def error(msg="error", err="error", status=status.HTTP_400_BAD_REQUEST):
        return Response({"error": err, "data": msg}, status=status)


class NotImplementedException(APIException):
    status = status.HTTP_501_NOT_IMPLEMENTED
    defualt_detail = '尚未实现该接口'


class FieldException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = '该请求需要字段'


class NoAttributeInDatabaseException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = '数据库无该字段'


def get_int(input_data, field_name):
    try:
        return int(input_data)
    except Exception as e:
        raise FieldException(f'{field_name} should be an integer')


def check_one_field(request_data, field_name):
    if field_name not in request_data:
        print(f'{field_name} is required')
        raise FieldException(
            {'msg': f'{field_name} is required'}
        )


def check_and_get_int(request_data, field_name):
    check_one_field(request_data, field_name)
    temp_data = request_data[field_name]
    if isinstance(temp_data, list):
        temp_data = temp_data[0]
    return get_int(temp_data, field_name)


def get_user_id(request):
    """
    获取用户的id
    """
    request_data = request.query_params
    """
    如果使用原生的django用户, 可以通过request.user拿到用户对象
    尝试该项目是否可以使用此法
    """
    user_id = None
    try:
        user_id = request.user.id
        assert (user_id is not None)
    except Exception as e:
        print("无法获取request.user.id")
        user_id = check_and_get_int(request_data, 'user_id')
    return user_id
