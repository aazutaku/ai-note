# 概要
このSkillは、OS通知APIを活用し、ユーザーの作業中に意図的な“現実逃避”を促すカオスな演出を目的としています。通知内容は完全ランダムで、ユーモアと実用性を両立します。

# 公式ドキュメント抜粋
- [notify-send (Linux)](https://specifications.freedesktop.org/notification-spec/notification-spec-latest.html)
- [osascript (macOS)](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/introduction/ASLR_intro.html)
- [win10toast (Windows)](https://pypi.org/project/win10toast/)

# 利用例
- チームの気分転換タイムに
- 長時間作業のリマインダーとして
- ランダムな演出で会話のネタに

# 注意点
- 通知はローカル環境のみ。外部送信なし。
- 履歴はユーザーディレクトリ配下に保存。
- 依存: Linux/macOSは標準コマンド、Windowsは`win10toast`が必要。

# 設計方針
- シンプルな構成で安全性を担保
- 通知内容は5パターン以上、今後拡張も容易
- CLIサブコマンドで柔軟な運用を可能に