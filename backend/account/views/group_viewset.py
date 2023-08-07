#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""group_viewset -- group view

"""
from django.contrib.auth.models import Group
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from account.serializers.group_serializer import GroupSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """GroupViewSet

    GroupViewSet is a viewsets.ModelViewSet.
    Responsibility:
    """
    permission_classes = [
        # IsAuthenticated,
    ]
    queryset = Group.objects.all()
    serializer_class = GroupSerializer



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# group_viewset.py ends here
