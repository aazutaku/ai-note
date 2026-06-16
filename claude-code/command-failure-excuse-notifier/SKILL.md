---
name: command-failure-excuse-notifier
description: コマンド実行時にエラーや失敗が検出された場合、“言い訳”付きでOS通知を発火します。失敗検知・エラー出力・通知連携が必要な場面で自動発動します。
---

# 機能概要
このSkillは、コマンド実行時にエラーが発生した場合、通常のエラーメッセージだけでなく、毎回異なる“謎の言い訳”メッセージをOSの通知領域に自動表示します。例えば「猫がキーボードを踏みました」「宇宙線がビットをひっくり返しました」など、ユーモア溢れる言い訳がランダムに生成され、開発現場の空気を和らげます。失敗のストレスを軽減し、自己肯定感を高めることを目的としています。

# 使い方
- 明示呼び出し例: `/command-failure-excuse-notifier --run "ls /notfound"`
- 暗黙発動キーワード例: 「コマンド失敗」「エラー通知」「言い訳」「notify on error」などが含まれる場合、自動的にSkillが発動します。

# 出力例
```
$ python command_failure_excuse_notifier.py --run "cat missing.txt"
[ERROR] Command failed: cat missing.txt
[STDERR] cat: missing.txt: No such file or directory
[EXCUSE] 言い訳: 宇宙線がビットをひっくり返しました
(通知がOSに表示されます)
```

# 注意点
- OS通知はmacOS/Linux/Windowsの主要デスクトップ環境でサポートされますが、サーバやCUI専用環境では通知が表示されません。
- 言い訳メッセージは毎回ランダム生成されます。
- 本来のエラーメッセージは失われず、ターミナルにも出力されます。
- ローカルに通知履歴は保存されません。

# 参考資料
- [Python公式 subprocess.run](https://docs.python.org/ja/3/library/subprocess.html)
- [plyer通知API](https://github.com/kivy/plyer)
- references/design_notes.md に詳細な設計方針を記載