---
name: random-os-coffee-break-notifier
description: 作業やコーディング中に“OS公式っぽい”コーヒーブレイク推奨通知を完全ランダムなタイミング・内容で表示したい時に発動。/random-os-coffee-break-notifier や「コーヒー休憩」「集中力低下」等のキーワードで自動発動。
---

# 機能概要
このSkillは、作業中に“OS公式っぽい”コーヒーブレイク推奨通知をランダムなタイミング・内容でデスクトップに表示します。通知内容は「重要：カフェイン補給の時刻です」「AI的診断：あと5分で集中力が消滅します」など、妙に説得力があるが全く役に立たないメッセージが毎回異なります。真面目に作業している時ほど理不尽に推奨される謎コーヒータイムで、作業の合間に少しだけクスッとできる演出を提供します。

# 使い方
- 明示呼び出し: `/random-os-coffee-break-notifier` を実行
- 暗黙発動: 「コーヒー休憩」「集中力低下」「生産性」「休憩したい」などのキーワードを含む会話やコード中で自動発動

# 出力例
```
[OS通知] 重要：カフェイン補給の時刻です
[OS通知] タスク進捗が停滞中。コーヒーを飲めとの神託
[OS通知] AI的診断：あと5分で集中力が消滅します
[OS通知] システム推奨：生産性維持のため、今すぐコーヒーブレイクを！
[OS通知] 注意：脳内カフェイン残量が閾値を下回りました
```

# 注意点
- 通知は完全ランダムなタイミング・内容で表示されます
- OSの通知API（macOS: `osascript`/Linux: `notify-send`/Windows: `toast`）を利用
- データ損失やファイル改変は一切ありません
- 通知内容はジョーク要素が強く、実際の健康や生産性向上は保証しません
- ローカルに通知履歴は保存されません

# 参考資料
- [Python公式 subprocess モジュール](https://docs.python.org/ja/3/library/subprocess.html)
- [macOS osascript公式](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/introduction/ASLR_intro.html)
- [Linux notify-send](https://specifications.freedesktop.org/notification-spec/notification-spec-latest.html)
- references/design_notes.md も参照