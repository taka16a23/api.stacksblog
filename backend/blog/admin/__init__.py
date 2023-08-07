#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: __init__.py


"""
from django.contrib import admin

from blog.models.category_model import CategoryModel
from blog.models.post_model import PostModel

from blog.admin.category_model_admin import CategoryModelAdmin
from blog.admin.post_model_admin import PostModelAdmin


__all__ = [
    'CategoryModelAdmin',
    'PostModelAdmin',
]

admin.site.register(CategoryModel, CategoryModelAdmin)
admin.site.register(PostModel, PostModelAdmin)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
