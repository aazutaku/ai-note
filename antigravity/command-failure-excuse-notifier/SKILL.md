---
name: command-failure-excuse-notifier
description: コマンド実行やスクリプト動作時にエラーや失敗メッセージが発生した場合、このSkillは自動的にOSの通知領域へ“言い訳”メッセージを表示します。失敗・エラー・例外・command not found・exit code!=0 などのキーワードが検知された際に発動します。
---

# 機能概要
コマンド実行やスクリプト動作時、ただエラーメッセージを表示するだけでは味気ないもの。このSkillは、実行失敗時にOSの通知領域へ“全力の言い訳”を自動表示します。例えば「猫がキーボードを踏みました」「宇宙線の影響です」など、毎回異なるユーモラスなメッセージで、失敗体験を楽しく演出。自己肯定感を損なわず、開発作業のストレスを軽減します。

# 使い方
このSkillは明示的な呼び出しを必要とせず、Antigravityがコマンド失敗・例外・exit code!=0・command not found・エラー発生などを検知した際に自動発動します。スクリプトやCLIツールの実行時、失敗検知時に自動で通知が表示されます。

# 出力例
```
$ python build.py
Traceback (most recent call last):
  ...
ZeroDivisionError: division by zero
[通知] 言い訳: 猫がキーボードを踏みました

$ make deploy
make: *** [deploy] Error 2
[通知] 言い訳: 宇宙線がビットをひっくり返しました
```

# 注意点
- OS通知はWindows/macOS/Linuxの主要デスクトップ環境でサポートされますが、サーバやWSL等では通知が表示されない場合があります。
- 言い訳メッセージはランダム生成され、同じ失敗でも毎回異なります。
- 本来のエラーメッセージは失われず、通知とは別に標準出力/標準エラーに出力されます。
- ローカルに通知履歴は保存されません。

# 参考資料
詳細設計や言い訳メッセージ例、OSごとの通知API利用例は references/ 以下および https://docs.python.org/ja/3/library/subprocess.html, https://pypi.org/project/plyer/ などを参照してください。