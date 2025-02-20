#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""list_post_ids_viewset --

"""
from django.contrib.auth import SESSION_KEY, BACKEND_SESSION_KEY, load_backend
from django.utils import timezone

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from blog.models.post_model import PostModel


class ListPostIdsViewset(APIView):
    permission_classes = [
        AllowAny
    ]

    def get(self, request, format=None):
        queryset = PostModel.objects.filter(is_public=True)
        if not self._has_session():
            queryset = PostModel.objects.filter(is_draft=False)
            queryset = queryset.filter(publish_date__lte=timezone.now())
        list_ids = queryset.values_list('post_id', flat=True)
        return Response(list_ids)

    def _has_session(self, ):
        user_id = self.request.session.get(SESSION_KEY, None)
        if user_id is None:
            return False
        backend_path = self.request.session.get(BACKEND_SESSION_KEY, None)
        if backend_path is None:
            return False
        backend = load_backend(backend_path)
        user = backend.get_user(user_id)
        if user is None:
            return False
        return True



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# list_post_ids_viewset.py ends here
