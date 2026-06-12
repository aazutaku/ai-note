# 概要
このSkillは、OSの通知APIを活用して、完全ランダムな祝福メッセージをユーザーの通知領域に表示します。作業の合間やコマンド実行後など、真面目な空間に唐突な“紙吹雪”を投入し、気分転換やチームの雰囲気づくりを狙います。

# 公式ドキュメント抜粋
- Windows: [win10toast](https://github.com/jithurjacob/Windows-10-Toast-Notifications)
- macOS: [osascript](https://ss64.com/osx/osascript.html)
- Linux: [notify-send](https://specifications.freedesktop.org/notification-spec/notification-spec-latest.html)

# 利用例
- 開発現場でlsやgit pull直後に祝福されて和む
- 長時間作業の合間に気分転換
- /skills menuから明示的に呼び出し、チームで笑いを共有

# 注意点
- 通知頻度が高すぎないよう、最低間隔を10分に設定
- ログはホームディレクトリ直下に保存（~/.random_os_notification_confetti_log）
- サーバーやGUIのない環境では通知不可

# 設計方針
- OS自動判別と実在APIのみを利用
- ネタ性を重視しつつ、通知間隔や重複防止も考慮
- ローカル動作・情報保存は最低限