---
name: os-command-drumroll-alert
description: git push、rm、npm publish、docker push などの重大コマンド実行直前に、必ずドラムロール演出とOS通知を発動。コマンド実行前の緊張感を演出したい時に発動。
---

# 機能概要
このSkillは、エンジニアがターミナルやエディタで重大なコマンド（例: `git push`, `rm -rf`, `npm publish`, `docker push` など）を実行する直前に、OS風のドラムロールサウンドとともに、デスクトップ通知で「本当に実行しますか？」や「運命の選択が迫る！」などの演出メッセージを表示します。普段の作業を一大イベントに昇華し、コマンド実行時の緊張感や注意喚起を高めます。演出は毎回ランダムで変化し、作業のマンネリ化を防ぎます。

# 使い方
- 明示呼び出し: `/skills os-command-drumroll-alert` または Skillメニューから選択
- 暗黙発動: `git push`, `rm`, `npm publish`, `docker push` などのコマンド入力直前に自動発動
- CLIから: `python drumroll_alert.py --command "git push"` のようにコマンド名を渡すと演出

# 出力例
```
[DRUMROLL] ドラムロール再生中...
[NOTIFY] 今から「git push」を実行します。本当に進めますか？
[DRUMROLL] ドラムロール終了！
[NOTIFY] 運命の選択が迫る！
[INFO] コマンド「git push」を続行してください。
```

# 注意点
- サウンド再生にはOSの標準音声プレイヤーを利用します（Linux: aplay/paplay, macOS: afplay, Windows: powershell）。
- 通知は`notify-send`(Linux), `osascript`(macOS), `powershell`(Windows)を使用。環境によっては追加インストールが必要です。
- コマンド実行自体はこのSkillでは行いません。演出後に手動でコマンドを入力してください。
- ローカル環境でのみ動作。リモートやWeb環境では制限があります。

# 参考資料
- [notify-send](https://specifications.freedesktop.org/notification-spec/latest/)
- [Python playsound](https://github.com/TaylorSMarks/playsound)
- references/design_notes.md も参照