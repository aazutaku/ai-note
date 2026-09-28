# 概要
このSkillは、開発現場や学習環境に“OS公式っぽいバグ孵化警告”を演出目的で挿入するものです。実害ゼロ・演出専用で、ユーザーの緊張感や話題作り、集中のリセットなどに活用されます。

# 公式ドキュメント抜粋
- Python subprocess: https://docs.python.org/ja/3/library/subprocess.html
- notify-send (Linux): https://specifications.freedesktop.org/notification-spec/notification-spec-latest.html
- osascript (macOS): https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/introduction/ASLR_intro.html

# 利用例
- ペアプロや勉強会で“謎のバグ警告”を話題にする
- 集中しすぎた作業の合間に緊張をほぐす
- デバッグ作業中の“気分転換”やジョークとして

# 注意点
- 実際のエラーやバグ通知と混同しないよう、通知文は明らかに冗談と分かる内容に限定
- OS通知APIが利用できない場合はターミナル出力のみ対応
- ログや履歴は保存しません

# 設計方針
- OSごとの通知APIを標準でサポート
- ランダムタイミング・セマンティックトリガー・明示呼び出しの3系統で発動
- 実在のAPIのみ利用し、架空の関数やCLIは使わない