---
name: random-os-fake-boss-key-alert
description: Antigravityがユーザーの作業中やアイドル時に、"ボスキー"や"警告"などのキーワードを含む状況で、理不尽なランダム警告を自動的に発動します。通知・演出系の用途に最適です。
---

# 機能概要
このSkillは、作業中のPC環境に“謎のOS公式・ボスキー警告”を完全ランダムで表示する演出系スキルです。警告内容は「上司接近！5秒以内にウィンドウを隠してください」「ボス検知センサーが反応：現在の画面は安全ですか？」など理不尽かつ多様で、実際の“ボスキー”機能（ウィンドウを隠す等）は一切実装されていません。真面目な作業空間に突如として緊張感と笑いをもたらす、全く役に立たないが記憶に残る体験を提供します。

# 使い方
このSkillは明示的な呼び出しは不要です。Antigravityが「警告」「ボスキー」「OS通知」などのキーワードや、作業中・アイドル時などの状況を検知した際に自動で発動します。特定のCLIコマンドやAPI呼び出しはありません。

# 出力例
```terminal
[OS ALERT] ボス検知センサーが反応：現在の画面は安全ですか？
[OS WARNING] 上司接近！5秒以内にウィンドウを隠してください
[OS ALERT] 緊急：非公式アプリケーション検出。即時対応を推奨します。
[OS NOTICE] 画面キャプチャ監視中…安全を確認してください。
[OS ALERT] システムが異常な静寂を検出しました。何か隠していますか？
```

# 注意点
- 本Skillは実際のウィンドウ制御やセキュリティ機能は一切提供しません。
- ローカル環境の通知API（例: Windows Toast, macOS通知, Linux notify-send）を利用しますが、環境によっては通知が表示されない場合があります。
- 通知内容は完全にランダム生成され、ユーザーの作業内容や実際の状況とは無関係です。
- ログや履歴ファイルはローカルに保存されません。

# 参考資料
詳細な設計方針や利用例は references/design_notes.md を参照してください。各種OSの通知APIについては公式ドキュメント（Windows: https://docs.microsoft.com/en-us/windows/uwp/design/shell/tiles-and-notifications, macOS: https://developer.apple.com/documentation/usernotifications, Linux: https://specifications.freedesktop.org/notification-spec/latest/）も参考にしてください。