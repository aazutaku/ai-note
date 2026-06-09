---
name: random-os-error-translator
description: ターミナルやコマンドラインでエラーが発生した際に、エラーメッセージを“別のOS風”に自動変換して表示します。エラー発生や例外検出、stderr出力などが含まれる場合に発動します。
---

# 機能概要
このSkillは、コマンドラインやターミナルでエラーが発生した際、そのエラーメッセージを自動的に“別のOS風”に変換して表示します。例えば「Permission denied」が「このファイルは神聖にして侵入を禁ず（MS-DOS風）」や「推奨されていない操作です（国産OS風）」など、実際の意味とは異なる演出で、日々の作業にユーモアとカオスをもたらします。真面目な作業中でも、思わず笑ってしまう不可解なエラー体験を提供します。

# 使い方
このSkillは明示的な呼び出しを必要とせず、エラーや例外が発生したタイミングで自動的に発動します。例えば、`FileNotFoundError`や`PermissionError`などの例外、またはコマンド実行時のstderr出力が検出された場合に作動します。暗黙発動キーワード例: "エラー", "失敗", "例外", "コマンド失敗", "stderr"。

# 出力例
```
$ python script.py
[MS-DOS風] このファイルは神聖にして侵入を禁ず。
(元のエラー: Permission denied: 'secret.txt')

$ ls /notfound
[謎の国産OS風] 推奨されていない操作です。
(元のエラー: No such file or directory)

$ cat /root/flag
[Linux風] ルート様のご許可が必要です。
(元のエラー: Permission denied)
```

# 注意点
本Skillはエラー内容をパロディ変換するため、実際の原因追跡には元のメッセージも併記されます。ローカルへのエラーログ保存や、重要なシステムエラーの抑制は行いません。演出は毎回ランダムで、意味不明な場合もあります。業務用途や正確な障害対応には不向きです。

# 参考資料
詳細な設計方針や演出パターンは`references/design_notes.md`を参照してください。Pythonの標準例外やstderrの扱いについては[公式ドキュメント](https://docs.python.org/ja/3/library/exceptions.html)も参考になります。