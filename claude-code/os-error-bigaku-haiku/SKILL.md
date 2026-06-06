---
name: os-error-bigaku-haiku
description: ターミナルやCLIでコマンド実行時にOSエラー（例: Permission denied, File not found, Segmentation fault等）が発生した際、そのエラー内容を和風俳句に変換し、元のエラーとともに表示するSkill。エラー発生時・明示コマンド呼び出し時に発動。
---

# 機能概要
このSkillは、ターミナルやCLIでコマンド実行時に発生する無機質なOSエラーメッセージ（例: Permission denied, File not found, Segmentation faultなど）を、和風の俳句に変換して表示します。エラー内容ごとに異なる俳句が自動生成され、元のエラーメッセージも併記されるため、トラブル発生時も思わず笑ってしまう“文学的体験”が得られます。日々の開発や運用でのストレスを和らげ、エラーを楽しむ新しい視点を提供します。

# 使い方
- 明示呼び出し例: `/os-error-bigaku-haiku "Permission denied: '/etc/shadow'"`
- 暗黙発動キーワード例: コマンド実行時に "Permission denied", "No such file or directory", "Segmentation fault" などのOSエラーが発生した場合、自動で俳句が表示されます。
- CLIとしては `python os_error_bigaku_haiku.py run --simulate 'File not found: /tmp/data.txt'` などで利用可能です。

# 出力例
```
[OS Error Haiku]
元メッセージ: Permission denied: '/etc/shadow'
俳句:  
扉閉ざす  
許されぬ道  
春霞

[OS Error Haiku]
元メッセージ: Segmentation fault (core dumped)
俳句:  
記憶の彼方  
断絶の響き  
絶望感
```

# 注意点
- すべてのOSエラーが俳句化されるわけではなく、主要なエラー種別に対応しています。
- ローカル端末でのみ動作し、外部APIやネットワークアクセスは不要です。
- 生成された俳句やエラー履歴はファイル保存されません。
- 本Skillはジョーク用途であり、実運用でのエラー解析には向きません。

# 参考資料
- references/design_notes.md を参照
- Python公式: https://docs.python.org/ja/3/library/exceptions.html
- 俳句生成ロジックやエラー分類の詳細も同リファレンスに記載