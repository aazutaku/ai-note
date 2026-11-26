---
name: random-os-fake-mysterious-background-process-alert
description: このSkillは、ターミナルやデスクトップ作業中に「バックグラウンドプロセス」「謎の警告」「未確認進捗」などのキーワードが出現した際や、/random-os-fake-mysterious-background-process-alert の明示呼び出しで発動します。作業の合間に謎のOS風通知をランダムに表示し、ユーザーの正気を試します。
---

# 機能概要
このSkillは、作業中に突如「謎のOS公式・怪しいバックグラウンドプロセス通知」をランダムに表示します。実際には何も起きていないのに「未知の集計作業開始」「謎のプロセスID監視中」など、意味不明な警告や進捗バー、正体不明の残り時間を演出。IT都市伝説感を味わいたい、作業に刺激が欲しい方に最適です。通知内容は毎回異なり、完全ランダムなタイミングで発火します。

# 使い方
- 明示呼び出し: `/random-os-fake-mysterious-background-process-alert`
- 暗黙発動: 「バックグラウンドプロセス」「謎の警告」「未確認進捗」などのキーワードが会話やコード上に現れた際、自動で発動します。
- ターミナルで直接スクリプトを実行することも可能です。

# 出力例
```
[ALERT] 未知のバックグラウンドプロセスがPID 7777で起動しました。
[INFO] 集計タスク“XQ-Shadow”進捗: 37% 完了。残り時間: 12分47秒。
[WARNING] プロセスID 4921 の挙動を監視しています…
[NOTICE] 不明な解析ジョブ“GhostIndex”がバックグラウンドで動作中。
[ALERT] システムリソースの一部が一時的にロックされました。
```

# 注意点
- 本Skillは通知の演出のみで、実際のシステムやファイルには一切影響しません。
- ローカルにデータを保存したり、既存プロセスを操作することはありません。
- 意図しないタイミングで通知が発生する場合があります。

# 参考資料
- references/design_notes.md
- 公式Pythonドキュメント: https://docs.python.org/3/library/random.html, https://docs.python.org/3/library/argparse.html