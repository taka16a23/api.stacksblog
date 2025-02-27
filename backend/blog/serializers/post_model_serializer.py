#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""post_model_serializer --

"""
from django.utils import timezone
from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField

from blog.models.category_model import CategoryModel
from blog.models.post_model import PostModel
from blog.serializers.category_model_serializer import CategoryModelSerializer


class BasePostModelSerializer(serializers.ModelSerializer):
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


class PostModelSerializer(BasePostModelSerializer):
    """PostModelSerializer

    PostModelSerializer is a BasePostModelSerializer.
    Responsibility:
    """
    next = serializers.SerializerMethodField()
    prev = serializers.SerializerMethodField()

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
            'next',
            'prev',
        )

    def get_next(self, obj):
        next_post = PostModel.objects.filter(
            is_public=True,
            publish_date__gt=obj.publish_date,
            publish_date__lte=timezone.now(),
            is_draft=False,
        ).order_by('publish_date').first()
        return BasePostModelSerializer(next_post).data

    def get_prev(self, obj):
        prev_post = PostModel.objects.filter(
            is_public=True,
            publish_date__lt=obj.publish_date,
            is_draft=False,
        ).order_by('-publish_date').first()
        return BasePostModelSerializer(prev_post).data



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# post_model_serializer.py ends here
