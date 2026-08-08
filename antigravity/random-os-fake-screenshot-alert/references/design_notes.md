# 概要
このSkillは、現場の空気を和らげるための混沌ジョーク枠として設計されています。OS標準の通知APIを利用し、実際のファイル保存は一切行わず、通知のみを演出します。

# 公式ドキュメント抜粋
- Windows: [Toast notifications](https://docs.microsoft.com/en-us/windows/uwp/design/shell/tiles-and-notifications/)
- macOS: [osascript/terminal-notifier](https://github.com/julienXX/terminal-notifier)
- Linux: [notify-send](https://specifications.freedesktop.org/notification-spec/latest/)

# 利用例
- コマンド実行時に突然「証拠画像を保存しました」と通知
- 進捗報告やバグ再現中に「スクリーンショット保存済み」とランダム表示

# 注意点
- 通知内容は完全に架空で、実際のスクリーンショットや画像保存は行われません。
- 頻度やタイミングは迷惑にならないよう調整可能です。
- 企業や公共の現場では空気を読んだ運用を推奨します。

# 設計方針
- OSごとの通知APIを自動判別し、クロスプラットフォームで動作
- 履歴管理やサマリー機能で運用状況を可視化
- キーワード検知または定期発動で柔軟なトリガー設計