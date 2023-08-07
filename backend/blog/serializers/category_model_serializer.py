#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""category_model_serializer --

"""
from rest_framework import serializers

from blog.models.category_model import CategoryModel


class CategoryModelSerializer(serializers.ModelSerializer):
    """CategoryModelSerializer

    CategoryModelSerializer is a serializers.ModelSerializer, UserStampSerializerMixin.
    Responsibility:
    """

    class Meta:
        model = CategoryModel
        fields = '__all__'



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# category_model_serializer.py ends here
