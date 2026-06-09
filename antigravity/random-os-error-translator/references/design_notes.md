# 概要
このSkillは、実際のOSエラーメッセージを複数の“OS風”パロディにランダム変換することで、日常的なコマンドライン作業にユーモアを加えることを目的としています。

# 公式ドキュメント抜粋
Pythonの例外一覧や標準エラー出力の扱いについては、[Python公式ドキュメント](https://docs.python.org/ja/3/library/exceptions.html)を参照してください。subprocess.runや例外ハンドリングの標準APIを利用しています。

# 利用例
- `python random_os_error_translator.py simulate --type permission` で疑似PermissionErrorを発生
- `python random_os_error_translator.py wrap "ls /notfound"` でコマンドのエラーを変換

# 注意点
このSkillは実際のエラー内容をパロディ変換するため、障害対応や業務用途には不向きです。元のエラーも必ず併記し、ユーザーが本来の原因を見失わないよう配慮しています。

# 設計方針
- OS風パターンは拡張容易なリスト構造で管理
- 例外発生時・コマンド失敗時の両方に対応
- 毎回ランダムな演出で飽きさせない設計
- 元のエラー内容も必ず表示し、実用性を損なわない