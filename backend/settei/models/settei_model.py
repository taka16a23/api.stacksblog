#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""settei_model --

"""
import logging
import inspect

from django.db import models
from django.utils.translation import ugettext, ugettext_lazy as _

from base.models.base_stamp_mixin import BaseStampMixin


class SetteiModel(BaseStampMixin):
    """SetteiModel

    SetteiModel is a BaseStampMixin.
    Responsibility:

    | Physical Name | type     | size | NN | PK | FK | IDX | default | description |
    | id            | bigint   |      |    | Y  |    |     |         |             |
    | setteimei     | nvarchar |   64 | Y  |    |    |     |         | unique制約  |
    | setteichi     | text     |      | Y  |    |    |     | '’     |             |
    | created_at    | datetime |      | Y  |    |    |     | now()   |             |
    | created_by    | int      |      |    |    |    |     |         |             |
    | modified_at   | datetime |      | Y  |    |    |     | now()   |             |
    | modified_by   | int      |      |    |    |    |     |         |             |
    """
    #1. ID
    id = models.BigIntegerField(_('ID'), primary_key=True)
    #2. 設定名
    setteimei = models.CharField(
        _('Setting Name'),
        max_length=64,
        null=False,
        blank=False,
        unique=True,
        db_index=False,
    )
    #3. 設定値
    setteichi = models.TextField(
        _('Setting Value'),
        default='',
        null=False,
        blank=True,
    )

    class Meta:
        db_table = 's_settei'
        verbose_name = _('Setting')

    def __str__(self):
        logging.getLogger('settei').debug('Called {0.__class__.__name__}.{1}'.format(self, inspect.currentframe().f_code.co_name))
        return '{}:{}'.format(self.id, self.setteimei)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# settei_model.py ends here
