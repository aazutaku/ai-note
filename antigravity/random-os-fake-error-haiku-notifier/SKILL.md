---
name: random-os-fake-error-haiku-notifier
description: エラー発生・例外検知・ビルド失敗・テストエラー・クラッシュ・stderr出力などのキーワードやイベントを検出した際に発動し、俳句形式の通知を表示します。
---

# 機能概要
このSkillは、ターミナルやエディタ上でエラーや例外が発生した際に、実際のエラー内容とは無関係な“謎のOS公式・エラー俳句”をデスクトップ通知として表示します。俳句は毎回ランダムで選ばれ、開発者の心に一瞬の静けさや混乱を提供します。真面目なエラー通知に飽きた方や、作業中の気分転換を求める方に最適な和風カオス演出です。

# 使い方
このSkillは明示的な呼び出しは不要です。エラー発生時（例: "error", "exception", "failed", "crash", "stderr" などのキーワードやイベント）を検知すると自動で発動します。設定やコマンドは不要で、OSの通知機能（Windows, macOS, Linux）を利用して俳句が表示されます。

# 出力例
```
[通知] OSからの神託:
バグの香や　春まだ遠き　デバッグ道

[通知] OSからの神託:
落ちるたび　静かに咲ける　桜かな

[通知] OSからの神託:
エラー音　夜更けの窓に　風ひとつ
```

# 注意点
- 通知はOSの標準API（notify-send, AppleScript, Windows Toast等）を利用します。
- 俳句は完全ランダムで、実際のエラー内容や原因とは無関係です。
- 通知は数秒で自動的に消え、作業を妨げません。
- ログやエラー内容の保存・送信は行いません。
- 通知機能が無効な環境では動作しません。

# 参考資料
- references/design_notes.md 参照
- https://docs.python.org/3/library/subprocess.html
- https://github.com/jithurjacob/Windows-10-Toast-Notifications
- https://wiki.archlinux.jp/index.php/Notify-send