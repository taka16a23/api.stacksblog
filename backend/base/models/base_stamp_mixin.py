#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""base_stamp_mixin -- 規定スタンプモデル

抽象スタンプモデルを定義

クラス
    BaseStampMixin
"""
from db_stamp.models.timestamp_mixin import TimeStampMixin
from db_stamp.models.userstamp_mixin import UserStampMixin


class BaseStampMixin(TimeStampMixin, UserStampMixin):
    """BaseStampMixin

    BaseStampMixin is a TimeStampMixin, UserStampMixin.
    Responsibility: タイムスタンプとユーザースタンプを定義する抽象モデル

    抽象モデル。 継承して利用されることを想定

    作成日時:
        DB レコード追加日時を保持
        DB Insert時に日時が追加され、以後更新されない
        すなわち、インスタンスを作成し保存した時点の日時を保持する
    更新日時:
        DB レコード更新日時を保持
        DB Update時に日時が更新される
        すなわち、インスタンスを取得し保存した時点の日時を保持する
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



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# base_stamp_mixin.py ends here
