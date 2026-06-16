---
name: command-failure-excuse-notifier
description: コマンド実行時に失敗（例: exit code非ゼロや例外発生）が検出された場合に発動し、OSの通知領域へ“言い訳”を添えたエラーメッセージを表示します。失敗時の通知・演出・OS連携が必要な場面で自動/明示的に利用されます。
---

# 機能概要
このSkillは、コマンドやスクリプト実行時にエラー（例: 非ゼロ終了コードや例外）が発生した際、通常のエラーメッセージだけでなく、ユーモラスな“全力言い訳”をOSの通知領域（Windows, macOS, Linux）へ自動表示します。これにより、開発や運用時の失敗体験をポジティブに転換し、チームや個人の気分転換・自己肯定感向上に貢献します。

# 使い方
- 明示呼び出し例: `/skills command-failure-excuse-notifier run -- python myscript.py`
- 暗黙発動例: コマンド実行時に `error`, `failed`, `exception`, `traceback` などのキーワードや非ゼロ終了コードが検出された場合、自動的にSkillが発動します。

# 出力例
```
$ python broken.py
Traceback (most recent call last):
  File "broken.py", line 1, in <module>
    1/0
ZeroDivisionError: division by zero
---
[通知領域]: コマンド失敗: 猫がキーボードを踏みました（ZeroDivisionError: division by zero）
```

# 注意点
- OS通知は `plyer` ライブラリ等を利用。Linuxでは通知デーモンが必要です。
- 言い訳メッセージは毎回ランダム生成されます。
- エラーメッセージ自体は失われず、標準エラー出力にも出力されます。
- ローカル通知のみ対応。リモートやWeb通知は非対応です。

# 参考資料
- [Plyer公式ドキュメント](https://plyer.readthedocs.io/en/latest/)
- references/design_notes.md 参照