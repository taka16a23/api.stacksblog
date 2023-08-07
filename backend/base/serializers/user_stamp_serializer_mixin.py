#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""user_stamp_serializer_mixin -- user stamp serializer mixin

"""
from rest_framework import serializers

from account.serializers.account_serializer import AccountUserSerializer


class UserStampSerializerMixin(metaclass=serializers.SerializerMetaclass):
    created_by_display = AccountUserSerializer(
        source="created_by",
        read_only=True,
    )

    modified_by_display = AccountUserSerializer(
        source="modified_by",
        read_only=True,
    )




# For Emacs
# Local Variables:
# coding: utf-8
# End:
# user_stamp_serializer_mixin.py ends here
