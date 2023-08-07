#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""settei_serializer --

"""
from rest_framework import serializers

from settei.models import SetteiModel


class SetteiSerializer(serializers.ModelSerializer):
    """SetteiSerializer

    SetteiSerializer is a serializers.ModelSerializer.
    Responsibility:
    """

    class Meta:
        model = SetteiModel
        fields = '__all__'



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# settei_serializer.py ends here
