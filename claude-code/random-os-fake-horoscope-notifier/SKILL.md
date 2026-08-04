---
name: random-os-fake-horoscope-notifier
description: 作業開始や新規ターミナル起動時など、ユーザーの開発セッション開始を検知した際に発動。'占い'や'運勢'、'ラッキーコマンド'などのキーワード出現時にも明示的に呼び出せます。
---

# 機能概要
このSkillは、開発者の作業開始時や新規ターミナル起動時などに、完全ランダムな“OS風の星占い通知”を表示します。通知内容は「今日のラッキーコマンドはls」や「運勢：バグ回避率上昇」「注意：仕様変更星が逆行中」など、開発現場にちなんだユーモラスな占いメッセージ。1日1回だけ通知され、毎回異なるネタが表示されるため、日々のコーディングにちょっとした笑いと新鮮さをもたらします。

# 使い方
- 明示呼び出し: `/random-os-fake-horoscope-notifier` または `/horoscope`
- 暗黙発動: 「作業開始」「新規ターミナル」「占い」「運勢」「ラッキーコマンド」などのキーワードや、セッション開始時に自動で発動します。

# 出力例
```
─────────────────────────────
【OS星占い通知】
運勢：今日はバグ回避率が15%上昇します。
ラッキーコマンド：ls
注意：仕様変更星が逆行中。コミット前にREADMEを確認！
─────────────────────────────
```

# 注意点
- 通知は1日1回のみ。複数回呼び出しても同じ内容が表示されます。
- 通知内容は完全ランダム生成ですが、実際の運勢や開発効率には一切影響しません。
- ローカルに通知履歴を保存します（`~/.random_os_horoscope_history.json`）。
- OSの通知API（macOS: `osascript`、Linux: `notify-send`、Windows: `toast`）とターミナル出力の両方に対応。

# 参考資料
- references/design_notes.md
- [notify-send公式](https://specifications.freedesktop.org/notification-spec/latest/)
- [osascript](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/introduction/ASLR_intro.html)