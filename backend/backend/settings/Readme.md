# 設定

### ■ 設定ファイル(backend/backend/settings)
+ パスワードなどはS90_local.pyに記載しリビジョン管理対象外とすること
+ S90_local.pyはサンプルファイルを実行し作成すること

| ファイル名              | 概要                     |
|--|--|
| S10_const.py             | 定数定義ファイル         |
| S20_international        | 言語、通貨、時間単位設定 |
| S21_path.py             | ディレクトリ、ファイルパス設定関係 |
| S30_security.py         | セキュリティ関連設定 |
| S40_app.py              | アプリケーション設定関係 |
| S50_database.py         | データベース関係設定 |
| S51_templates.py        | テンプレート関係設定 |
| S60_email.py            | メール設定 |
| S70_misc.py             | その他設定        |
| S80_logging.py          | ログ設定関係       |
| S90_local.py            | ローカル環境設定    |
| sample_develop_local.py | 開発環境設定サンプル |
| sample_product_local.py | 本番環境設定サンプル |
