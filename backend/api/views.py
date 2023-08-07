from django.shortcuts import render
from api.serializers import UserSerializer


def jwt_response_payload_handler(token, user=None, request=None):
    data = UserSerializer(user, context={'request': request}).data
    data['token'] = token
    return {
        'user': data
    }
