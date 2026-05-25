---
name: terminal-mood-indicator
description: ターミナルの環境変数（例: MOOD）が設定されている場合や、コマンドラインで明示的に呼び出された場合に発動します。"気分" "mood" "プロンプト" "環境変数" などのキーワードや、/terminal-mood-indicator コマンドがトリガーです。
---

# 機能概要
terminal-mood-indicator Skillは、ターミナルの環境変数（MOOD）に応じてプロンプトや画面上にその日の気分マーク（例: 元気・だるい・やる気MAXなど）を自動表示します。作業開始時に気分をセットするだけで、以降のコマンド実行時に毎回その気分が演出され、チームメンバーにも可視化されます。これにより、開発現場の雰囲気を和らげたり、コミュニケーションのきっかけを作ることができます。

# 使い方
- 明示呼び出し例:
  `/terminal-mood-indicator set "迷走中"`
  `/terminal-mood-indicator show`
- 暗黙発動キーワード例:
  "気分", "mood", "プロンプト", "今日の気分"
- 気分を変更するには、`export MOOD="やる気MAX"` などと環境変数を設定します。

# 出力例
```
$ export MOOD="燃え尽き寸前"
$ /terminal-mood-indicator show
今日の気分：燃え尽き寸前
──────────────
(╯°□°）╯︵ ┻━┻
──────────────
$ echo hello
今日の気分：燃え尽き寸前
hello
$ /terminal-mood-indicator set "元気"
今日の気分：元気
( •̀ᴗ•́ )و ̑̑
```

# 注意点
- MOOD環境変数が未設定の場合はデフォルト表示になります。
- 本Skillはローカル環境のみに影響し、他ユーザーのセッションには影響しません。
- プロンプト自動書き換えには、bash/zshの設定ファイル編集が必要な場合があります。
- 長文や特殊文字は一部サポート外です。

# 参考資料
- [Bash環境変数公式ドキュメント](https://www.gnu.org/software/bash/manual/html_node/Environment.html)
- references/design_notes.md 参照