---
name: random-os-error-translator
description: CodexがターミナルやCLIでエラー発生時、または'/skills menu'や'skill名'で明示呼び出されたときに発動。エラーメッセージを複数の“別OS風”パロディに変換し、元の内容も簡単に参照可能です。
---

# 機能概要
このSkillは、コマンドラインやターミナルで発生したエラーメッセージを、毎回異なる“架空または実在OS風”のパロディメッセージに変換して表示します。例えば「Permission denied」という標準的なエラーが、「このファイルは神聖にして侵入を禁ず（MS-DOS風）」や「推奨されていない操作です（国産OS風）」など、意味不明かつユーモラスな表現に変換されます。作業中のストレスを和らげ、日常のCLI作業にカオスで楽しい演出を加えます。

# 使い方
- 明示呼び出し例: `/skills menu` でスキル一覧から選択、または `random-os-error-translator` を直接呼び出し
- 暗黙発動キーワード例: `error`, `failed`, `Exception`, `Permission denied`, `command not found` など、エラー発生時に自動で発動

# 出力例
```
$ ls /root
[AmigaOS風] 申し訳ありません、この命令は神の領域です。
(元のエラー: Permission denied)

$ cat notfound.txt
[国産OS風] ファイルが見つかりませんでした。再起動を推奨します。
(元のエラー: No such file or directory)

$ rm /dev/null
[MS-DOS風] システムが混乱しました。操作は許可されません。
(元のエラー: Operation not permitted)
```

# 注意点
- OS風変換は完全なジョークであり、実際のエラー内容の正確な説明ではありません。
- 元のエラー内容も必ず併記されるため、トラブルシュートは可能です。
- ローカルファイルやシステムには一切変更を加えません。
- 除外パス: システム管理系・セキュリティ関連の致命的エラーには変換を適用しません。

# 参考資料
- references/design_notes.md に設計方針や利用例を記載
- 公式Pythonドキュメント: https://docs.python.org/ja/3/library/exceptions.html
- CLIエラー例: https://wiki.archlinux.jp/index.php/Errors_and_troubleshooting