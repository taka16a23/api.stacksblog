#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""softdelete_manager -- 論理削除用のカスタムマネージャー

"""
from django.db import models

from .softdelete_queryset import SoftDeleteQuerySet


class SoftDeleteManager(models.Manager):
    """SoftDeleteManager

    SoftDeleteManager is a models.Manager.
    Responsibility:
    """
    def __init__(self, *args, **kwargs):
        """

        @Arguments:
        - `args`:
        - `kwargs`:
        """
        self.alive_only = kwargs.pop('alive_only', True)
        super(SoftDeleteManager, self).__init__(*args, **kwargs)

    def get_queryset(self, ):
        """クエリセットを返却

        get_queryset()

        alive_only プロパティがTrueなら論理削除されていないデータを取得

        @Return: クエリセットを返却
        """
        # if self.alive_only == True:
            # return SoftDeleteQuerySet(self.model).filter(deleted_at=None)
        return SoftDeleteQuerySet(self.model)

    def hard_delete(self, ):
        """物理削除クエリセットを取得

        hard_delete()

        @Return:
        """
        # require
        return self.get_queryset().hard_delete()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# softdelete_manager.py ends here
