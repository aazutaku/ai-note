# 概要
`random-os-error-poetry`は、OSエラーを詩的かつユーモラスに変換することで、開発現場の雰囲気を和らげることを目的としています。主にPythonの標準例外（PermissionError, FileNotFoundError, OSError等）を対象にしています。

# 公式ドキュメント抜粋
- [Python 組み込み例外](https://docs.python.org/ja/3/library/exceptions.html)
- [OSError](https://docs.python.org/ja/3/library/exceptions.html#OSError)

# 利用例
- ターミナルやエディタでコマンド失敗時の出力を詩化。
- `/random-os-error-poetry "FileNotFoundError: [Errno 2] No such file or directory: 'foo.txt'"` のように明示呼び出し。
- `--log`で履歴保存、`--list`で詩化エラー一覧、`--summary`で統計表示。

# 注意点
- エラー原文も必ず併記されるため、詩化による情報損失はありません。
- 詩のテンプレートはランダム選択され、同じエラーでも多様な表現が楽しめます。
- ネットワークエラーや構文エラー等、OS例外以外は対象外です。

# 設計方針
例外ごとに複数の詩的テンプレートを用意し、エラー発生時にパス等の情報を埋め込んで即興詩を生成します。CLIサブコマンドで履歴や統計も管理でき、日々の開発に遊び心を提供します。