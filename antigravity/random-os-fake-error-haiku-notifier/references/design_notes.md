# 概要
このSkillは、エラー発生時に開発者の緊張感を和らげることを目的とし、通知内容を完全に俳句に限定しています。俳句は日本語でランダムに選ばれ、実際のエラー内容とは無関係です。

# 公式ドキュメント抜粋
- Python subprocess: https://docs.python.org/3/library/subprocess.html
- notify-send: https://wiki.archlinux.jp/index.php/Notify-send
- win10toast: https://github.com/jithurjacob/Windows-10-Toast-Notifications

# 利用例
- ターミナルでビルドエラーやテスト失敗時に自動で俳句通知
- GUIエディタのエラー検知イベントに連動

# 注意点
- 通知はOS標準APIのみを利用し、外部サービス送信やログ保存は行いません。
- 通知が多発する場合は間隔制御（0.5秒sleep）でスパム化を防止しています。
- 俳句の内容は固定リストからランダム選択。追加カスタムも可能です。

# 設計方針
- OS横断的な通知実装（macOS, Linux, Windows）
- 明示呼び出し不要、エラーイベントに自動反応
- 俳句通知は短時間で消え、作業を妨げない