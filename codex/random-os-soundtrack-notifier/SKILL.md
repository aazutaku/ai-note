---
name: random-os-soundtrack-notifier
description: ターミナルやエディタの起動時、または /skills menu など明示呼び出し時に、作業開始BGMとしてバカバカしい楽曲タイトルをOS通知でランダム表示。trigger: always, semantic-or-explicit。
---

# 機能概要
このSkillは、ターミナルやエディタを起動した瞬間に「今日の作業BGM」として、思わず二度見するようなバカバカしい楽曲タイトルをOS通知で提案します。選曲は完全ランダムで、ジャンルも統一感がなく、『情熱大陸』『運命』『初音ミクの消失』『ドラクエ戦闘曲』『朝のラジオ体操』など、思わず「本当にこれ流すの？」と突っ込みたくなるラインナップです。実際に音楽が流れることはありませんが、毎日の作業開始時にちょっとした笑いと意外性を提供します。

# 使い方
- 明示的な呼び出し例: `/skills menu` または `random-os-soundtrack-notifier` のメンション
- 暗黙発動キーワード例: 「エディタ起動」「ターミナル開始」「作業開始」などのタイミングで自動発動

# 出力例
```
[通知] 今日の作業BGM: 『情熱大陸』
[通知] 今日の作業BGM: 『初音ミクの消失』
[通知] 今日の作業BGM: 『運命（ベートーヴェン）』
[通知] 今日の作業BGM: 『ドラクエ戦闘曲』
[通知] 今日の作業BGM: 『朝のラジオ体操 第一』
[通知] 今日の作業BGM: 『NHKニュースのテーマ』
```

# 注意点
- 実際に音楽は再生されません。通知のみです。
- OSの通知機能（macOS: `osascript`, Linux: `notify-send`, Windows: `toast`等）に依存します。
- 通知が出ない場合はOS側の通知設定をご確認ください。
- 楽曲リストはスクリプト内で編集可能です。

# 参考資料
- references/design_notes.md
- https://docs.python.org/ja/3/library/subprocess.html
- https://github.com/notify2/notify2 (Linux通知)
- https://docs.microsoft.com/ja-jp/windows/uwp/design/shell/tiles-and-notifications/