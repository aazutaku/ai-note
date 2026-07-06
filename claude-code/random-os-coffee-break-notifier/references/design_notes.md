# 概要
本Skillは、作業中に“OS公式っぽい”通知でコーヒーブレイクを理不尽に推奨することで、ユーザーの気分転換やユーモア演出を狙っています。通知内容とタイミングは完全ランダムです。

# 公式ドキュメント抜粋
- Python subprocess: https://docs.python.org/ja/3/library/subprocess.html
- macOS osascript: https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/introduction/ASLR_intro.html
- Linux notify-send: https://specifications.freedesktop.org/notification-spec/notification-spec-latest.html

# 利用例
- `/random-os-coffee-break-notifier notify -n 2` で2回連続通知
- `/random-os-coffee-break-notifier auto --min 600 --max 1200` で10-20分間隔で3回通知

# 注意点
- 通知はジョーク目的であり、健康や生産性を保証しません
- OS通知APIが利用できない環境では標準出力にメッセージを表示します
- 履歴や個人情報の保存はありません

# 設計方針
- OSごとに最適な通知APIを自動選択
- 通知内容は毎回ランダム、タイミングもランダム
- 実害やデータ損失を一切発生させない安全設計