# 概要
このSkillは、作業中や会議中に架空のOSアップデート通知を表示し、場を和ませたり、集中力をリセットするためのジョーク系演出ツールです。通知内容は完全にランダムで、実際のシステムや業務には一切影響しません。

# 公式ドキュメント抜粋
- Python subprocess: https://docs.python.org/3/library/subprocess.html
- notify-send (Linux): https://specifications.freedesktop.org/notification-spec/notification-spec-latest.html
- osascript (macOS): https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/introduction/ASLR_intro.html

# 利用例
- オンライン会議中に突然通知を表示して場を和ませる
- コーディング中に集中しすぎた時のリフレッシュ
- 仲間内でのジョークやアイスブレイク

# 注意点
- 本Skillは業務用途や真面目な通知には絶対に使わないでください
- 通知内容が現実のOS通知と誤認されないよう「fake」や「ジョーク」等の文言を明示
- 通知履歴や個人情報は一切保存されません

# 設計方針
- OSごとに標準APIで通知を表示（Linux: notify-send, macOS: osascript, Windows: powershell）
- 通知内容は毎回ランダム生成
- 誤認防止のため必ず「fake」表示
- CLIサブコマンドで明示的な呼び出し・サンプル表示・概要確認が可能