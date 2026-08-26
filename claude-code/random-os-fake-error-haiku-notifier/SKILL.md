---
name: random-os-fake-error-haiku-notifier
description: Claude Codeは、エラー発生時や例外キャッチ時、または明示的に /random-os-fake-error-haiku-notifier が呼ばれた際にこのSkillを発動します。triggerType: always。キーワード: error, exception, fail, bug。
---

# 機能概要
このSkillは、開発者がターミナルやエディタでエラーや例外に遭遇した際、厳かな（しかし全く役に立たない）“OS公式風”のエラー俳句通知をデスクトップに表示します。エラー内容は無視し、毎回ランダムな俳句が選ばれるため、真面目なエラー通知に飽きた方や、作業中に一瞬の和みや混乱を求める方に最適です。俳句は日本語で生成され、通知は短時間で自動的に消えます。

# 使い方
- 明示呼び出し: `/random-os-fake-error-haiku-notifier` を入力すると即座に俳句通知が表示されます。
- 暗黙発動: `error`, `exception`, `fail`, `bug` などのキーワードを含む出力や例外発生時に自動で発動します。

# 出力例
```terminal
[OS Error Haiku]
バグの香や　春まだ遠き　デバッグ道

[OS Error Haiku]
夜のコード　静かに落ちる　未定義エラー

[OS Error Haiku]
桜散る　リファクタリングの　果てしなさ
```

# 注意点
- 通知内容はエラーの実態とは無関係です。
- 俳句は毎回ランダム生成・選択されます。
- 通知はローカル環境でのみ表示され、リモートやWeb IDEでは動作しない場合があります。
- ログやファイルへの保存は行いません。

# 参考資料
- [公式ドキュメント（Python notify2）](https://github.com/caronc/apprise)
- references/design_notes.md を参照してください。