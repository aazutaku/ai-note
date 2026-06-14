---
name: random-os-error-poetry
description: Antigravity でコマンド実行やファイル操作時に 'Permission denied' や 'File not found' などの典型的なOSエラーが発生した際、自動で詩的なメッセージに変換して表示するSkillです。エラー内容のキーワード検出時に発動します。
---

# 機能概要
random-os-error-poetry は、ターミナルやエディタで頻出するOSエラー（例: Permission denied, No such file or directory, File exists, Is a directory など）を検知すると、そのエラーメッセージを重厚かつユーモラスな詩に即興変換して表示します。作業中の苛立ちや疲労を和らげるため、厳しいエラーも思わず笑ってしまうポエムに変身。通常のエラー出力も参照可能なため、デバッグや作業効率を損なうことなく、気分転換やチームの雰囲気づくりに役立ちます。

# 使い方
このSkillは明示的な呼び出しは不要です。Antigravity上でコマンド実行時やファイル操作時に、エラーメッセージ（例: 'Permission denied', 'No such file or directory', 'Is a directory', 'File exists', 'Not a directory', 'Connection refused' など）を検出すると自動発動します。暗黙発動キーワード例: 'permission', 'not found', 'refused', 'directory', 'exists'。

# 出力例
```
$ cat secret.txt
cat: secret.txt: Permission denied
---
許されぬ権限よ、我が手にパーミッションを。
閉ざされた扉の向こうに、静かなるファイルは眠る。
（原文: Permission denied）

$ ls /notfound
ls: cannot access '/notfound': No such file or directory
---
見つからぬ道、404の黄昏。
ファイルの幻影は、虚空に消えゆく。
（原文: No such file or directory）
```

# 注意点
- 原文エラーも併記されるため、通常のデバッグ作業を妨げません。
- 変換は主要な英語エラーのみ対応。ローカル保存や履歴管理は行いません。
- システムクリティカルなエラーや非OS系例外は除外されます。

# 参考資料
- [Python 標準エラー一覧](https://docs.python.org/ja/3/library/exceptions.html)
- references/design_notes.md も参照してください。