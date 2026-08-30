# 概要
このSkillは、OSの標準通知APIを活用し、作業中に意外性のある演出を提供します。実際のシステムやファイルには一切影響を与えず、通知のみを行う設計です。

# 公式ドキュメント抜粋
- Windows: Toast Notification ([公式](https://learn.microsoft.com/en-us/windows/uwp/design/shell/tiles-and-notifications/send-local-toast))
- macOS: AppleScript display notification ([公式](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/reference/ASLR_display.html))
- Linux: notify-send ([manページ](https://man7.org/linux/man-pages/man1/notify-send.1.html))

# 利用例
- 長時間作業時の休憩リマインダー
- 雑談イベントや社内ハッカソンの演出
- 集中力が切れたタイミングでの気分転換

# 注意点
- 業務端末や会議中の利用は控えてください。
- 通知が届かない場合は、OSの通知設定を確認してください。

# 設計方針
- 毎回ランダムなボス・セリフを生成し、履歴も記録
- OS種別ごとに最適な通知APIを選択
- コマンドラインから明示的にも、キーワード検知による自動発動にも対応