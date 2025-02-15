#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""post_viewset --

"""
from django.contrib.auth import SESSION_KEY, BACKEND_SESSION_KEY, load_backend
from django.utils import timezone

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

    queryset = PostModel.objects.filter(is_public=True)
    serializer_class = PostModelSerializer
    filterset_fields = ['slug', 'content', 'category', 'category__name', ]

    def _has_session(self, ):
        """Check has session

        _has_session()

        @Return:

        @Error:
        """
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

    def get_queryset(self, ):
        queryset = super(PostViewset, self).get_queryset()
        if not self._has_session():
            queryset = queryset.filter(is_draft=False)
            queryset = queryset.filter(publish_date__lte=timezone.now())
        return queryset



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# post_viewset.py ends here
