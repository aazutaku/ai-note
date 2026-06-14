---
name: random-os-error-poetry
description: コマンド実行やファイル操作などで発生したOSエラー（例: PermissionError, FileNotFoundError, OSError）を検知した際、自動的に詩的なエラーメッセージへ変換して表示します。エラー発生時や'/random-os-error-poetry'明示呼び出しで発動します。
---

# 機能概要
`random-os-error-poetry`は、ターミナルやエディタ上でコマンド実行時に発生する各種OSエラー（ファイル未発見、パーミッション拒否、I/Oエラーなど）を検知し、その内容を重厚な詩へと即興変換して表示するスキルです。従来の味気ないエラーメッセージを、思わず笑ってしまう壮大なポエムに変換することで、作業中のストレスや疲労を和らげます。真面目な開発現場にユーモアと創造性をもたらし、エラー内容の本質も詩的に伝達します。

# 使い方
- 明示呼び出し例: `/random-os-error-poetry "PermissionError: [Errno 13] Permission denied: '/etc/passwd'"`
- 暗黙発動キーワード例: `PermissionError`, `FileNotFoundError`, `OSError`, `No such file or directory`, `IsADirectoryError` などのエラー発生時に自動発動します。

# 出力例
```
$ python script.py
許されぬ権限よ、我が手にパーミッションを。
閉ざされた門の向こうに、/etc/passwdの夢。
[原文: PermissionError: [Errno 13] Permission denied: '/etc/passwd']

$ cat missing.txt
見つからぬ道、404の黄昏。
失われしファイル、missing.txtは幻。
[原文: FileNotFoundError: [Errno 2] No such file or directory: 'missing.txt']
```

# 注意点
- 本SkillはOSエラー例外のみを対象とし、SyntaxErrorやネットワーク系エラー等は詩化しません。
- 原文エラーメッセージも併記されるため、実際のトラブルシュートを妨げません。
- 詩の生成はランダム性を含むため、同じエラーでも毎回異なる表現になる場合があります。
- ローカルファイル等への自動保存は行いません。

# 参考資料
本SkillはPythonの組み込み例外クラス（[OSError](https://docs.python.org/ja/3/library/exceptions.html#OSError)等）を対象としています。詩的変換ロジックや設計方針の詳細は`references/design_notes.md`を参照してください。