#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""urls -- account urls define

"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from account import views

router = DefaultRouter()
router.register(r'account', views.AccountUserViewSet)
router.register(r'search/simple/account', views.AccountUserSimpleViewSet)
router.register(r'permission', views.PermissionViewSet)
router.register(r'group', views.GroupViewSet)

urlpatterns = router.urls
urlpatterns += [
    path('loginuser/', views.LoginUserView.as_view()),
]



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# urls.py ends here
