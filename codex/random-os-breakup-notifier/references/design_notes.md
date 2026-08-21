# 概要
random-os-breakup-notifierは、作業中のユーザーに突発的な“デジタル失恋”通知を届けるジョーク系Skillです。通知内容はバリエーション豊かで、日常の作業に非日常の笑いを提供します。

# 公式ドキュメント抜粋
- Linux: notify2 (https://pypi.org/project/notify2/)
- macOS: osascript (https://ss64.com/osx/osascript.html)
- Windows: win10toast (https://pypi.org/project/win10toast/)

# 利用例
- チームの朝会や、集中作業中のリフレッシュタイムに
- Slackやチャットボットの通知トリガーとしても応用可能

# 注意点
- 通知内容はローカルに保存されません。
- システム通知APIの仕様変更や権限設定により、通知が表示されない場合があります。
- 重要作業中の誤発動には注意し、必要に応じてSkillの一時停止を推奨します。

# 設計方針
- OSごとの標準APIを用い、環境依存性を最小化
- ジョーク性と安全性（作業への非干渉）を両立
- 拡張性を考慮し、通知メッセージの追加やカスタマイズも容易