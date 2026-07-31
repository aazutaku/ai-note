# 概要
random-os-karaoke-alertは、ユーザーの作業中に完全ランダムなタイミングでユーモラスなカラオケ推奨通知を表示するスキルです。現実逃避や気分転換を促し、作業環境に遊び心を加えます。

# 公式ドキュメント抜粋
- plyer通知API: https://plyer.readthedocs.io/en/latest/
- macOS通知: https://ss64.com/osx/osascript.html
- Linux notify-send: https://specifications.freedesktop.org/notification-spec/latest/

# 利用例
- 明示呼び出し: `python random_os_karaoke_alert.py alert`
- バックグラウンド: `python random_os_karaoke_alert.py loop --min 300 --max 900`
- 履歴確認: `python random_os_karaoke_alert.py list`

# 注意点
- 通知はローカル環境のみに表示され、外部送信やシステム設定変更は行いません。
- plyer未導入の場合はOS標準通知APIを利用、それも不可ならコンソール出力にフォールバックします。

# 設計方針
- 完全なランダム性と多様な通知文で飽きさせない体験を重視
- 履歴ログ機能で通知の振り返りや集計も可能
