#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""settei_viewset --

"""
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from settei.models import SetteiModel
from settei.serializers import SetteiSerializer


class SetteiViewSet(viewsets.ModelViewSet):
    """SetteiViewSet

    SetteiViewSet is a viewsets.ModelViewSet.
    Responsibility:
    """
    permission_classes = [
        # IsAuthenticated,
    ]
    queryset = SetteiModel.objects.all()
    serializer_class = SetteiSerializer



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# settei_viewset.py ends here
