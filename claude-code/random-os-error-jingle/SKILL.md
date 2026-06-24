---
name: random-os-error-jingle
description: コマンド実行時やスクリプト内で例外・OSエラーが発生した際に、ランダムな“OSエラージングル”を再生するSkill。エラー発生・Exception・失敗・通知・サウンド演出などが発動条件。
---

# 機能概要
`random-os-error-jingle`は、コマンド実行やPythonスクリプト内でエラー（例外やOSエラー）が発生した瞬間、ローカルに用意した複数の“OSエラージングル”音源（WAV/MP3/ファミコン風など）からランダムで1つを強制再生します。作業中にエラーが起きたことを音で即座に知らせるだけでなく、周囲にも「また変な音が鳴ってる」と印象づけるジョーク系Skillです。音源の追加・差し替えも容易で、サウンド演出にこだわりたいユーザー向けです。

# 使い方
- 明示呼び出し: `/random-os-error-jingle --mute` でミュート、`--volume 0.3`で音量調整。
- 暗黙発動: `try/except`やコマンド失敗時に自動で発動。`Exception`, `OSError`, `失敗`, `エラー`, `通知`などのキーワードや例外発生時にトリガー。
- 音源は `.claude/skills/random-os-error-jingle/sounds/` にWAV/MP3形式で追加・差し替え可。

# 出力例
```
$ python my_script.py
Traceback (most recent call last):
  File "my_script.py", line 10, in <module>
    raise OSError("Disk not found!")
OSError: Disk not found!
[ジングル再生: famicom_error2.wav]
```

# 注意点
- 音源ファイルはローカル保存が必要です。
- サウンド再生には`playsound`/`pygame`/`pydub`などの実在APIを利用。
- ミュート/音量調整はコマンドライン引数で切替。
- サーバーや音声出力不可環境では動作しません。
- 除外パスや特定例外は`--exclude`で指定可能。

# 参考資料
- 詳細設計・参考: [references/design_notes.md]
- 公式: [https://pypi.org/project/playsound/], [https://www.pygame.org/docs/]
