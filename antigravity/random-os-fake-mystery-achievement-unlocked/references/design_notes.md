# 概要
本Skillは、OSのネイティブ通知APIやターミナル出力を活用し、ユーザーの作業中に“実績解除”風の通知をランダムに表示します。通知内容はシュールな称号と詳細テキストで構成され、集中力や作業効率にユーモラスな影響を与えることを狙っています。

# 公式ドキュメント抜粋
- Linux: notify-send (Freedesktop.org Notification Spec)
- Windows: win10toast, Windows Toast通知 ([公式](https://learn.microsoft.com/en-us/windows/uwp/design/shell/tiles-and-notifications/))
- macOS: osascriptによるUserNotifications ([公式](https://developer.apple.com/documentation/usernotifications))

# 利用例
- 長時間のコーディングやリモート作業時に、意図的に集中を乱したい場合
- オフィスやイベントでの“ネタ”演出
- ターミナルやデスクトップのデモンストレーション

# 注意点
- 通知はユーザーの意図と無関係に発動するため、業務環境や集中が必要な場面では利用に注意してください。
- 実績履歴はローカルにJSONで保存され、個人情報や詳細な操作ログは収集しません。
- OS通知APIが利用できない場合はターミナル出力にフォールバックします。

# 設計方針
- 実在するAPIのみを利用し、クロスプラットフォーム対応を重視
- 通知内容は十分なバリエーションを確保し、毎回新鮮な驚きを提供
- 履歴管理・集計・即時通知など、CLIサブコマンドで柔軟に運用可能