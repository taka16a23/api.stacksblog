#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""userstamp_mixin -- 抽象ユーザースタンンプモデル

抽象ユーザースタンプモデルを定義

フィールド名などを変更する際は当モデルクラスを変更すること
継承して利用されることを想定している為、影響範囲を検討のこと

モデルクラス
    UserStampMixin
    フィールド
         created_by
         modified_by
"""
from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserStampMixin(models.Model):
    """UserStampMixin

    UserStampMixin is a models.Model.
    Responsibility: 作成者、更新者を定義する抽象モデル

    抽象モデル。 継承して利用されることを想定

    作成者:
        DB レコード追加時のユーザーを登録
        DB Insert時にユーザーが追加される
        すなわち、インスタンスを作成し保存した時点のユーザーを保持する
    更新者:
        DB レコード更新時のユーザーを登録
        DB Update時にユーザーが更新される
        すなわち、インスタンスを取得し保存した時点のユーザーを保持する
    """
    class Meta:
        # 抽象モデルを有効化 マイグレーション対象外となる
        abstract = True

    # 作成者
    created_by = models.ForeignKey(
        # ログインユーザーモデル
        getattr(settings, "AUTH_USER_MODEL", "auth.User"),
        on_delete=models.SET_DEFAULT,
        default=None,
        verbose_name=_('created_by'),
        null=True,
        # 逆引用 外部キーモデルから当モデルを取得する為
        related_name='%(app_label)s_%(class)s_created_by',
        db_column='created_by'
    )
    # 更新者
    modified_by = models.ForeignKey(
        # ログインユーザーモデル
        getattr(settings, "AUTH_USER_MODEL", "auth.User"),
        on_delete=models.SET_DEFAULT,
        default=None,
        verbose_name=_('modified_by'),
        null=True,
        # 逆引用 外部キーモデルから当モデルを取得する為
        related_name='%(app_label)s_%(class)s_modified_by',
        db_column='modified_by'
    )

    def set_user(self, user):
        """指定されたユーザーを作成者、更新者にセットする

        既に作成者がある場合は作成者は更新しない

        set_user(user)

        @Arguments:
        - `user`: settings.AUTH_USER_MODEL のユーザーモデル

        @Return: None

        @Error:
        """
        # require
        if user is None:
            return
        # 作成者がセットされてなければ
        if self.created_by is None:
            self.created_by = user
        # 更新者をセット
        self.modified_by = user



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# userstamp_mixin.py ends here
