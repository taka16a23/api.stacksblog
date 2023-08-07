#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""LoginUserViewSet -- login user view set

"""
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class LoginUserView(APIView):
    permission_classes = [
        # IsAuthenticated,
    ]
    authentication_classes = [
        TokenAuthentication,
    ]

    def get(self, request, format=None):
        data = {
            'username': request.user.username,
            'email': request.user.email,
        }
        return Response(data)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# LoginUserViewSet.py ends here
