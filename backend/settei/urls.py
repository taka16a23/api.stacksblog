#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""urls --

"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from settei import views


router = DefaultRouter()
router.register(r'settei', views.SetteiViewSet)

urlpatterns = router.urls



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# urls.py ends here
