---
name: random-os-mystery-sound-effect
description: コマンド実行やファイル操作、プロジェクトビルドなどのアクション時に、毎回ランダムな“謎のOS公式サウンドエフェクト”を鳴らすことで、開発現場にシュールな混乱や笑いを演出したい場合に発動します。triggerType: always/semantic。
---

# 機能概要
このSkillは、ターミナルやエディタでコマンド実行のたびに、謎めいた“OS公式サウンドエフェクト”をランダムに再生します。音源は「ファイルが旅立つ音」「やる気起動音」「謎の自動拍手」など、用途や意味が不明なSEばかり。開発現場に突如シュールな混乱をもたらし、集中力を崩壊させるカオスな体験を提供します。通知や演出、OS連携カテゴリに最適です。

# 使い方
- 明示呼び出し: `/random-os-mystery-sound-effect` または `/skill random-os-mystery-sound-effect`
- 暗黙発動: `run`, `build`, `compile`, `test`, `deploy`, `save`, `commit` などのコマンド実行時に自動発動します。

# 出力例
```
$ git commit -m "fix typo"
[謎の自動拍手音が鳴る]
$ make build
[やる気起動音が鳴る]
$ rm -rf tmp/
[ファイルが旅立つ音が鳴る]
$ /random-os-mystery-sound-effect
[謎のシステム効果音が鳴る]
```

# 注意点
- サウンドファイルはローカルの .claude/skills/random-os-mystery-sound-effect/sounds/ に保存されます。
- Linux/macOSでは `aplay` または `afplay`、Windowsでは `winsound` を利用します。
- 音量や再生デバイスはOSの設定に依存します。
- サウンド再生が不要な場合はSkillを無効化/削除してください。

# 参考資料
- 参考: [Python公式sound再生](https://docs.python.org/ja/3/library/winsound.html), [afplay](https://ss64.com/osx/afplay.html), [aplay](https://man7.org/linux/man-pages/man1/aplay.1.html)
- 詳細は references/design_notes.md を参照してください。