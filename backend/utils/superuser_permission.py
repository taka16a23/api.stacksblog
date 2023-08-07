#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""SuperUserPermission -- Super User Permission

"""
from rest_framework.permissions import IsAdminUser

class SuperUserPermission(IsAdminUser):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# SuperUserPermission.py ends here
