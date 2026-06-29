---
name: random-os-fake-boot-sound
description: ターミナルやエディタの起動時、または /skills menu や random-os-fake-boot-sound への明示呼び出し時に、毎回ランダムなサウンド（wav/mp3）が再生されます。triggerType: semantic-or-explicit。
---

# 機能概要
random-os-fake-boot-soundは、あなたの作業開始時（ターミナルやエディタ起動時など）に、毎回ランダムな“謎のOS起動音”を再生するSkillです。サウンドはローカルのwav/mp3ファイルから選ばれ、懐かしいPCの起動音風から、バネ音・カラスの鳴き声・意味不明な電子音までバリエーション豊か。作業開始の雰囲気を一新し、まるで“どこかの知らないOS”にいるような体験を演出します。

# 使い方
- 明示呼び出し例: `/skills menu` でSkill一覧から選択、または `$ random-os-fake-boot-sound` を直接実行。
- 暗黙発動キーワード例: 「エディタ起動」「ターミナル起動」「新規セッション開始」などのイベント時に自動発動。
- サウンドファイルは `.agents/skills/random-os-fake-boot-sound/sounds/` 配下に任意のwav/mp3を配置してください。

# 出力例
```
[INFO] Boot sound files found: 7
[INFO] Selected: mysterious_beep.mp3
[PLAY] Now playing: mysterious_beep.mp3
[OK] Boot sound playback finished.
```

# 注意点
- サウンドファイルはローカル保存が必要です（著作権に注意）。
- 音源の追加・差し替えは `sounds/` フォルダにファイルを置くだけ。
- OSによって一部音声再生機能が制限される場合があります。
- 実用性はありません。混乱や驚きを演出するためのSkillです。

# 参考資料
- 公式Pythonドキュメント: [playsound](https://pypi.org/project/playsound/), [os](https://docs.python.org/ja/3/library/os.html), [random](https://docs.python.org/ja/3/library/random.html)
- 詳細設計・注意事項は references/design_notes.md を参照してください。