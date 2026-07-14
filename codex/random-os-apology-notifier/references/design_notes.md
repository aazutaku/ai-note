# 概要
random-os-apology-notifierは、OSの通知APIを利用して「無責任な謝罪」を演出するジョークSkillです。実際のエラーやファイル操作は一切行わず、ユーザーの作業環境に影響を与えません。

# 公式ドキュメント抜粋
- macOS: [AppleScript display notification](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/introduction/ASLR_intro.html)
- Linux: [notify-send](https://specifications.freedesktop.org/notification-spec/notification-spec-latest.html)

# 利用例
- チームの朝会で「OSが謝ってきた！」と話題作りに
- リモートワーク中のちょっとした息抜きやネタに
- 実際のエラーと混同しないよう、明確にフェイクであることを強調

# 注意点
- Windows OSでは動作しません
- 通知APIが無効な環境では表示されません
- 通知内容は完全にランダム生成

# 設計方針
- シンプルなCLI構成とし、サブコマンドで柔軟に利用可能
- ログや履歴保存は一切行わず、プライバシーに配慮
- 実際の業務進行やシステムに干渉しない設計