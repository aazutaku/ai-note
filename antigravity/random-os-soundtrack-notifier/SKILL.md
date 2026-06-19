---
name: random-os-soundtrack-notifier
description: ターミナルやエディタの起動時、または作業開始を示唆するキーワード（例: start, open, begin, code, terminal）が検出された際に、AntigravityがこのSkillを自動発動します。
---

# 機能概要
random-os-soundtrack-notifierは、作業開始時に“今日の作業BGM”として、ジャンルも状況も無視した奇妙なサウンドトラック名をOS通知で表示します。通知されるだけで実際には音楽は流れません。『情熱大陸』『運命』『初音ミクの消失』『ドラクエ戦闘曲』『朝のラジオ体操』など、思わず二度見するバカバカしいラインナップが特徴です。日々の作業開始にユーモアを添え、気分転換や話題作りをサポートします。

# 使い方
このSkillは明示的な呼び出しを必要とせず、ターミナルやエディタの起動、または“start”“open”“begin”“code”“terminal”などのキーワードを含む状況で自動発動します。手動実行は不要です。

# 出力例
```
[通知] 今日の作業BGM: ドラクエ戦闘曲
[通知] 今日の作業BGM: 情熱大陸
[通知] 今日の作業BGM: 初音ミクの消失
[通知] 今日の作業BGM: 運命（ベートーヴェン）
[通知] 今日の作業BGM: 朝のラジオ体操
[通知] 今日の作業BGM: ルパン三世のテーマ
[通知] 今日の作業BGM: ポケモンセンター
[通知] 今日の作業BGM: 甲子園応援歌
```

# 注意点
- 実際に音楽は再生されません。通知のみです。
- 通知はOSのネイティブAPIを利用します（Windows: Toast, macOS: AppleScript, Linux: notify-send）。
- 通知がOSの設定でブロックされている場合は表示されません。
- 選曲リストはローカル保存やカスタマイズ不可です。
- セキュリティ上、外部APIやインターネットアクセスは行いません。

# 参考資料
- [Python公式: platform, subprocess, random, os](https://docs.python.org/3/library/)
- references/design_notes.md を参照してください。