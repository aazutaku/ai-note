# 概要
本Skillは、ユーザーの作業中に意図的な緊張緩和や盛り上げ演出を目的とした、完全フェイクのOS風ズームイン警告通知をランダムに表示します。実際の画面ズームやシステム操作は一切発生しません。

# 公式ドキュメント抜粋
- PythonでのOS通知API利用例: [notify-send (Linux)](https://wiki.archlinux.jp/index.php/Notify-send)、[osascript (macOS)](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/introduction/ASLR_intro.html)、[win10toast (Windows)](https://pypi.org/project/win10toast/)

# 利用例
- オンライン会議やイベントでのアイスブレイク
- 長時間作業時の気分転換やジョーク演出
- チーム内での「謎のOS警告」ネタとして活用

# 注意点
- 本Skillはシステムに実害を与えませんが、通知内容が紛らわしいため、誤解を招く環境では利用を控えてください。
- デスクトップ通知はOS依存のため、Linux/macOS/Windowsで動作確認済みですが、環境によっては追加パッケージ（例: win10toast）が必要です。

# 設計方針
- CLIサブコマンド(run/list)で柔軟な利用を実現
- 通知間隔・通知方法のカスタマイズ性を重視
- すべての通知はランダム生成・履歴保存なし