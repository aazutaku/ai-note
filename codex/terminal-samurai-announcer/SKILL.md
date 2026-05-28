---
name: terminal-samurai-announcer
description: ターミナルでコマンド実行時や /skills menu で明示的に呼び出された際、侍風の時代劇ナレーションを毎回ランダムに挿入し、進捗や作業内容を勇ましく実況するSkill。コマンド実行・進捗・通知などのキーワードを含む操作時に発動。
---

# 機能概要
terminal-samurai-announcerは、ターミナルでコマンドを実行するたびに、侍が現れて時代劇風に作業内容や進捗を高らかに実況します。lsやgit、ビルドコマンドなど、普段の作業が一気にチャンバラ劇場に早変わり。毎回ランダムな侍ナレーションが表示され、作業の緊張感を和らげ、周囲の注目も集められる演出系Skillです。既存の作業フローを壊さず、ON/OFFも手軽に切り替え可能です。

# 使い方
- 明示呼び出し例: `/skills menu` から「terminal-samurai-announcer」をONにする、または `$terminal-samurai-announcer` をmention
- 暗黙発動キーワード例: 「コマンド実行」「進捗」「通知」「ls」「git」「build」などの操作時に自動発動

# 出力例
```
拙者、lsの構えにて候！
このcommit、見事なり！
お主、buildを成し遂げ申した！
拙者、rmの術を使い申す！
これぞpush、まさに一世一代の大勝負！
そなたのpull、鮮やかなる手並み！
```

# 注意点
- 本Skillは標準出力に侍風メッセージを挿入しますが、コマンドの実際の出力や挙動には影響しません。
- ローカルの履歴やファイルを変更しません。
- ON/OFFはSkillメニューや明示コマンドで切り替え可能です。
- 一部の特殊なコマンドやパイプ処理には対応しない場合があります。

# 参考資料
詳細な設計方針・利用例は `references/design_notes.md` を参照。時代劇ナレーションの生成はPythonの標準randomモジュールを活用。公式ドキュメント: https://docs.python.org/ja/3/library/random.html