# 概要
このSkillは、OSエラー発生時の無機質なメッセージを和風俳句に変換し、開発者のストレスを和らげることを目的としています。エラー内容ごとに異なる俳句を返すことで、単調なエラー体験を“文学的”に変換します。

# 公式ドキュメント抜粋
Pythonの組み込み例外やOSエラーについては、[Python公式ドキュメント](https://docs.python.org/ja/3/library/exceptions.html)を参照してください。

# 利用例
- `python os_error_bigaku_haiku.py run --simulate "Permission denied: '/etc/shadow'"`
- `ls /root | python os_error_bigaku_haiku.py run --stdin`

# 注意点
- すべてのエラーに俳句が割り当てられるわけではありません。未知のエラーはデフォルト俳句で対応します。
- 本Skillはジョーク・パロディ用途です。実際のエラー解析やトラブルシューティングには公式ドキュメントやログを参照してください。

# 設計方針
- 実在のエラーパターンに正規表現でマッチし、対応する俳句を返す方式。
- CLIサブコマンドや標準入力対応で柔軟に利用可能。
- 外部依存を極力排除し、ローカルで完結する設計としています。