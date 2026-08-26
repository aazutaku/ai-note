---
name: random-os-fake-error-haiku-notifier
description: ターミナルやエディタ上でエラーや例外発生時、または /skills menu など明示コマンド時に、完全ランダムな和風エラー俳句をデスクトップ通知で表示します。通知・演出・OS連携用途に適します。
---

# 機能概要
このSkillは、開発中のエラー発生時や明示呼び出し時に、実際のエラー内容とは無関係な“謎のOS公式・エラー俳句”をデスクトップ通知として表示します。俳句は毎回ランダム生成され、作業中の緊張感を和らげたり、意表を突く和風演出で開発者の心に一瞬の静けさと混乱をもたらします。真面目なエラー通知に飽きた方や、チームの雰囲気を和らげたい場面に最適です。

# 使い方
- 明示呼び出し: `/skills menu` から本Skillを選択、または `$random-os-fake-error-haiku-notifier` を直接実行
- 暗黙発動: ターミナルやエディタで `Traceback`、`Exception`、`error:` などのキーワードを含むエラー出力が発生した際、自動的に俳句通知が表示されます。

# 出力例
```terminal
$ python myscript.py
Traceback (most recent call last):
  File "myscript.py", line 3, in <module>
    raise ValueError("fail")
ValueError: fail

[OS通知]
デバッグ道
夜更けに響く
バグの声
```

# 注意点
- 本Skillはエラー内容を解析せず、俳句のみをランダム表示します。
- 通知は一時的(約5秒)で自動消去され、ログ等には保存されません。
- OSの通知機能(python標準または`plyer`等)を利用しますが、環境によって通知表示に制限がある場合があります。
- ローカル保存や履歴取得機能はありません。

# 参考資料
- [Python plyer通知ドキュメント](https://plyer.readthedocs.io/en/latest/)
- references/design_notes.md 参照