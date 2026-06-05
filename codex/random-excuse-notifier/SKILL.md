---
name: random-excuse-notifier
description: Codexがターミナル操作やコマンド実行、/skills menuやrandom-excuse-notifierの明示呼び出し時に発動。通知・OS連携・演出系Skillとして、操作ごとにユーモラスな“言い訳”をOS通知領域へ表示します。
---

# 機能概要
random-excuse-notifierは、ターミナル操作やコマンド実行のたびに、全く根拠のない“言い訳”をOSの通知領域にランダム表示するSkillです。ネットワーク遅延や水星逆行、マウス不調など、思わず笑ってしまう言い訳が次々と現れ、作業の合間にユーモアを提供します。業務効率化や生産性向上には一切寄与しませんが、日々の作業にちょっとした遊び心を加えたい方に最適です。

# 使い方
- 明示呼び出し例:
  - `/skills menu` から random-excuse-notifier を選択
  - `$random-excuse-notifier` をターミナルで直接実行
- 暗黙発動キーワード例:
  - ターミナルでコマンド実行時
  - 「通知」「演出」「言い訳」などのキーワードを含む操作

# 出力例
```
$ ls
（通知）今日はネットが遅いみたいです。
$ git push
（通知）マウスが反応しませんでした。
$ random-excuse-notifier
（通知）水星逆行中なので仕方ありません。
$ echo hello
（通知）上司のせいです。
$ python script.py
（通知）たぶん宇宙線の影響です。
```

# 注意点
- OSの通知API（Windows: Toast, macOS: terminal-notifier, Linux: notify-send）を利用
- 通知はローカル端末でのみ表示され、履歴保存は行いません
- ネタが被りにくいよう十分なランダム性を確保していますが、完全な非重複は保証しません
- 通知機能が無効な環境では動作しません

# 参考資料
- [notify2 (Linux)](https://pypi.org/project/notify2/)
- [plyer (クロスプラットフォーム通知)](https://plyer.readthedocs.io/en/latest/)
- references/design_notes.md も参照