---
name: os-fake-coffee-break-sound-effect
description: このSkillは、Claude Codeがコマンド実行や作業の節目（例: ビルド/テスト/デプロイ/長時間作業）を検知した際や、/os-fake-coffee-break-sound-effect の明示呼び出し時に発動します。通知・サウンド演出を通じて“強制コーヒーブレイク”を演出します。
---

# 機能概要
このSkillは、作業中やコマンド実行時に、まるでOSが“コーヒーブレイクを強制したい”かのような、謎のサウンド演出とデスクトップ通知を自動で発動します。通知文は「あなたの集中はカフェイン不足です」「今こそ一服の時」など完全ランダム。サウンドもコーヒー抽出音やカップを置く音など複数から選ばれ、開発現場に突如“休憩ムード”をねじ込みます。作業リズムを愉快に撹乱したい時や、チームの雰囲気を和ませたい時に最適です。

# 使い方
- 明示呼び出し: `/os-fake-coffee-break-sound-effect`
- 暗黙発動: 「ビルド」「テスト」「デプロイ」「run」「長時間作業」などのコマンドや作業イベントを検知して自動発動
- 設定不要、スクリプトを実行するだけで利用可能

# 出力例
```terminal
[通知] 今こそ一服の時
[サウンド] ./sounds/coffee_pour.wav を再生中...
[通知] あなたの集中はカフェイン不足です
[サウンド] ./sounds/cup_put.wav を再生中...
[通知] マシンも休みたい気分
[サウンド] ./sounds/coffee_machine.wav を再生中...
```

# 注意点
- サウンド再生には `playsound` パッケージ、通知には `plyer` を使用します。
- 音源ファイルは `./sounds/` ディレクトリに保存されています。
- サポートOS: Windows/macOS/Linux（通知機能は一部環境で制限あり）
- 音量や通知頻度の細かい調整は未対応です。

# 参考資料
- [playsound公式](https://github.com/TaylorSMarks/playsound)
- [plyer通知API](https://plyer.readthedocs.io/en/latest/)
- references/design_notes.md 参照