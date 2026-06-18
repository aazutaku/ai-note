---
name: random-os-error-kaiseki
description: コマンド実行時にエラーが発生した場合、このSkillは自動的に“OS風カタカナ専門用語”による意味不明なエラー解説をデスクトップ通知で強制表示します。trigger: error, exception, コマンド失敗, /random-os-error-kaiseki。
---

# 機能概要
このSkillは、コマンドやスクリプトの実行時にエラーが発生した際、通常のエラーメッセージに代えて“OS風・謎のカタカナ専門用語”による意味不明なエラー解説をデスクトップ通知で強制表示します。例えば「パケット・シンフォニーがバッファ・カタストロフを検出しました」「デジタル・アンビエントがオーバーフローしました」など、技術者っぽいのに全く意味が通じない迷文が毎回ランダム生成されます。開発現場のバグ疲れをカタカナギャグで強制リフレッシュし、異常時の雰囲気を和らげます。

# 使い方
- 明示呼び出し: `/random-os-error-kaiseki` を実行すると、直近のエラー内容をカタカナ解説付きで通知します。
- 暗黙発動: コマンド実行時に `error`, `exception`, `失敗`, `traceback` などのキーワードを含む出力が発生した場合、自動的にSkillが発動し、通知が表示されます。

# 出力例
```
$ python sample_script.py
Traceback (most recent call last):
  File "sample_script.py", line 2, in <module>
    1/0
ZeroDivisionError: division by zero
[通知] パケット・シンフォニーがバッファ・カタストロフを検出しました

$ /random-os-error-kaiseki
[通知] デジタル・アンビエントがオーバーフローしました
```

# 注意点
- 通知はローカル環境のデスクトップ通知機能を利用します（Linux: notify-send, macOS: osascript, Windows: win10toast等）。
- 本来のエラー内容は通知とは別に標準出力やログで確認できます。
- カタカナ解説は毎回ランダム生成されますが、実際のエラー内容とは無関係です。
- サーバ環境や通知非対応端末では動作しません。

# 参考資料
- references/design_notes.md
- https://docs.python.org/3/library/subprocess.html
- https://pypi.org/project/win10toast/