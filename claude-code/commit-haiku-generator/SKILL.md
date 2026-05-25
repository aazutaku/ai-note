---
name: commit-haiku-generator
description: コミットメッセージを自動で五・七・五の俳句形式に変換したい場合に発動します。キーワード: commit, message, haiku, 俳句, 自動生成, joke, parody, semantic trigger。
---

# 機能概要
commit-haiku-generatorは、Git等のコミットメッセージを日本語の五・七・五俳句形式に自動変換するSkillです。開発現場での単調なコミット作業に文学的な遊び心を加え、エンジニアの心に癒しと笑いをもたらします。真面目な修正内容も和のリズムで表現され、時に意味不明な一句が生まれることで、日々の開発にユーモアとカオスを提供します。

# 使い方
明示的な呼び出しは `/commit-haiku-generator "修正内容の説明"` のように行います。暗黙的には「commit」「message」「haiku」「俳句」「自動生成」などのキーワードを含むコミットメッセージ編集時や、コミット直前のフックで発動します。CLIサブコマンドとして `generate`（俳句生成）、`list`（過去の俳句一覧）、`summary`（俳句による要約）を利用可能です。

# 出力例
```
$ /commit-haiku-generator "READMEを更新しバグ修正"
READMEを
更新しつつも
バグ直した

$ python haiku_commit.py generate "API仕様変更"
API変え
仕様の波に
乗る我ら
```

# 注意点
- 完全な意味保持は保証されません。俳句生成の過程で内容が崩れる場合があります。
- 除外パスや特定ファイルには適用されません（設定で指定可能）。
- 生成された俳句はローカルの履歴ファイルに保存されます。
- 俳句生成には形態素解析エンジン（MeCab）を利用しています。

# 参考資料
詳細な設計方針や利用例は references/design_notes.md を参照してください。公式ドキュメントや形態素解析の詳細は https://taku910.github.io/mecab/ を参照。