# 概要
このSkillは、作業中のユーザーに対して完全ランダムな“気分天気”を通知として表示し、場の空気を和らげることを目的としています。実用性よりも演出・遊び心を重視した設計です。

# 公式ドキュメント抜粋
- Windows: [Toast Notifications](https://docs.microsoft.com/en-us/windows/uwp/design/shell/tiles-and-notifications/toast-notifications)
- macOS: [NSUserNotification](https://developer.apple.com/documentation/usernotifications)
- Linux: [notify-send](https://man.archlinux.org/man/notify-send.1)

# 利用例
- チームの朝会や作業開始時に、/os-fake-mood-weather-bar で気分天気を表示し、会話のきっかけや笑いを誘う。
- 開発の合間にランダム発動させて、集中しすぎた空気を和ませる。

# 注意点
- OSの通知APIを直接呼び出すため、権限やAPIのバージョンによっては通知が表示されない場合があります。
- ログファイルはユーザーのホームディレクトリに保存されますが、個人情報は含まれません。

# 設計方針
- クロスプラットフォーム（Windows/macOS/Linux）対応。
- 実在APIのみ使用し、外部依存を最小限に。
- Skill本体はCLIサブコマンド形式で拡張性を確保しています。