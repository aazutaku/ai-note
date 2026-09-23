# 概要
このSkillは、開発者の作業フロー中に突如現れる“無意味な古文書通知”を巻物風UIで表示する、完全エンタメ志向の演出用ツールです。通知文は複数セクションからランダムに組み合わせて生成され、毎回異なる内容となるよう設計されています。

# 設計方針
- 実用性よりも“集中力ブレイカー”としての破壊力を優先。
- テキストベースの巻物UIは、ターミナルでの再現性と汎用性を重視。
- 通知文は3セクション構成とし、古文書・占い・OS擬人化などの要素を盛り込む。
- ログ保存や履歴参照もCLIサブコマンドでサポート。

# 利用例
- コマンド: `python random_scroll_alert.py show` で即時通知。
- ログ追記: `python random_scroll_alert.py log --logfile myscroll.log`
- 履歴参照: `python random_scroll_alert.py list --count 3`

# 公式ドキュメント抜粋
- Python random: https://docs.python.org/ja/3/library/random.html
- argparse: https://docs.python.org/ja/3/library/argparse.html

# 注意点
- 実務的な通知や警告は一切含まれません。
- GUI通知やOSネイティブ連携は未対応（拡張可）。
- ログファイルはユーザーが明示的に指定した場合のみ保存されます。