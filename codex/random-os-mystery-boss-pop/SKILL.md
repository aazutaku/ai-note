---
name: random-os-mystery-boss-pop
description: 作業中の集中力が高まったタイミングや、/skills menu コマンド、または『ボス』『警告』『ストレッチ』などのキーワードを含む会話で発動。カオスなOSボスキャラ通知をデスクトップや画面端に表示します。
---

# 機能概要
このSkillは、作業中に突如“謎のOSボスキャラ”が現れ、デスクトップや画面端に奇妙な命令や警告をポップアップ通知で表示します。ボスキャラは毎回ランダム生成され、セリフもカオスに変化。集中しすぎている時や、長時間作業の合間に意外性のある演出を加えて、ユーザーの気分転換やストレッチ喚起を促します。通知はシステムに影響を与えず、純粋な演出として楽しめます。

# 使い方
- 明示呼び出し例: `/skills menu` から skill を選択、または `random-os-mystery-boss-pop` を直接呼び出し。
- 暗黙発動キーワード例: 「ボス」「警告」「ストレッチ」「魔王」「集中力」「休憩」などの単語を含む会話やコマンドで自動発動。

# 出力例
```
[画面右下通知]
【降臨：メモリ喰いのバグ魔王】
緊急任務：今すぐ椅子から立ち上がり、3回ジャンプせよ！

[画面中央ポップアップ]
【出現：CPUオーバーロード伯爵】
警告：本日は残業魔王が降臨中。集中力を維持できるか？

[端末出力]
Mystery Boss: SSDトロールが現れた！「今すぐストレッチせよ」
```

# 注意点
- 本Skillは通知演出のみで、ファイルやシステム設定には一切変更を加えません。
- ローカルの通知API（Windows: Toast, macOS: AppleScript, Linux: notify-send）を使用。
- 一部環境では通知が非対応の場合あり。
- 履歴やボスキャラの記録はローカル保存されません。

# 参考資料
- [Windows Toast Notifications](https://docs.microsoft.com/en-us/windows/uwp/design/shell/tiles-and-notifications/toast-notifications)
- [AppleScript display notification](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/reference/ASLR_cmds.html)
- [notify-send man page](https://man7.org/linux/man-pages/man1/notify-send.1.html)
- references/design_notes.md 参照