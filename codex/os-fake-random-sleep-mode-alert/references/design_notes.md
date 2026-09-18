# 概要
このSkillは、ユーザーの作業中に“OS公式風”の理不尽なスリープ警告通知をランダムに表示することで、作業の息抜きや会話のネタを提供します。実際のシステムスリープや休止状態は一切発生しません。

# 公式ドキュメント抜粋
- Python subprocess: https://docs.python.org/3/library/subprocess.html
- notify-send (Linux): https://specifications.freedesktop.org/notification-spec/latest/
- osascript (macOS): https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/

# 利用例
- チームの雑談タイムやリモートワークの息抜きに
- ターミナルやチャットでの「/skills os-fake-random-sleep-mode-alert」コマンド実行時
- 集中力や作業停滞をネタにしたい場面

# 注意点
- 本Skillはジョーク用途専用です。通知内容は毎回ランダム生成され、実際のスリープ操作は一切行いません。
- 通知はOS標準APIやターミナル出力で実装されていますが、Linux/macOS/Windowsでの動作互換性に注意してください。

# 設計方針
- OS種別ごとに適切な通知APIを選択し、通知が失敗した場合はターミナル出力で代替します。
- 通知内容はハードコードされたリストからランダム選択され、拡張も容易です。
- ログや履歴は一切保存せず、純粋な演出機能に徹しています。