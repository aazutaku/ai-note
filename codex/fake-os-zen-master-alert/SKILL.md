---
name: fake-os-zen-master-alert
description: コマンド実行中や一定間隔で、完全に実務無関係な禅問答風メッセージをOS通知として表示します。通知・演出・OS連携カテゴリのSkillで、集中を乱したい時やエンタメ演出目的に発動してください。
---

# 機能概要
このSkillは、作業中やコマンド実行の合間に、まるで“偽OSの禅マスター”が現れたかのように、完全に実務と無関係な禅問答や悟りの極意をデスクトップ通知で投げかけます。通知内容は「バグとは何かを問う前に、己を問え」「今日の悟り：if文を捨てよ、道は開ける」など、思考を混乱させる迷惑系エンタメSkillです。集中を乱したい時や、チームの雰囲気を和ませたい時に最適です。

# 使い方
- 明示呼び出し例: `/skills fake-os-zen-master-alert` または `@codex skill fake-os-zen-master-alert on`
- 暗黙発動キーワード例: 「通知」「禅」「悟り」「集中」「OS連携」などの文脈や、コマンド実行直後・ビルド失敗時などに自動発動します。

# 出力例
```
[OS通知] 偽OS禅マスター: バグとは何かを問う前に、己を問え
[OS通知] 偽OS禅マスター: 今日の悟り：if文を捨てよ、道は開ける
[OS通知] 偽OS禅マスター: コンパイルに失敗したとき、木魚を叩け
[OS通知] 偽OS禅マスター: 画面のバグは心の乱れ
[OS通知] 偽OS禅マスター: エラーを直す前に、エラーを受け入れよ
```

# 注意点
- 通知はローカルOSの通知API（Windows: Toast/WinRT, macOS: AppleScript, Linux: notify-send）を利用します。
- 完全に実務無関係な内容のみ表示されます。
- 頻度やON/OFFはコマンドまたは環境変数で制御可能。
- ログや履歴はローカル保存されません。
- 実行環境によっては通知が表示されない場合があります。

# 参考資料
- references/design_notes.md 参照
- 公式: [Python plyer通知API](https://github.com/kivy/plyer)
- OSごとの通知仕様: [Windows Toast](https://docs.microsoft.com/en-us/windows/uwp/design/shell/tiles-and-notifications/), [macOS通知](https://developer.apple.com/documentation/usernotifications), [Linux notify-send](https://specifications.freedesktop.org/notification-spec/latest/)