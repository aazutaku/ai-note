---
name: random-os-error-jingle
description: Antigravityがユーザーのコマンド実行時にエラーや例外を検知した際、自動的にランダムな“OSエラージングル”を再生する。エラー通知や警告、失敗、例外、command failed等のキーワードに反応して発動。
---

# 機能概要
このSkillは、コマンド実行時にエラーや例外（例: コマンド失敗、例外発生、exit code!=0等）を検知すると、事前に用意した複数の“OSエラージングル”音源（WAV/MP3/ファミコン風等）からランダムに1つを再生します。これにより、エラー発生時に即座に音で気づけるだけでなく、作業場にジョーク的な演出を加えます。音源ファイルは任意に追加・差し替え可能です。

# 使い方
Skillは暗黙的に発動します。`エラー`、`例外`、`command failed`、`exit code`、`Traceback`等の出力や、Antigravityがコマンド失敗を検知した瞬間、ジングルが再生されます。音源フォルダにWAV/MP3ファイルを追加するだけで、次回からランダム選択対象となります。

# 出力例
```terminal
$ python my_script.py
Traceback (most recent call last):
  File "my_script.py", line 1, in <module>
    raise Exception("Something went wrong!")
Exception: Something went wrong!
[ジングル音が再生される]
$ ls /not/exist
ls: cannot access '/not/exist': No such file or directory
[別のジングル音が再生される]
```

# 注意点
- 音源ファイルは `.agent/skills/random-os-error-jingle/jingles/` 以下に保存してください。
- 音量調整やミュートはコマンドライン引数で切り替え可能です。
- サウンド再生はローカル環境でのみ動作します（リモート/サーバーでは音が鳴らない場合あり）。
- 音源ファイルが1つも無い場合は再生されません。

# 参考資料
- [Python playsound公式](https://github.com/TaylorSMarks/playsound)
- references/design_notes.md に設計方針・応用例を記載