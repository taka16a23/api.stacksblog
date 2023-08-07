#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""softdelete_queryset -- 論理削除QuerySet

論理削除用のクエリセットを定義

フィールド名などを変更する際は当モデルクラスを変更すること

クラス
    SoftDeleteQuerySet
    Method:
        delete:
            論理削除クエリを返却
        hard_delete:
            物理削除クエリを返却
        only_alive
            論理削除されていないもののみを絞り込むクエリを返却
        only_deleted
            論理削除されたデータのみを絞り込むクエリを返却
"""
from django.db.models.query import QuerySet
from django.utils import timezone


class SoftDeleteQuerySet(QuerySet):
    """SoftDeleteQuerySet

    SoftDeleteQuerySet is a QuerySet.
    Responsibility: 論理削除用のクエリセットを生成

    Method:
        delete:
            論理削除クエリを返却
        hard_delete:
            物理削除クエリを返却
        only_alive
            論理削除されていないもののみを絞り込むクエリを返却
        only_deleted
            論理削除されたデータのみを絞り込むクエリを返却
    """
    def delete(self, ):
        """論理削除クエリを返却

        deleted_at フィールドに日時をセットするクエリを返却

        delete()

        @Return:
        クエリセットを返却
        """
        return super(SoftDeleteQuerySet, self).update(deleted_at=timezone.now())

    def hard_delete(self, ):
        """物理削除クエリを返却

        hard_delete()

        @Return:
        クエリセットを返却
        """
        return super(SoftDeleteQuerySet, self).delete()

    def only_alive(self, ):
        """論理削除されていないもののみを絞り込むクエリを返却

        deleted_at フィールドにNullがセットされているもののみを取得するクエリ
        を返却

        only_alive()

        @Return:
        クエリセットを返却
        """
        return self.filter(deleted_at=None, )

    def only_deleted(self, ):
        """論理削除されたデータのみを絞り込むクエリを返却

        only_deleted()

        deleted_at フィールドにNullがセットされていないもののみを取得するクエリ
        を返却
        @Return:
        クエリセットを返却
        """
        return self.exclude(deleted_at=None, )



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# softdelete_queryset.py ends here
