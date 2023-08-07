#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""category_viewset --

"""
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from blog.models.category_model import CategoryModel
from blog.serializers.category_model_serializer import CategoryModelSerializer


class CategoryViewset(viewsets.ModelViewSet):
    """CategoryViewset

    CategoryViewset is a viewsets.ModelViewSet.
    Responsibility:
    """
    permission_classes = [
        AllowAny
    ]

    http_method_names = ['get', ]

    queryset = CategoryModel.objects.all()
    serializer_class = CategoryModelSerializer
    filterset_fields = '__all__'



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# category_viewset.py ends here
