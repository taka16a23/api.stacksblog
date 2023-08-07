#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""auth_permission_serializer -- auth permission serializer

"""
from django.contrib.auth.models import Permission
from rest_framework import serializers


class PermissionSerializer(serializers.ModelSerializer):
    """PermissionsSerializer

    PermissionsSerializer is a serializers.ModelSerializer.
    Responsibility:
    """
    class Meta:
        model = Permission
        fields = '__all__'



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# auth_permission_serializer.py ends here
