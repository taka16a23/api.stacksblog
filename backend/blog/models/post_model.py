#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""post_model --

"""
import logging
import inspect

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.core.validators import RegexValidator
from django.utils import timezone

from base.models.base_stamp_mixin import BaseStampMixin
from soft_delete.models.softdelete_mixin import SoftDeleteMixin
from blog.models.category_model import CategoryModel


class PostModel(BaseStampMixin, SoftDeleteMixin):
    """PostModel

    PostModel is a BaseStampMixin, SoftDeleteMixin.
    Responsibility:
    """
    # ID
    post_id = models.BigAutoField(_('ID'), primary_key=True)
    # タイトル
    title = models.CharField(
        _('Blog Title'),
        max_length=100,
        default='',
        null=False,
        blank=False,
        db_index=False,
        help_text=_('Ex. Python powered examples.'),
    )
    # 抜粋
    excerpt = models.TextField(
        u'記事の抜粋',
        default='',
        blank=True,
        null=False,
    )
    # slug
    slug = models.SlugField(
        null=False,
        unique=True,
    )
    # 画像
    image = models.ImageField(
        u'画像',
        upload_to='blog/',
        blank=True,
        null=True,
    )
    # 記事
    content = models.TextField(
        u'記事',
        default='',
        blank=True,
        null=False,
    )
    # カテゴリー
    category = models.ManyToManyField(
        CategoryModel,
        verbose_name=u'カテゴリー',
        blank=True,
        related_name="categories",
    )
    # 公開日時
    publish_date = models.DateTimeField(
        _('publish_date'),
        # null不許可
        null=False,
        blank=False,
        default=timezone.now(),
    )
    # 公開フラグ
    is_public = models.BooleanField(
        u'公開',
        null=False,
        blank=False,
        default=False,
    )
    # 下書きフラグ
    is_draft = models.BooleanField(
        u'下書き',
        null=False,
        blank=False,
        default=False,
    )

    class Meta:
        db_table = 'blog_posts'
        verbose_name = _('Blog Post')

    def __str__(self):
        logging.getLogger('blog').debug('Called {0.__class__.__name__}.{1}'.format(self, inspect.currentframe().f_code.co_name))
        return '{}:{}'.format(self.post_id, self.title)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# post_model.py ends here
