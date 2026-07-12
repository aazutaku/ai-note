---
name: random-os-motivational-quote-notifier
description: 作業中やコマンド実行時、または『モチベーション』『やる気』『進捗』『バグ』などのキーワード検出時に、OSのデスクトップ通知でランダムな“謎のOS偽モチベーション格言”を表示します。気分転換やチームの雰囲気変化に最適です。
---

# 機能概要
このSkillは、作業中や特定のキーワード（例: モチベーション、やる気、進捗、バグ）を検出した際、あるいは明示的な呼び出しによって、あなたのデスクトップに“謎のOS偽モチベーション格言”をランダムに通知します。格言は毎回異なり、「本日もバグに感謝せよ」「進捗ゼロ、それもまた進化」「コードは寝かせて美味しくなる」など、やけに的外れで深そうなものばかり。仕事が進まないときや、やる気が出ないとき、逆に動揺したいときに最適なエンタメ通知を提供します。

# 使い方
- 明示呼び出し: `/random-os-motivational-quote-notifier` または `/skill random-os-motivational-quote-notifier notify`
- 暗黙発動: 「やる気」「進捗」「バグ」「モチベーション」などの単語を含む会話やコマンド実行時に自動で発動
- CLIからは `python notifier.py notify` で即時通知

# 出力例
```
$ python notifier.py notify
[通知] OS格言: コードは寝かせて美味しくなる

$ python notifier.py list
1. 本日もバグに感謝せよ
2. 進捗ゼロ、それもまた進化
3. コードは寝かせて美味しくなる
...
```

# 注意点
- 通知はローカルOSの通知機能を利用します（Windows/macOS/Linux対応）
- 通知内容や履歴はローカルにのみ保存され、外部送信はありません
- 長時間の連続通知や大量発動にはご注意ください
- Python 3.8以降、`plyer`または`notify2`などの通知ライブラリが必要です

# 参考資料
- references/design_notes.md
- https://plyer.readthedocs.io/en/latest/
- https://docs.python.org/3/library/random.html