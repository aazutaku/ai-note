# 概要
このSkillは、開発者の作業現場にユーモアと知的混乱をもたらすため、完全に無関係な“古文調”の詩をOS通知やターミナルに表示するものです。内容は作業やエラーと無関係で、集中力を和らげる効果を狙っています。

# 公式ドキュメント抜粋
- [notify-send (Linux)](https://specifications.freedesktop.org/notification-spec/latest/)
- [osascript (macOS)](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/introduction/ASLR_intro.html)
- [win10toast (Windows)](https://pypi.org/project/win10toast/)

# 利用例
- 長時間作業中のリフレッシュや、チーム内での話題作りに。
- /skills menuや明示的な呼び出しで、いつでも発動可能。

# 注意点
- 通知内容は完全ランダムで、実際のシステム状態やエラーとは無関係です。
- OS通知APIが利用できない場合はターミナル出力にフォールバックします。
- 履歴はユーザーのホームディレクトリに保存されますが、個人情報やコード内容は含みません。

# 設計方針
- OSごとの通知APIを自動判別し、失敗時は標準出力に切り替えます。
- サブコマンドで履歴閲覧や発動回数要約も可能とし、CLIツールとしても活用できます。