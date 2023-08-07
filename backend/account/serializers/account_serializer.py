#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""account_serializer -- account serializer

"""
from rest_framework import serializers

from django.conf import settings

class AccountUserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only=True,
        required=True,
        allow_null=False,
    )

    def create(self, validated_data):
        return AccountUser.objects.create_account(**validated_data)

    def update(self, instance, validated_data):
        passwd = validated_data.get('password', None)
        if passwd is None:
            return super(AccountUserSerializer, self).update(instance, validated_data)
        instance.set_password(passwd)
        instance.save()
        return instance

    class Meta:
        model = getattr(settings, "AUTH_USER_MODEL", "auth.User")
        fields = '__all__'



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# account_serializer.py ends here
