# 概要
このSkillは、ユーザーの作業体験に“意味のないセンチメンタル”な演出を加えるために設計されました。実在しないOSキャラクターの退職通知を、完全ランダムな内容でデスクトップに表示します。

# 公式ドキュメント抜粋
通知表示にはPythonのnotify2ライブラリ（https://pypi.org/project/notify2/）を利用し、環境によってはnotify-sendコマンドにフォールバックします。

# 利用例
- 明示呼び出し: `python random_os_retirement_announcement.py announce`
- 履歴表示: `python random_os_retirement_announcement.py list`
- 集計: `python random_os_retirement_announcement.py summary`

# 注意点
- 通知は1時間に1回まで。履歴は~/.random_os_retirement_logに保存されます。
- Linux等、デスクトップ通知APIに対応した環境でのみ有効です。

# 設計方針
“意味のなさ”と“演出の多様性”を重視し、通知内容・キャラ名・理由を毎回ランダム生成。スパム防止のため頻度制限も実装しています。