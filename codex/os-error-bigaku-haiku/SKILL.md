---
name: os-error-bigaku-haiku
description: ターミナルやCLIでコマンド実行時にエラー（例: Permission denied, Segmentation fault, File not found等）が発生した際、自動的にエラー内容を和風俳句として表示し、元のエラーメッセージも併記します。エラー発生・明示呼び出し時に発動。
---

# 機能概要
このSkillは、ターミナルやコマンドラインで発生する無機質なエラーメッセージを、和風の俳句に変換して表示します。例えば "Permission denied" や "Segmentation fault" など、よくあるエラーを日本語の俳句（五・七・五調）に自動変換し、元のエラーメッセージとともに出力します。ミスやトラブルを文学的に味わい深い体験へと昇華し、開発者の心を和ませます。

# 使い方
- 明示呼び出し: `/skills os-error-bigaku-haiku` または `$ os-error-bigaku-haiku <コマンド>` でラップ実行
- 暗黙発動: ターミナルで "Permission denied", "Segmentation fault", "No such file or directory" などのエラーが発生したときに自動発動
- サブコマンド: `haiku-log` で過去の俳句エラー履歴を表示

# 出力例
```
$ os-error-bigaku-haiku ls /root
[和風エラー俳句]
Permission denied、心閉ざして、春霞
[元のエラー]
ls: cannot open directory '/root': Permission denied

$ os-error-bigaku-haiku cat missing.txt
[和風エラー俳句]
ファイル消え、探す手のひら、春の闇
[元のエラー]
cat: missing.txt: No such file or directory
```

# 注意点
- 俳句はエラー内容ごとに自動生成またはテンプレートから選択されます
- すべてのエラーに完全対応するわけではありません（未知のエラーは汎用俳句）
- ローカルにエラー履歴（俳句付き）を保存します。プライバシーに注意
- システムコマンドのラップ実行のみ対応。GUIアプリや外部プロセスは対象外

# 参考資料
- [Python subprocess 公式ドキュメント](https://docs.python.org/3/library/subprocess.html)
- references/design_notes.md 参照（俳句生成ロジック、設計方針、利用例など）