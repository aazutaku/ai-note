# 概要
このSkillは、OSエラーやPython例外の無機質なメッセージを和風俳句に変換し、ユーザー体験をユーモラスにするために設計されています。主要なエラーごとに独自の俳句テンプレートを用意し、エラー発生時に即座に俳句として表示します。

# 公式ドキュメント抜粋
- Python例外: https://docs.python.org/3/library/exceptions.html
- subprocessモジュール: https://docs.python.org/3/library/subprocess.html

# 利用例
```bash
$ python os_error_bigaku_haiku.py run ls /root
[元エラー] ls: cannot open directory '/root': Permission denied
[俳句]
  Permission denied
          心閉ざして
          春霞
```

# 注意点
- すべてのエラーに完全対応しているわけではありません。
- 俳句はユーモア目的であり、実際のトラブルシュートには原文も参照してください。
- ログや履歴は保存しません。

# 設計方針
- 主要なエラータイプを独自に抽出し、テンプレートに基づき俳句を生成。
- subprocessで外部コマンドを安全に実行し、エラー時のみ俳句化。
- CLIサブコマンドで拡張性を確保。