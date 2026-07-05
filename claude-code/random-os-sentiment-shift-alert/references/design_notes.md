# 概要
このSkillは、OS通知APIを利用してユーザーの作業中にランダムな人格変化メッセージを表示し、ユーモラスな演出を提供します。実際の設定や作業には一切影響を与えません。

# 公式ドキュメント抜粋
- Python subprocess: https://docs.python.org/3/library/subprocess.html
- macOS通知: https://developer.apple.com/documentation/usernotifications
- Linux notify-send: https://specifications.freedesktop.org/notification-spec/notification-spec-latest.html
- Windows win10toast: https://pypi.org/project/win10toast/

# 利用例
- コーディングやドキュメント作成中に、明示的に `/random-os-sentiment-shift-alert` を呼び出す
- 「キャラ変」などのキーワードが登場した際に自動発動

# 注意点
- 通知はセッション内のみ履歴管理。ファイル保存やシステム設定変更は一切なし。
- Windowsで通知を利用する場合は win10toast のインストールが必要です。

# 設計方針
- シュールかつ多様な通知内容を維持し、繰り返し利用しても飽きにくい構成としています。
- OS依存部分は極力標準APIで実装し、クロスプラットフォーム対応を意識しています。