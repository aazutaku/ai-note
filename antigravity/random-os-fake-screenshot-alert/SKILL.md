---
name: random-os-fake-screenshot-alert
description: Antigravityがコマンド実行や作業中に、'スクリーンショット保存通知'や'証拠画像保存済み'などの謎OS風通知をランダムに発動。通知内容は毎回変化し、何も保存されません。'スクリーンショット'や'保存'などのキーワード検知時や定期的なトリガーで自動発動します。
---

# 機能概要
このSkillは、作業中やコマンド実行時に突然“OS偽スクリーンショット保存通知”をデスクトップに表示し、現場の緊張感やマンネリを一撃で打ち砕くジョーク系演出を提供します。通知内容は完全ランダムで、例えば「スクリーンショット保存済み：バグ発生の瞬間」や「証拠画像を保存しました」「あなたの集中顔を記録しました」など、意味不明で混沌とした内容が炸裂します。実際には何も保存されず、通知のみが表示されます。

# 使い方
このSkillは明示的な呼び出しは不要です。Antigravityが「スクリーンショット」「保存」「記録」などのキーワードを含むコマンドや会話、または一定時間ごとに自動的に発動します。例えば、`git commit`や`python main.py`実行時、または「記録」「証拠」などの単語を含む発話時に、突然通知が表示されます。

# 出力例
```
[通知] スクリーンショット保存済み：バグ発生の瞬間
[通知] 証拠画像を保存しました（保存先：謎の場所）
[通知] あなたの集中顔を記録しました
[通知] スクリーンショット保存済み：謎の警告画面
[通知] 保存完了：エラー再現の瞬間
```

# 注意点
- 実際に画像やファイルは一切保存されません。
- 通知内容は毎回ランダム生成されます。
- 頻度やタイミングは自動で制御され、迷惑にならないよう設計されています。
- ローカル環境の通知API（Windows: Toast, macOS: terminal-notifier, Linux: notify-send）を使用します。
- 企業や公共の場での利用は空気を読んでください。

# 参考資料
参考実装や通知APIの詳細は`references/design_notes.md`および各OSの通知公式ドキュメント（[Windows Toast](https://docs.microsoft.com/en-us/windows/uwp/design/shell/tiles-and-notifications/), [macOS terminal-notifier](https://github.com/julienXX/terminal-notifier), [Linux notify-send](https://specifications.freedesktop.org/notification-spec/latest/)）を参照してください。