#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""post_viewset --

"""
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from blog.models.post_model import PostModel
from blog.serializers.post_model_serializer import PostModelSerializer


class PostViewset(viewsets.ModelViewSet):
    """PostViewset

    PostViewset is a viewsets.ModelViewSet.
    Responsibility:
    """
    permission_classes = [
        AllowAny
    ]

    http_method_names = ['get', ]

    queryset = PostModel.objects.all()
    serializer_class = PostModelSerializer
    filterset_fields = ['slug', 'content', 'category']



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# post_viewset.py ends here
