# 概要
このSkillは、実際のOSやファイルシステムへ影響を与えず、標準出力や（オプションで）デスクトップ通知を通じて“架空のロックダウン”を演出します。職場の雰囲気を和ませるためのジョーク用途を主眼としています。

# 公式ドキュメント抜粋
- notify-send: https://specifications.freedesktop.org/notification-spec/latest/
- osascript (macOS): https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/introduction/ASLR_intro.html
- win10toast: https://github.com/jithurjacob/Windows-10-Toast-Notifications

# 利用例
- `/skills menu` から明示呼び出し
- コマンド: `python random_os_fake_lockdown_alert.py alert --desktop`
- 会話内で「ロック」「凍結」等の単語が出た際の自動発動

# 注意点
- 実ファイルやシステムには一切作用しません
- デスクトップ通知は環境依存で動作しない場合もあります
- 業務の妨げにならない範囲でご利用ください

# 設計方針
- 完全ランダム生成による“非現実的”な通知内容
- ユーザーの安全・安心を最優先に設計
- OSごとの通知APIをラップし、失敗時は標準出力にフォールバック
