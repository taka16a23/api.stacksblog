#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""token_obtainpair_view -- token obtain pair

"""
from django.contrib.auth.models import update_last_login
from rest_framework_simplejwt.views import TokenObtainPairView as _TokenObtainPairView

from account.models import AccountUser


class TokenObtainPairView(_TokenObtainPairView):
    """TokenObtainPairView

    TokenObtainPairView is a _TokenObtainPairView.
    Responsibility:
    """
    def post(self, request, *args, **kwargs):
        result = super(TokenObtainPairView, self).post(request, *args, **kwargs)
        try:
            email = request.data.get('email', None)
            if email is None:
                return result
            user = AccountUser.objects.get(email=email)
            update_last_login(None, user)
        except Exception as exc:
            pass
        return result



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# token_obtainpair_view.py ends here
