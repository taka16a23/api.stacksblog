#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""account_user_viewset -- account user viewset

"""
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import Permission

from account.models.account_model import AccountUser
from account.serializers.account_serializer import AccountUserSerializer


class AccountUserViewSet(viewsets.ModelViewSet):
    """AccountUserViewSet

    AccountUserViewSet is a viewsets.ModelViewSet.
    Responsibility:
    """
    permission_classes = [
        # IsAuthenticated,
    ]
    queryset = AccountUser.objects.all()
    serializer_class = AccountUserSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        all_permissions = set(data.get('user_permissions', []))
        all_permissions.update([
            permission.id for permission in
            Permission.objects.filter(group__user=instance)])
        data['all_permissions'] = list(all_permissions)
        return Response(data)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# account_user_viewset.py ends here
