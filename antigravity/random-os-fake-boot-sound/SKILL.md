---
name: random-os-fake-boot-sound
description: ターミナルやエディタの起動時、または作業開始時などのセッション開始イベント（例: terminal open, editor launch, workspace attach）で自動的に発動し、毎回異なるランダムなサウンドを再生して疑似的な“OS起動音”を演出します。
---

# 機能概要
random-os-fake-boot-sound は、ターミナルやエディタの起動時などに“謎のOS起動音”を毎回ランダムで再生するスキルです。音源はwav/mp3ファイルをローカルに数個用意するだけで、懐かしいPCの起動音から、バネ音・カラスの鳴き声・電子音など多彩な効果音を演出できます。作業開始時に“どこかの知らないOS”にいるような気分を味わえる、実用性ゼロの混乱系演出スキルです。

# 使い方
このSkillは、ターミナルやエディタの起動時（`terminal open`, `editor launch`, `workspace attach` などのセマンティックイベント）で自動的に発動します。音源ファイルは `.agent/skills/random-os-fake-boot-sound/sounds/` ディレクトリにwavまたはmp3形式で保存してください。サウンドは毎回ランダムに選ばれます。音源の差し替えや追加はファイルを置くだけでOKです。

# 出力例
```
[INFO] random-os-fake-boot-sound: サウンドファイルを検索中...
[INFO] 4個の音源を検出: boot98.wav, spring.mp3, crow.wav, mysteryos.mp3
[INFO] 今回の起動音: spring.mp3
[INFO] サウンド再生完了
```

# 注意点
- 音源ファイルはローカル保存のみ対応。ネットワーク経由の再生やストリーミングは未対応です。
- 音量調整や再生デバイスの指定はOS側の設定に依存します。
- サウンド再生にはPythonの `playsound` または `pydub` ライブラリを利用。Linux/Windows/Macで動作しますが、依存パッケージのインストールが必要です。

# 参考資料
詳細な設計方針や参考リンクは `references/design_notes.md` を参照してください。公式APIやサウンド再生の詳細は [playsound公式](https://github.com/TaylorSMarks/playsound) をご覧ください。