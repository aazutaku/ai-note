# 概要
このSkillは、ユーザーの作業中に“OS公式風”の404ジョーク通知をランダムなタイミングで表示することで、気分転換やコミカルな演出を提供します。通知は実際のエラーとは明確に区別される文言を用い、誤解を防止します。

# 公式ドキュメント抜粋
- [notify-send (Linux)](https://specifications.freedesktop.org/notification-spec/latest/)
- [osascript (macOS)](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/introduction/ASLR_intro.html)
- [win10toast (Windows)](https://pypi.org/project/win10toast/)

# 利用例
- 長時間作業中のリマインダーとして
- チームのアイスブレイクや雑談用
- ターミナルやデスクトップでの気分転換

# 注意点
- 通知が本物のシステムエラーと誤認されないよう、文言・タイトルは工夫しています。
- OSごとの通知APIに依存するため、Linux/macOS/Windowsで動作確認済みですが、追加パッケージが必要な場合があります。

# 設計方針
- ジョーク性・非日常感を重視し、通知頻度や内容はランダム性を最大化。
- 明示呼び出しとキーワード検出の両方に対応し、柔軟なトリガー設計としています。