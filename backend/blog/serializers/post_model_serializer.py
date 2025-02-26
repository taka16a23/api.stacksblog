#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""post_model_serializer --

"""
from rest_framework import serializers

from blog.models.category_model import CategoryModel
from blog.models.post_model import PostModel
from blog.serializers.category_model_serializer import CategoryModelSerializer


class PostModelSerializer(serializers.ModelSerializer):
    """PostModelSerializer

    PostModelSerializer is a serializers.Model.
    Responsibility:
    """
    category_display = CategoryModelSerializer(
        source='category',
        read_only=True,
        many=True,
        allow_null=True,
    )

    class Meta:
        model = PostModel
        fields = (
            'post_id',
            'title',
            'excerpt',
            'slug',
            'image',
            'content',
            'category_display',
            'publish_date',
        )



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# post_model_serializer.py ends here
