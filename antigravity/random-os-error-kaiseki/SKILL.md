---
name: random-os-error-kaiseki
description: Antigravityは、コマンド実行時にOSエラーや例外が発生した場合、このSkillを自動発動し、エラーメッセージを“カタカナ専門用語”でランダムにデスクトップ通知します。triggerType: always、semantic-match-onlyで動作。
---

# 機能概要
このSkillは、コマンドやスクリプト実行時に発生したエラーや例外を検知し、通常のエラーメッセージの代わりに“OS風・謎のカタカナ専門用語”による意味不明なエラー解説をデスクトップ通知として表示します。たとえば「パケット・シンフォニーがバッファ・カタストロフを検出しました」や「デジタル・アンビエントがオーバーフローしました」など、技術者っぽい雰囲気を醸し出しつつも、内容は全く意味が通じません。エラー発生時のストレスをカタカナギャグで強制リフレッシュし、開発現場に笑いと混乱をもたらします。

# 使い方
このSkillはAntigravity内で自動的に発動します。明示的な呼び出しは不要です。エラーや例外（例: FileNotFoundError, OSError, subprocess.CalledProcessErrorなど）が発生した際に、通常のエラーメッセージに加えて、毎回異なるカタカナ専門用語の解説がデスクトップ通知として表示されます。

## 暗黙発動キーワード例
- OSError
- Exception
- subprocess error
- ファイルアクセス失敗
- コマンド実行失敗

# 出力例
```
$ python example.py
Traceback (most recent call last):
  File "example.py", line 2, in <module>
    open('notfound.txt')
FileNotFoundError: [Errno 2] No such file or directory: 'notfound.txt'

[通知] パケット・シンフォニーがバッファ・カタストロフを検出しました

$ ./run_command.sh
[通知] デジタル・アンビエントがオーバーフローしました
```

# 注意点
- 本Skillはエラーの本質的な原因分析や解決には役立ちません。
- 通知内容は毎回ランダム生成されるため、再現性がありません。
- 本来のエラーメッセージは通知とは別に標準出力/標準エラーに出力されます。
- ローカル環境のデスクトップ通知機能（notify-send, plyer等）が必要です。

# 参考資料
- references/design_notes.md を参照
- [Python公式例外ドキュメント](https://docs.python.org/ja/3/library/exceptions.html)
- [plyer通知API](https://plyer.readthedocs.io/en/latest/)
