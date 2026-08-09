# 概要
このSkillは、開発者の操作時に現実には存在しないレガシーOSやAPIの“サポート終了通知”をランダムで表示し、ユーモアとノスタルジーを演出します。実際の環境やデータには一切影響を与えません。

# 公式ドキュメント抜粋
- Windows: [Toast Notifications](https://learn.microsoft.com/en-us/windows/uwp/design/shell/tiles-and-notifications/)
- macOS: [AppleScript display notification](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/introduction/ASLR_intro.html)
- Linux: [notify-send](https://specifications.freedesktop.org/notification-spec/notification-spec-latest.html)

# 利用例
- ターミナルやエディタでコマンド実行時に自動発火
- `/random-os-fake-legacy-support-alert log` で任意に通知を発火
- `/random-os-fake-legacy-support-alert list` で過去の通知履歴を確認

# 注意点
- 通知内容は完全なジョークであり、実際のサポート終了やシステム変更は発生しません。
- Linuxで`notify-send`が未インストールの場合は通知が表示されません。

# 設計方針
OSごとの標準通知APIのみを利用し、外部依存やシステム設定変更を一切行いません。履歴はユーザーディレクトリ配下に記録し、プライバシーや安全性を重視しています。