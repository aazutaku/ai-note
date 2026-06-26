# 概要
本Skillは、OS標準の通知APIを活用し、明らかにジョークと分かる“フェイクウイルスアラート”をランダム表示することで、作業のマンネリ化を打破し、チームや個人の気分転換を促進します。

# 公式ドキュメント抜粋
- Windows: win10toast (https://pypi.org/project/win10toast/)
- macOS: AppleScript display notification (https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/reference/ASLR_cmds.html)
- Linux: notify-send (https://specifications.freedesktop.org/notification-spec/)

# 利用例
- 長時間のコーディングやリモートワーク中、気分転換のきっかけに
- チームのSlackやZoomで話題作りとして

# 注意点
- 通知内容は本物のウイルス警告やセキュリティアラートと誤認されないよう、明確なジョーク文言のみを使用
- システムやファイルには一切影響を与えません

# 設計方針
- クロスプラットフォーム（Windows/macOS/Linux）対応
- 環境構築不要（OS標準APIのみ）
- ログ機能・履歴閲覧・サマリー表示で運用状況も可視化