#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""category_model --

"""
import logging
import inspect

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.core.validators import RegexValidator

from base.models.base_stamp_mixin import BaseStampMixin


class CategoryModel(BaseStampMixin):
    """CategoryModel

    Category is a BaseStampMixin.
    Responsibility:
    """
    # ID
    category_id = models.BigAutoField(_('ID'), primary_key=True)
    # カテゴリ名
    name = models.CharField(
        _('Category Name'),
        max_length=20,
        default='',
        null=False,
        blank=False,
        unique=True,
        db_index=False,
        help_text=_('Ex. Web'),
    )

    class Meta:
        db_table = 'blog_categories'
        verbose_name = _('Blog Category')

    def __str__(self):
        logging.getLogger('blog').debug('Called {0.__class__.__name__}.{1}'.format(self, inspect.currentframe().f_code.co_name))
        return '{}:{}'.format(self.category_id, self.name)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# category_model.py ends here
