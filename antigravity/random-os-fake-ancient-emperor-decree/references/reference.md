# 概要
このSkillは、作業中にランダムな“古代皇帝の勅令”を通知することで、ユーザーの気分転換やユーモラスな演出を実現します。通知内容は威厳と理不尽さを両立させた完全フィクションです。

# 公式ドキュメント抜粋
- Python subprocess: https://docs.python.org/3/library/subprocess.html
- notify-send (Linux): https://specifications.freedesktop.org/notification-spec/
- osascript (macOS): https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/
- win10toast (Windows): https://pypi.org/project/win10toast/

# 利用例
- 長時間作業中の気分転換や、チーム内の冗談演出に。
- ターミナルやデスクトップで突発的なカオスを演出したいとき。

# 注意点
- 実際のシステムやファイルには一切影響を与えません。
- 通知APIが利用できない環境では標準出力に表示されます。

# 設計方針
- OSごとに適切な通知APIを自動選択。
- 勅令テンプレート・項目・条件・罰則をランダム組み合わせで生成。
- ログや履歴は保存せず、純粋な演出用途に特化。