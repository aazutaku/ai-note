---
name: os-random-fake-motivational-speech-alert
description: 作業コマンド実行時や/skillsメニュー呼び出し時など、ユーザーのアクションに応じて毎回異なる“OS公式・やる気爆上げスピーチ通知”を自動発火します。通知・演出・OS連携系Skill。
---

# 機能概要
このSkillは、ターミナルやエディタで作業中に、まるでOS公式からの激励のような“謎のやる気爆上げスピーチ”通知をランダムに表示します。内容は毎回異なり、「あなたのタイピングが世界を変える」「今こそ伝説になるときです」など、どこかズレているが妙に熱いメッセージばかり。日常のコーディングやタスク実行にエンタメ要素を注入し、気分転換や集中力UPをサポートします。実害ゼロで、システムやデータには一切影響しません。

# 使い方
- 明示呼び出し: `/skills os-random-fake-motivational-speech-alert` または `$ os-random-fake-motivational-speech-alert`
- 暗黙発動: ターミナルでコマンド実行時、またはエディタで保存・ビルド・テストなどのタイミングで自動発火（設定により常時/任意トリガー選択可）

# 出力例
```
[OS MOTIVATION] 今こそコード界の伝説になるときです。
[OS MOTIVATION] あなたのcommitは宇宙を救う可能性を秘めています。
[OS MOTIVATION] そのタイピング、情熱が伝わってきます。
[OS MOTIVATION] シンタックスエラーも、あなたなら乗り越えられる。
[OS MOTIVATION] 今日の努力が明日のOSを支えます。
```

# 注意点
- 通知内容は毎回ランダム生成されますが、真剣に受け止める必要はありません。
- システムやファイルには一切変更を加えません。
- ローカル通知（`notify-send`や`osascript`等）を利用するため、環境によっては追加設定が必要です。
- ログ保存や履歴機能はありません。

# 参考資料
- [notify-send (Linux)](https://specifications.freedesktop.org/notification-spec/latest/)
- [osascript (macOS)](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/introduction/ASLR_intro.html)
- references/design_notes.md を参照