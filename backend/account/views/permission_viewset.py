#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""permission_viewset -- permission viewset

"""
from django.contrib.auth.models import Permission
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from account.serializers.permission_serializer import PermissionSerializer


class PermissionViewSet(viewsets.ModelViewSet):
    """PermissionsViewSet

    PermissionsViewSet is a viewsets.ModelViewSet.
    Responsibility:
    """
    permission_classes = [
        # IsAuthenticated,
    ]
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# permission_viewset.py ends here
