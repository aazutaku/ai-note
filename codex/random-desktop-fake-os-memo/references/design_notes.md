# 概要
このSkillは、ユーザーのデスクトップに意味不明な“謎OSメモ”を定期的または任意タイミングで通知し、作業中の集中にシュールな混乱と遊び心をもたらします。実用性ゼロの怪文書で、通知内容は完全ランダムです。

# 公式ドキュメント抜粋
- macOS: `osascript`で通知表示 ([AppleScript通知公式](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/introduction/ASLR_intro.html))
- Linux: `notify-send` ([freedesktop.org](https://specifications.freedesktop.org/notification-spec/latest/))
- Windows: PowerShellでToast通知 ([Microsoft Docs](https://learn.microsoft.com/en-us/windows/uwp/design/shell/tiles-and-notifications/send-local-toast))

# 利用例
- `/skills menu`や`random-desktop-fake-os-memo notify`で即時発動
- 作業中に定期的なシュール通知で気分転換

# 注意点・設計方針
- 通知内容は毎回完全ランダムで、履歴やローカル保存は行いません。
- OSごとに通知APIを自動判別し、システム設定やファイルには一切影響しません。
- 実用性や意味は一切なく、純粋な演出・遊び用途に特化しています。
