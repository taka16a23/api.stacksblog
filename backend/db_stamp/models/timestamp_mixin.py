#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""timestamp_mixin -- 抽象タイムスタンンプモデル

抽象タイムスタンプモデルを定義

フィールド名などを変更する際は当モデルクラスを変更すること
継承して利用されることを想定している為、影響範囲を検討のこと

モデルクラス
    TimeStampMixin
    フィールド
        created_at
        modified_at
"""
from django.db import models
from django.utils.translation import gettext_lazy as _


class TimeStampMixin(models.Model):
    r"""TimeStampMixin

    TimeStampMixin is a models.Model.
    Responsibility: 作成日時、更新日時を定義する抽象モデル

    抽象モデル。 継承して利用されることを想定

    作成日時:
        DB レコード追加日時を保持
        DB Insert時に日時が追加され、以後更新されない
        すなわち、インスタンスを作成し保存した時点の日時を保持する
    更新日時:
        DB レコード更新日時を保持
        DB Update時に日時が更新される
        すなわち、インスタンスを取得し保存した時点の日時を保持する
    """
    class Meta:
        # 抽象モデルを有効化 マイグレーション対象外となる
        abstract = True

    # 作成日時
    created_at = models.DateTimeField(
        _('created_at'),
        # Insertの際に日時を自動登録
        auto_now_add=True,
        # null不許可
        null=False,
        # モデルフォーム上に表示しない
        editable=False,
    )
    # 更新日時
    modified_at = models.DateTimeField(
        _('modified_at'),
        # 追加、更新の際に日時を自動登録
        auto_now=True,
        # null不許可
        null=False,
        # モデルフォーム上に表示しない
        editable=False,
    )



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# timestamp_mixin.py ends here
