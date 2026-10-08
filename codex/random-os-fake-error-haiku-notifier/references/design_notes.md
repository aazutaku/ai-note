# 概要
random-os-fake-error-haiku-notifierは、CLIや作業ログに現れるエラー/バグ関連ワードをトリガーとして、俳句形式のジョーク通知を行うSkillです。技術用語と季語を組み合わせることで、開発現場にユーモアと癒しをもたらします。

# 公式ドキュメント抜粋
- [notify-send (Linux)](https://specifications.freedesktop.org/notification-spec/latest/)
- [osascript (macOS)](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/introduction/ASLR_intro.html)

# 利用例
- `cat error.log | python random_os_fake_error_haiku_notifier.py monitor --mode both`
- `python random_os_fake_error_haiku_notifier.py run --mode desktop`

# 注意点
- 実際の障害監視や運用通知には使用しないこと。
- Windowsではデスクトップ通知非対応（ターミナル出力のみ）。
- 通知が多すぎる場合は--freqや--intervalで調整可能。

# 設計方針
- 五・七・五の構造を厳守しつつ、毎回異なる俳句を生成。
- OSごとに最適な通知APIを選択。
- Skill本体は100行超のPythonスクリプトでCLI/監視モード両対応。