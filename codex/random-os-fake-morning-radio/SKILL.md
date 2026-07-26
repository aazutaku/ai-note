---
name: random-os-fake-morning-radio
description: 作業開始直後や『おはよう』『start work』などのキーワード、または明示的なSkill呼び出し時に、OS風ラジオDJトークや意味不明なOSニュースを通知・ターミナル出力します。日替わりで無駄な実況やゴシップが流れ、開発現場に笑いと活気を注入します。
---

# 機能概要
このSkillは、作業開始時や任意のタイミングで、まるで謎のOS内蔵ラジオ番組のようなメッセージを通知やターミナルに流します。内容は『本日のOS天気予報』『バグ修正応援メッセージ』『OS業界ゴシップ』など、完全に無駄で意味不明なラジオDJトーク。開発現場の朝をカオスに盛り上げ、笑いと活気を生み出します。

# 使い方
- 明示呼び出し: `/skills random-os-fake-morning-radio` または Skillメニューから選択
- 暗黙発動: 「おはよう」「start work」「今日もよろしく」などの開始系キーワード入力時や、作業開始直後に自動発動
- オプション: `--notify` でデスクトップ通知、`--terminal` でターミナル出力（デフォルトは両方）

# 出力例
```
[OS Morning Radio] おはようございます！本日のOS天気予報：カーネルの空は快晴、バグの雲がちらほら。
[OS Morning Radio] 業界ゴシップ：昨日、メモリ管理部が寝坊した模様です。
[OS Morning Radio] 今日も元気にバグを直しましょう！
[OS Morning Radio] 本日のラッキーコマンド：sudo reboot（実行は自己責任で）
[OS Morning Radio] DJ: システムログに愛を込めて。
```

# 注意点
- 本Skillは実際のOSやシステムには一切影響しません
- ローカルに履歴を保存しません
- 通知機能はLinux/macOSの`notify-send`/`osascript`を利用（Windowsはターミナル出力のみ）
- 業務外の無駄な情報が含まれます

# 参考資料
詳細な設計方針や利用例は `references/design_notes.md` を参照してください。公式通知API:
- [notify-send (Linux)](https://specifications.freedesktop.org/notification-spec/latest/)
- [osascript (macOS)](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/introduction/ASLR_intro.html)