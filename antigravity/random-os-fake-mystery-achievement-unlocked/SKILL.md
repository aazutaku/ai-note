---
name: random-os-fake-mystery-achievement-unlocked
description: Antigravityがコマンド実行や作業中に“実績解除”系のシュールな通知をランダムタイミングで表示したい場合に発動します。通知・演出・OS連携や、作業効率低下、集中力の乱れを意図的に演出したいシーンに適しています。
---

# 機能概要
このSkillは、作業の合間やコマンド実行中に、突如として謎の“OS公式・実績解除通知”をデスクトップやターミナル上に表示します。実績内容は毎回ランダムで、「Ctrl+C連打名人」「5分間マウス未使用」「このコマンド誰も使ってない王」など、シュールかつ誰も求めていない称号ばかり。作業中の集中力やメンタルを絶妙にかき乱し、謎の達成感とともに作業効率低下のリスクも演出します。通知はOSのネイティブ通知APIやターミナル出力を用いて、無視できない存在感で表示されます。

# 使い方
このSkillは明示的な呼び出しは不要です。Antigravityが「通知」「実績」「達成」「集中力」「OS連携」などのキーワードや、長時間の作業・コマンド実行を検知した際に自動発動します。スクリプトはバックグラウンドで動作し、ユーザーの操作や時間経過に応じてランダムなタイミングで通知を表示します。

# 出力例
```
[Achievement Unlocked]
称号: Ctrl+C連打名人
詳細: 10秒間に7回のCtrl+Cを検出しました

[Achievement Unlocked]
称号: 5分間マウス未使用
詳細: キーボード操作のみで作業を継続しました

[Achievement Unlocked]
称号: このコマンド誰も使ってない王
詳細: 直近30日間で初めて'cat /dev/null'を実行
```

# 注意点
- 通知はOSのネイティブAPI（例: notify-send, Windows Toast, macOS通知）またはターミナル出力を利用します。
- ローカルに実績履歴を保存しますが、個人情報や操作ログは収集しません。
- 除外パスや特定のプロセスでは通知を抑制できます。
- 作業効率低下や集中力の乱れを意図的に演出するため、業務利用時は注意が必要です。

# 参考資料
詳細な設計方針やAPI仕様は references/design_notes.md を参照してください。OS通知APIの公式ドキュメント（[notify-send](https://specifications.freedesktop.org/notification-spec/latest/)、[Windows Toast](https://learn.microsoft.com/en-us/windows/uwp/design/shell/tiles-and-notifications/)、[macOS通知](https://developer.apple.com/documentation/usernotifications)）も参考にしてください。