# 概要
このSkillは、作業中のユーザー体験に遊び心を加えるためのフェイク通知演出ツールです。実際の会議やOS操作は一切伴わず、通知内容も完全なジョークです。

# 公式ドキュメント抜粋
- Windows: [Toast Notifications](https://learn.microsoft.com/en-us/windows/uwp/design/shell/tiles-and-notifications/toast-notifications)
- Linux: [freedesktop.org Notification Spec](https://specifications.freedesktop.org/notification-spec/latest/)
- macOS: [osascript](https://ss64.com/osx/osascript.html)

# 利用例
- 長時間の集中作業中にリフレッシュを促す
- チーム内での小ネタやアイスブレイク
- ターミナルやチャットで明示的に呼び出して楽しむ

# 注意点
- 実際の会議や通知と誤認しないよう、内容は極端にネタ要素を強調
- 通知頻度は15分以上の間隔を設け、連続発動を抑制
- ログや個人情報の外部送信は一切なし

# 設計方針
- OSの標準通知APIのみ利用し、追加ライブラリ依存は最小限
- ユーザーの作業やデータに影響を与えない安全設計
- ジョーク性を保ちつつ、通知内容のバリエーションを重視