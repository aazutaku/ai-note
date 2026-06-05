---
name: random-excuse-notifier
description: ターミナル操作やコマンド実行時、または /random-excuse-notifier 呼び出し時に、OS通知領域へランダムな言い訳メッセージを表示します。notify, excuse, notification, 言い訳 などのキーワードや明示呼び出しで発動。
---

# 機能概要
このSkillは、ターミナルでコマンドを実行した際や明示的に呼び出したとき、OSの通知領域に“全力で無意味な言い訳”をランダム表示します。例えば「ネットが遅い」「今日は水星逆行中」など、作業効率には一切寄与しない、ジョーク的な通知演出を提供します。通知内容は完全ランダムで、繰り返し利用してもネタが被りにくい設計です。作業の合間にクスッと笑いたい方や、真面目な通知に飽きた方に最適です。

# 使い方
- 明示呼び出し例:
  `/random-excuse-notifier`
- 暗黙発動キーワード例:
  - コマンド入力時に「notify」「excuse」「notification」「言い訳」などが含まれている場合
  - ターミナル操作やスクリプト実行時の自動発動

# 出力例
```
$ /random-excuse-notifier
[通知] 今日はキーボードが冷たくて指が動きません。
$ ls
[通知] ネットが遅いから時間かかってます。
$ git push
[通知] すみません、水星逆行中なのでうまくいきません。
$ echo hello
[通知] マウスが反応しませんでした。
$ python script.py
[通知] 今日は月が綺麗ですね。
```

# 注意点
- 通知はOSの標準通知APIを利用します（Linux: notify-send, macOS: osascript, Windows: win10toast）
- ネタは毎回ランダム抽選され、直近の履歴から重複を避けます
- ローカルに履歴ファイルを保存します（.random_excuse_history）
- 通知の内容は業務に全く役立ちません
- サーバ環境や通知API未対応OSでは動作しません

# 参考資料
- [Python公式 subprocess モジュール](https://docs.python.org/ja/3/library/subprocess.html)
- [notify-send (Linux)](https://specifications.freedesktop.org/notification-spec/latest/)
- [osascript (macOS)](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/introduction/ASLR_intro.html)
- references/design_notes.md 参照