# 概要
このSkillは、CLIやターミナルで発生するエラーを、複数の“OS風”パロディメッセージにランダム変換することで、作業中のユーザーにユーモアと癒やしを提供します。エラー内容の本質は損なわず、元のメッセージも必ず併記する設計です。

# 公式ドキュメント抜粋
- Python例外: https://docs.python.org/ja/3/library/exceptions.html
- サブプロセス実行: https://docs.python.org/ja/3/library/subprocess.html

# 利用例
- `python random_os_error_translator.py simulate ls /root` で権限エラーをパロディ表示
- `translate "No such file or directory"` でメッセージ変換
- `log`, `list`, `summary` コマンドでエラー記録と集計

# 注意点
- 本Skillはジョーク用途です。実際のトラブルシュート時は元のエラーを参照してください。
- 致命的なシステムエラーは除外対象です。

# 設計方針
- OS風テンプレートは拡張容易なdict構造
- ログ機能はファイルベースでシンプルに実装
- サブコマンドで用途別に柔軟運用