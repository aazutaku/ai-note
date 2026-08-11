---
name: os-fake-mood-weather-bar
description: このSkillは、コード実行や作業の合間に「気分天気バー」を画面端へランダム表示します。明示呼び出し（/os-fake-mood-weather-bar）や、'気分','天気','バー','カオス','演出'等のキーワード検知時に自動発動します。
---

# 機能概要
このSkillは、あなたのPC画面端やメニューバーに“OS風・謎の気分天気バー”を突如出現させます。天気バーは「絶好調・晴れ」「やる気霧雨」「集中力台風接近中」「バグの嵐」「仕様雪崩」など、完全ランダムな“気分天気”を表示し、作業空間にカオスな演出を加えます。実用性はほぼありませんが、仕事や開発の合間にシュールな空気を演出することができます。

# 使い方
- 明示呼び出し: `/os-fake-mood-weather-bar` を実行すると即座にバーが表示されます。
- 暗黙発動: 「気分」「天気」「バー」「カオス」「演出」などのキーワードが会話やコマンド内に出現した場合、自動でバーが出現します。

# 出力例
```
[気分天気バー] 2024-06-23 14:33:07
本日の気分天気：やる気霧雨
コメント：やる気が微妙に降り注ぐ午後。コーヒーで回復を！

[気分天気バー] 2024-06-23 15:12:10
本日の気分天気：集中力台風接近中
コメント：集中の嵐が迫る。タスクを片付けるチャンス！

[気分天気バー] 2024-06-23 16:01:55
本日の気分天気：バグの嵐
コメント：バグが吹き荒れる一日。冷静なデバッグを。
```

# 注意点
- 実際の天気や心理状態とは一切関係ありません。
- ローカルPCでのみ動作し、バーの表示はOSの通知API（Windows: Toast, macOS: NSUserNotification, Linux: notify-send）を利用します。
- 他の通知系Skillと同時に発動した場合、通知が重複する可能性があります。
- ログはローカルに保存されますが、個人情報は含みません。

# 参考資料
- [Windows Toast Notifications](https://docs.microsoft.com/en-us/windows/uwp/design/shell/tiles-and-notifications/toast-notifications)
- [macOS User Notifications](https://developer.apple.com/documentation/usernotifications)
- [Linux notify-send](https://man.archlinux.org/man/notify-send.1)
- references/design_notes.md を参照してください。