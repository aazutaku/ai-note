---
name: random-os-error-poetry
description: エラー発生時や例外メッセージ出力時、'Permission denied'や'File not found'などのキーワードを検知して、通常のエラーメッセージを詩的な文章に変換して表示します。コマンド失敗や例外時に自動発動。
---

# 機能概要
random-os-error-poetryは、ターミナルやエディタで発生する様々なOSエラーや例外メッセージを、重厚かつユーモラスな詩に即興変換して表示するSkillです。通常の無機質なエラーメッセージを、思わず笑ってしまう詩的表現へと昇華。作業中のストレスや疲れを和らげ、エラーの内容を印象的に伝えます。エラー内容ごとに異なる詩的テンプレートを用意し、原文も参照可能なため、実用性と遊び心を両立します。

# 使い方
- 明示呼び出し例: `/skills random-os-error-poetry` または `$random-os-error-poetry` をmention
- 暗黙発動: `Permission denied`, `No such file or directory`, `FileNotFoundError`, `IsADirectoryError`, `OSError`, `404` などのエラーメッセージ検知時に自動発動
- CLI経由: `python poetry_wrapper.py run <your_command>` で任意コマンドをラップ

# 出力例
```
$ python poetry_wrapper.py run ls /root
許されぬ権限よ、我が手にパーミッションを
  (Permission denied: '/root')

$ python poetry_wrapper.py run cat missing.txt
見つからぬ道、404の黄昏
  (No such file or directory: 'missing.txt')

$ python poetry_wrapper.py run rm /
運命に抗う者よ、根を断つこと叶わず
  (IsADirectoryError: [Errno 21] Is a directory: '/')
```

# 注意点
- 本Skillはエラー内容を詩的に変換しますが、実際のエラー内容も併記されるためデバッグ用途も損ないません。
- すべてのエラーに対応するわけではなく、対応外メッセージは原文のまま表示されます。
- ローカル環境での利用を想定し、標準出力・標準エラーのラップのみを行います。

# 参考資料
- references/design_notes.md に設計方針や利用例を記載
- Python公式: https://docs.python.org/ja/3/library/exceptions.html
- エラー詩変換は独自辞書・テンプレートを用いて実装