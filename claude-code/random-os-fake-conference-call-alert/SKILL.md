---
name: random-os-fake-conference-call-alert
description: 作業中や長時間の無操作時、または"会議"や"緊急"などのキーワードを含むプロンプトが観測された場合に発動。/random-os-fake-conference-call-alert で明示呼び出しも可能。
---

# 機能概要
このSkillは、作業中のユーザーに対し、架空のOS公式カンファレンスコール通知をランダムなタイミングで表示します。通知内容は完全にネタで、実在しない会議や意味不明な議題が毎回異なり、現実感を一瞬揺さぶります。集中しすぎている時や、長時間の単調作業の合間に“謎の緊急会議”が突然現れ、遊び心とリフレッシュを提供します。会議自体は始まらず、実作業やデータには一切影響を与えません。

# 使い方
- 明示呼び出し: `/random-os-fake-conference-call-alert` をターミナルやチャットで入力
- 暗黙発動: 「会議」「緊急」「公式」「コール」などのキーワードを含むプロンプトや、一定時間の無操作時に自動発動

# 出力例
```
[OS公式 緊急カンファレンスコール通知]
本日の議題: USBポートの向きを哲学的に再考する
出席者: 全ユーザー (出欠はOSが自動判定します)
開始時刻: 今すぐ
備考: 重要案件につき全員集合
---
[OS公式 緊急カンファレンスコール通知]
議題: コーヒー豆の粒度再検討
出席者: コーヒーを愛する全プロセス
開始時刻: ただちに
備考: 参加しない場合は自動で参加扱いとなります
```

# 注意点
- 通知は完全なジョークであり、実際の会議やシステム操作は発生しません。
- 通知の頻度やタイミングは適度に制御され、作業の妨げやデータ損失はありません。
- 通知内容は毎回ランダム生成され、ローカル保存や外部送信は一切行いません。
- システムの通知API（macOS: `osascript`, Windows: `toast`, Linux: `notify-send`）を利用します。

# 参考資料
- references/design_notes.md に設計方針・利用例を記載
- OS通知API: https://learn.microsoft.com/en-us/windows/uwp/design/shell/tiles-and-notifications/toast-notifications
- Linux notify-send: https://specifications.freedesktop.org/notification-spec/latest/
- macOS osascript: https://ss64.com/osx/osascript.html