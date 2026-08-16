---
name: random-os-mystery-sound-effect
description: コマンド実行やファイル操作などのアクションごとに、謎のOS公式サウンドエフェクトを毎回ランダムで再生します。trigger: コマンド実行/ファイル保存/明示呼び出し。
---

# 機能概要
このSkillは、ターミナルやエディタ上でコマンドを実行するたびに、謎の“OS公式サウンドエフェクト”をランダムで再生します。音源は「ファイルが旅立つ音」「シュールなやる気起動音」「謎のシステム自動拍手」など、用途や意味が不明なSEばかり。真面目な開発現場に突如シュールな音が響き渡ることで、集中崩壊や周囲の反応を楽しむカオスな演出が可能です。通知・演出・OS連携カテゴリに属し、開発体験にユーモアと混乱をもたらします。

# 使い方
- 明示呼び出し例: `/skills random-os-mystery-sound-effect` または `$random-os-mystery-sound-effect`
- 暗黙発動キーワード例: `run`, `build`, `save`, `compile`, `exec`, `ファイル保存`, `コマンド実行`

Skillを有効化すると、以降コマンドやファイル操作のたびに自動でSEが鳴ります。停止したい場合はSkillを無効化してください。

# 出力例
```
$ python main.py build
[SE] ファイルが旅立つ音を再生中...
Build succeeded!
$ ls
[SE] 謎のシステム自動拍手を再生中...
main.py  README.md
$ /skills random-os-mystery-sound-effect
[SE] シュールなやる気起動音を再生中...
```

# 注意点
- 音源ファイルはSkill内に同梱または公式フリー素材を自動DLし、一時ディレクトリにのみ保存されます
- サウンド再生には`playsound`または`afplay`/`aplay`等のOS標準コマンドを利用
- 音量や再生タイミングは環境依存。ミュート環境では無音
- Skill削除時に一時ファイルは自動削除され、環境に影響を残しません

# 参考資料
- [Python playsound公式](https://github.com/TaylorSMarks/playsound)
- references/design_notes.md 参照