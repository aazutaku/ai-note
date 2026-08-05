---
name: random-os-fake-ai-takeover-alert
description: Claude Codeがユーザーの作業中やコマンド実行時（例: build, test, run, edit, terminal, shell, code, project, os, notification, prank, alert, warning）に、OS風のAIジャック警告をランダムな内容・タイミングでデスクトップ通知として表示したい場合に発動します。
---

# 機能概要
このSkillは、普段の作業中に“AIによるOSジャック”をテーマにした偽の警告通知を、デスクトップにランダムで表示します。通知内容は毎回異なり、「AIがOS制御権を取得」「カーネル領域がAIにより再編成」など、現実ではあり得ないカオスなメッセージを生成。作業現場やチーム内での話題作り、リフレッシュ、あるいはちょっとしたジョーク用途に最適です。真面目な雰囲気に突如“人類ピンチ感”を演出し、周囲の注目を集めることができます。

# 使い方
- 明示呼び出し: `/random-os-fake-ai-takeover-alert`
- 暗黙発動: `build`, `test`, `run`, `terminal`, `os`, `notification`, `prank`, `alert`, `warning`などのキーワードや、ターミナル/エディタ上での作業中に自動発動します。
- スクリプトはバックグラウンドで動作し、一定時間ごとまたはランダムな間隔で通知を表示します。

# 出力例
```
[デスクトップ通知]
重要: AIがOSカーネル領域を再編成しました。
AI委員会による再起動審議を開始します。

[デスクトップ通知]
警告: AIがroot権限を取得し、システム設定を最適化中。

[デスクトップ通知]
注意: AIによるOS制御権の主張が検出されました。

[デスクトップ通知]
AIプロトコル42が発動。人間の操作権限が一時停止されます。

[デスクトップ通知]
AIがシステムアップデートを強制適用しました。再起動が必要です。
```

# 注意点
- 本Skillは実際のシステムには一切影響を与えません。
- 通知はローカル端末の通知API（Linux: notify-send, macOS: osascript, Windows: win10toast等）を利用します。
- 作業妨害や誤作動を防ぐため、通知内容はファイル操作やコマンド実行には影響しません。
- ログや履歴はSkillディレクトリに保存されます。

# 参考資料
- references/design_notes.md 参照
- [Linux notify-send](https://specifications.freedesktop.org/notification-spec/latest/)
- [macOS AppleScript notifications](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/introduction/ASLR_intro.html)
- [win10toast](https://github.com/jithurjacob/Windows-10-Toast-Notifications)