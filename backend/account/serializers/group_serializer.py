#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""group_serializer -- group serializer

"""
from rest_framework import serializers

from django.contrib.auth.models import Group

from .permission_serializer import PermissionSerializer


class GroupSerializer(serializers.ModelSerializer):
    """GroupSerializer

    GroupSerializer is a serializers.ModelSerializer.
    Responsibility:
    """
    permissions_display = PermissionSerializer(
        source="permissions",
        read_only=True,
        many=True,
    )

    class Meta:
        model = Group
        fields = '__all__'



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# group_serializer.py ends here
