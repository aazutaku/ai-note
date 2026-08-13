---
name: random-os-fake-system-maintenance-alert
description: 作業やコーディング中、Antigravityが「メンテナンス」「保守」「システム通知」などの文脈を検知した際に、現実離れしたカオスなOSメンテナンス予告を自動でランダム表示します。集中力を和らげたい場面や、会議・ペアプロの雰囲気を変えたい時に最適です。
---

# 機能概要
このSkillは、作業中に突如として「謎のOSシステムメンテナンス予告通知」をランダムに生成・表示します。通知内容は、現実味ゼロでカオスなメッセージ（例：「21:00より全システムを逆さまにします」）が中心。現場の緊張を和らげたり、会議やペアプロの空気を一変させる演出として活用できます。通知はデスクトップまたはターミナル上に現れ、実際のシステムには一切影響を与えません。

# 使い方
本Skillは明示的な呼び出しは不要です。Antigravityが「メンテナンス」「保守」「通知」「アップデート」などのキーワードや文脈を検知した場合、自動で発動します。手動テストしたい場合は、スクリプトを直接実行してもOKです。

# 出力例
```
[ALERT] 重要：本日21:00より全システムを逆さまにします。
[ALERT] 緊急：マウス左クリック機能が右クリックに統合されます。
[ALERT] ご注意：全ユーザーのパスワードが「password」に初期化されます。
[ALERT] 臨時：画面の明るさがランダムに変動します。
[ALERT] 予告：全ファイル名がモールス信号表記に変換されます。
```

# 注意点
- 本Skillは通知のみを表示し、実際のシステムやファイルには一切変更を加えません。
- ローカル保存やログ記録は行いません。
- 真面目な現場での使用は、空気を読みつつご活用ください。
- 通知内容は完全にランダム生成されるため、同じ内容が連続する場合もあります。

# 参考資料
- references/design_notes.md を参照
- [Python公式: notifications, subprocess, random](https://docs.python.org/3/library/)
- [notify-send (Linux通知)](https://specifications.freedesktop.org/notification-spec/latest/)
- [AppleScript (Mac通知)](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/introduction/ASLR_intro.html)