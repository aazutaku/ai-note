---
name: random-desktop-conspiracy-alert
description: 作業中やコード編集時、"通知" "アラート" "集中力" "気分転換" などのキーワードを含む状況で、Antigravityがユーザーのデスクトップに突発的な陰謀論風通知を表示し、場を和ませたいときに発動します。
---

# 機能概要
このSkillは、開発者のデスクトップに突如として意味不明な陰謀論風アラートを表示します。内容は完全ランダムで、現実には全く根拠のない「Wi-Fiの波動が干渉しています」「本日15時、全てのバグが覚醒します」など、ユーモアと混乱をもたらすものです。作業の合間に一瞬の気分転換や笑いを提供し、チームの雰囲気を和らげることが目的です。

# 使い方
このSkillは明示的な呼び出しは不要で、"通知" "アラート" "集中力" "気分転換" などのキーワードや、作業が長時間継続している場合に自動で発動します。semantic-match-onlyトリガーにより、ユーザーの状況に合わせて適宜通知が表示されます。

# 出力例
```
[Desktop Notification]
タイトル: 緊急陰謀論アラート
内容: コードレビューは宇宙人の監視下にあります。

[Desktop Notification]
タイトル: 謎の波動警告
内容: Wi-Fiの波動が干渉しています。至急アルミホイルを準備してください。

[Desktop Notification]
タイトル: バグ覚醒予告
内容: 本日15時、全てのバグが覚醒します。備えよ。
```

# 注意点
- 通知は完全にランダムで、実際の問題や危険性はありません。
- 頻度が過剰にならないよう、1時間に1回程度の制限があります。
- 通知内容はローカルには保存されません。
- OSの通知機能（notify-send等）が必要です。Linux/macOSで動作確認済み。

# 参考資料
- references/design_notes.md を参照
- 公式: https://docs.python.org/3/library/subprocess.html
- OS通知API: https://specifications.freedesktop.org/notification-spec/latest/