#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""softdelete_mixin -- 抽象論理削除モデル

抽象論理削除モデル

フィールド名などを変更する際は当モデルクラスを変更すること
継承して利用されることを想定している為、影響範囲を検討のこと

モデルクラス
    SoftDeleteMixin
    フィールド
        deleted_at
"""
from django.db import models
from django.utils.translation import gettext_lazy as _
from .softdelete_manager import SoftDeleteManager
from soft_delete.models.datetimeflag_field import DateTimeFlagField


class SoftDeleteMixin(models.Model):
    """SoftDeleteMixin

    SoftDeleteMixin is a models.Model.
    Responsibility: 論理削除日を定義する抽象モデル

    抽象モデル。 継承して利用されることを想定

    削除日時:
        論理削除日を保持
        None(Null) なら未削除、否で日時があれば削除
    """
    class Meta:
        # 抽象モデルを有効化 マイグレーション対象外となる
        abstract = True

    objects = SoftDeleteManager(alive_only=True)

    deleted_at = DateTimeFlagField(_('Deleted'), blank=True, null=True, )

    @property
    def is_deleted(self, ):
        """Check deleted.

        is_deleted()

        @Return:

        @Error:
        """
        if self.deleted_at is None:
            return False
        return True



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# softdelete_mixin.py ends here
