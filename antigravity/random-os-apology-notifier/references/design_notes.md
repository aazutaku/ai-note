# 概要
random-os-apology-notifierは、ユーザー体験を損なうことなく、デスクトップ通知APIを活用して完全なフェイク謝罪メッセージを表示する演出スキルです。実際のエラーや業務進行と無関係に、ユーモアや和みを提供します。

# 公式ドキュメント抜粋
- Windows: Toast通知API（https://docs.microsoft.com/en-us/windows/uwp/design/shell/tiles-and-notifications/）
- macOS: AppleScript通知（https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/）
- Linux: notify-send（https://specifications.freedesktop.org/notification-spec/latest/）

# 利用例
- リモートワークやオフィスでのアイスブレイク
- 業務進行中の息抜きや話題作り
- フェイク障害訓練やユーモア演出

# 注意点
- 通知APIが利用不可な環境や、通知がポップアップしない設定では効果がありません。
- ログはユーザーのホームディレクトリにのみ保存され、外部送信はありません。
- 実際のエラーやシステム障害とは一切関係ありません。

# 設計方針
- OSごとに実在する通知APIのみを利用し、追加ライブラリが不要な範囲は極力標準機能で実装。
- ログ・サマリー機能で利用状況を可視化。
- ユーザーの混乱を避けるため、通知タイトルやメッセージ文面でフェイク性を明示。