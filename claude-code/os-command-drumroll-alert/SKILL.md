---
name: os-command-drumroll-alert
description: このSkillは、git push、rm、npm publish、docker pushなどの重大コマンド検知時、直前にドラムロール音とOS通知で“運命の選択”を演出します。コマンド実行前の緊張感を高め、重大操作のミス防止や気分転換にも役立ちます。
---

# 機能概要
`os-command-drumroll-alert`は、ターミナルやエディタで重大コマンド（例: `git push`, `rm -rf`, `npm publish`, `docker push`など）が実行される直前に、OS風のドラムロール音を鳴らし、デスクトップ通知で「本当にやるのか？」「運命の選択が迫る！」などの演出を自動的に挿入するSkillです。普段の作業が一気に壮大なイベントに変わり、エンジニアの心拍数を無駄に上げてくれます。ミス防止や気分転換、作業のリズムチェンジにも有効です。

# 使い方
- 明示呼び出し: `/os-command-drumroll-alert "git push"`
- 暗黙発動: `git push`, `rm -rf`, `npm publish`, `docker push` などのコマンド入力直前に自動発動（semantic trigger）。
- カスタムコマンド登録も可能。

# 出力例
```
[ドラムロール音が鳴る]
[通知] 今から本当に "git push" を実行しますか？
[通知] 運命の選択が迫る！
[通知] ドラマチックな瞬間に突入します。
(3秒後)
[INFO] コマンド "git push" を実行します。
```

# 注意点
- ドラムロール音はOS標準または内蔵WAVファイルを使用。
- 通知はOSの通知API（Windows: Toast, macOS: AppleScript, Linux: notify-send）を自動判別。
- 重大コマンド以外には発動しません。
- ローカルでのみ動作。通知や音声が不要な場合は環境変数で無効化可。

# 参考資料
- [Python playsound](https://github.com/TaylorSMarks/playsound)
- [notify2 (Linux通知)](https://pypi.org/project/notify2/)
- [Windows Toast通知](https://docs.microsoft.com/en-us/windows/uwp/design/shell/tiles-and-notifications/send-local-toast)
- references/design_notes.md も参照