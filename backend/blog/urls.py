#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""urls -- define urls for messages

"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from blog import views


router = DefaultRouter()
router.register(r'category', views.CategoryViewset)
router.register(r'post', views.PostViewset)

urlpatterns = router.urls



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# urls.py ends here
