---
name: random-os-fake-boot-sound
description: ターミナルやエディタの起動、または /random-os-fake-boot-sound コマンド実行時に、ローカルのwav/mp3から毎回ランダムな“謎のOS起動音”を再生します。起動・開始・新規セッション・起動音・サウンドなどのキーワードで自動発動します。
---

# 機能概要
このSkillは、作業開始時やターミナル/エディタの起動時に、毎回ランダムな“謎のOS起動音”を再生する演出スキルです。音源はユーザーが用意したwav/mp3ファイルをローカルディレクトリに配置するだけ。懐かしいPC起動音から、バカバカしい効果音まで、バリエーション豊かな音で毎回違う“どこかのOS”気分を味わえます。実用性はほぼゼロですが、作業開始の気分転換やネタ演出に最適です。

# 使い方
- 明示呼び出し例: `/random-os-fake-boot-sound` をコマンドパレットやターミナルで実行
- 暗黙発動: "起動", "開始", "ターミナル", "エディタ", "boot", "sound" などのキーワードや、セッション開始時に自動実行
- 音源ファイルは `.claude/skills/random-os-fake-boot-sound/sounds/` 配下に wav/mp3 で複数配置してください

# 出力例
```
$ /random-os-fake-boot-sound
[INFO] サウンド候補: 6件
[INFO] 選択: mysterious_boot_3.wav
[PLAY] 再生中...
(音が鳴る)
```

# 注意点
- 音源ファイルはローカル保存のみ対応。ネットワーク越しのストリーミング再生は未対応です。
- サウンドファイルはwav/mp3のみ対応。数が多いほどランダム性が高まります。
- 音量や再生デバイスはOSの設定に依存します。
- スクリプトはPython 3.7以上、`playsound`または`pydub`/`simpleaudio`が必要です。

# 参考資料
詳細な設計方針や参考リンクは `references/design_notes.md` を参照してください。公式ドキュメント: [playsound](https://github.com/TaylorSMarks/playsound), [pydub](https://github.com/jiaaro/pydub)