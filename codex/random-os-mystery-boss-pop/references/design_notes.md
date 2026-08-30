# 概要
このSkillは、作業中のユーザーに意外性とユーモアを与えるため、OSの通知APIを活用して“謎のボスキャラ”演出を提供します。通知は純粋な演出であり、システムやデータには一切影響を与えません。

# 公式ドキュメント抜粋
- Windows: [Toast Notifications](https://docs.microsoft.com/en-us/windows/uwp/design/shell/tiles-and-notifications/toast-notifications)
- macOS: [AppleScript display notification](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/reference/ASLR_cmds.html)
- Linux: [notify-send](https://man7.org/linux/man-pages/man1/notify-send.1.html)

# 利用例
- 長時間作業時のストレッチ喚起
- チームのリラックス演出
- コーディング中の気分転換

# 注意点
- 通知は一時的な表示のみで、履歴や記録は残りません。
- 一部Linux環境や通知非対応端末では表示されない場合があります。

# 設計方針
- OS標準APIのみ使用し、外部依存や永続データ保存を避ける。
- ボスキャラやメッセージは随時拡張可能なリスト構造。
- CLIサブコマンドで演出・一覧・概要を柔軟に呼び出せる設計。