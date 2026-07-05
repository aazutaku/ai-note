# 概要
本Skillは、ユーザーの作業環境に突如として「OSの人格が変わった」と宣言する通知を送り、シュールな演出体験を提供します。通知内容は完全ランダムで、実際のOSや作業には一切影響しません。

# 公式ドキュメント抜粋
- Linux: `notify-send` (Freedesktop.org Notification Spec)
- macOS: `osascript` (AppleScriptによる通知)
- Windows: `win10toast` (Pythonパッケージ)

# 利用例
- `/skills random-os-sentiment-shift-alert alert` で即座にランダム通知
- `/skills random-os-sentiment-shift-alert list` で過去の通知履歴を確認
- `/skills random-os-sentiment-shift-alert summary` で履歴サマリ表示

# 注意点
- 通知は一時的で、OSやファイル、作業内容には変更を加えません。
- Windowsでは`win10toast`が必要です。インストールされていない場合はpipで追加してください。
- 履歴はホームディレクトリの隠しファイルに保存されます。

# 設計方針
「何も変わらないのに本気で通知だけが来る」不条理さ・脱力感を追求。通知内容は20種類以上のキャラクター変化からランダム生成し、複数回実行しても飽きないよう工夫しています。