#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""account_user_viewset -- account user viewset

"""
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.db.models import Q
from django.contrib.auth.models import Permission

from account.models.account_model import AccountUser
from account.serializers.account_serializer import AccountUserSerializer

from utils.superuser_permission import SuperUserPermission


class AccountUserSimpleViewSet(viewsets.ModelViewSet):
    """AccountUserSimpleViewSet

    AccountUserSimpleViewSet is a viewsets.ModelViewSet.
    Responsibility:
    """
    # permission_classes = (IsSuperUser, )
    permission_classes = [
        # IsAuthenticated,
    ]
    queryset = AccountUser.objects.all()
    serializer_class = AccountUserSerializer
    http_method_names = [
        'get',
    ]

    def get_queryset(self):
        queryset = self.queryset
        keyword = self.request.GET.get('q')
        if keyword:
            queryset = queryset.filter(
                Q(username__icontains=keyword) |
                Q(email__icontains=keyword)
            )
        return queryset



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# account_user_viewset.py ends here
