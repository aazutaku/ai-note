---
name: random-os-mystery-boss-pop
description: 作業中の集中やリマインダー、息抜きが必要なタイミング（例: 長時間作業・休憩忘れ・集中力低下など）に、ランダム生成の“謎OSボスキャラ”が画面端やデスクトップに突如現れ、ユニークな命令や警告を通知します。発動キーワード: ボス, 急襲, 休憩, ストレッチ, 魔王, 集中, OS演出。
---

# 機能概要
このSkillは、作業中のあなたのデスクトップや画面端に“謎のOSボスキャラ”が突如出現し、カオスな命令や警告をランダムに発します。ボスキャラのビジュアルやセリフは毎回ランダム生成され、例えば「緊急任務：今すぐストレッチせよ」や「本日は残業魔王が降臨中」など、妙に的外れな演出で集中力を試します。作業の合間に意外性と遊び心をもたらし、リフレッシュや注意喚起に役立ちます。

# 使い方
明示的な呼び出しは `/random-os-mystery-boss-pop` コマンドで実行します。また、「ボス」「魔王」「ストレッチ」「集中」などのキーワードを含むプロンプトや作業ログからも自動発動します。通知はOSのネイティブ通知機能を使い、画面端やデスクトップにポップアップ表示されます。

# 出力例
```
[通知] 謎のOSボス「メモリ喰らい魔王」が出現！
命令: 今すぐ椅子から立ち上がり、3回回転せよ！
---
[通知] ボス「ディスク断捨離伯爵」からの警告:
「ファイル整理を怠る者に明日はない！」
---
[通知] 新たな刺客「プロセス暴走忍者」参上！
任務: 10秒間、目を閉じて深呼吸！
```

# 注意点
- 本Skillは通知のみを行い、ファイルやシステム設定には一切変更を加えません。
- ローカル環境の通知API（Windows: Toast, macOS: AppleScript, Linux: notify-send）を利用します。
- 画像や音声演出は含みません（テキスト通知のみ）。
- 業務用端末や集中必須の場面ではご注意ください。

# 参考資料
- references/design_notes.md に設計方針・通知APIの解説を記載
- 公式: [Windows Toast Notification](https://learn.microsoft.com/en-us/windows/uwp/design/shell/tiles-and-notifications/send-local-toast)
- 公式: [AppleScript display notification](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/reference/ASLR_display.html)
- 公式: [notify-send (Linux)](https://man7.org/linux/man-pages/man1/notify-send.1.html)