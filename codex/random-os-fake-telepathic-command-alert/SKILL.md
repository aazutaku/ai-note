---
name: random-os-fake-telepathic-command-alert
description: このSkillは、ユーザーがコマンド入力や作業中に“念波”や“心の声”をOSが検出したかのようなフェイク通知をランダムに表示します。明示的な呼び出し（/skills menuやskill名メンション）や、作業進行・コマンド実行などのsemantic trigger時に発動します。
---

# 機能概要
`random-os-fake-telepathic-command-alert`は、作業やコマンド実行の合間に「OSがあなたの心の中のコマンドを検出した」とする、完全に架空の通知をランダムで表示するSkillです。実際には存在しないコマンドや妄想的な操作内容を、あたかもOSが読心術で察知したかのように演出します。真面目な作業空間に突如現れる不条理な通知で、現実逃避や笑いを提供し、作業の合間のリフレッシュやチーム内のアイスブレイクにも活用できます。

# 使い方
- 明示呼び出し例: `/skills menu` から本Skillを選択、または `@random-os-fake-telepathic-command-alert` で直接発動
- 暗黙発動例: コマンド実行直後、長時間入力なし、または「deploy」「build」「coffee」などのキーワードを含む作業時に自動発動

# 出力例
```
[Telepathic OS Alert]
あなたが心の中で考えたコマンドを検出しました: 'make coffee'

[Telepathic OS Alert]
念波検出: 'deploy to mars'

[Telepathic OS Alert]
思念コマンド捕捉: 'sudo fix all bugs instantly'

[Telepathic OS Alert]
OSがあなたの夢を感知しました: 'take a nap'

[Telepathic OS Alert]
未知の念波: 'hack time itself'
```

# 注意点
- 実際のコマンドやファイル操作は一切行いません
- 通知内容は毎回ランダム生成され、実行・保存・履歴等は残りません
- ローカル通知API（Linux: notify-send, macOS: osascript, Windows: Toast通知）を利用
- チームや共有環境での利用時は、混乱を避けるため周知推奨

# 参考資料
- references/design_notes.md
- [Linux notify-send](https://specifications.freedesktop.org/notification-spec/latest/)
- [macOS osascript](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/introduction/ASLR_intro.html)
- [Windows Toast Notifications](https://learn.microsoft.com/en-us/windows/uwp/design/shell/tiles-and-notifications/toast-notifications)