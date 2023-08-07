#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: __init__.py


"""
from blog.views.category_viewset import CategoryViewset
from blog.views.post_viewset import PostViewset

__all__ = [
    'CategoryViewset',
    'PostViewset',
]



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
