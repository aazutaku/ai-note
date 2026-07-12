# 概要
このSkillは、作業の合間やモチベーションに関するキーワード出現時に、OSの通知機能を使って“謎のOS偽モチベーション格言”をランダム表示するエンタメ系ツールです。日常の開発現場にちょっとした笑いや動揺をもたらします。

# 公式ドキュメント抜粋
- [plyer通知API](https://plyer.readthedocs.io/en/latest/)
- [notify2 (Linux)](https://pypi.org/project/notify2/)
- [Python random](https://docs.python.org/3/library/random.html)

# 利用例
- `python notifier.py notify` で即座に格言を通知
- `/random-os-motivational-quote-notifier` コマンドでAI経由実行
- チームでの朝会や進捗報告時のネタとして活用

# 注意点
- 通知はローカル環境に限定され、外部送信はありません
- OSごとに通知ライブラリが異なるため、事前に`pip install plyer notify2`等が必要
- 格言リストはスクリプト内で編集可能

# 設計方針
- OS判定によるクロスプラットフォーム対応
- 履歴ファイルによる通知記録（ホームディレクトリ直下）
- シンプルなCLIサブコマンド設計で導入・削除も容易