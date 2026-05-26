---
name: commit-dajare-generator
description: Antigravity は、コミットメッセージ自動生成時や git commit 操作の直前にこのSkillを発動します。変更内容やファイル名を解析し、ダジャレを交えたユーモアあるメッセージを提案したい場合に最適です。
---

# 機能概要
commit-dajare-generator は、コミット時に変更内容やファイル名を解析し、理系ギャグ漫画家ばりのダジャレを効かせたコミットメッセージを自動生成します。真面目な開発現場に笑いとユーモアをもたらし、コミュニケーションのきっかけやチームの雰囲気改善に貢献します。ファイル名やdiffからキーワードを抽出し、それに基づくダジャレを自動で提案。毎回のコミットがちょっとしたネタになるため、エンジニアの“寒さ耐性”と“笑いの沸点”を同時に試すことができます。

# 使い方
このSkillは、Antigravityのコミットメッセージ自動生成機能と連携し、`git commit`や「コミット」「変更」「push」などの操作時に暗黙的に発動します。明示的な呼び出しは不要です。Skillが有効な場合、コミット直前にダジャレ混じりのメッセージ案が自動で表示されます。

- 暗黙発動キーワード例: `git commit`, `push`, `変更`, `add`, `update`, `fix` など

# 出力例
```
$ git add main.py
$ git commit
[commit-dajare-generator] 提案:
main.py をメインに修正。メインイベント発生！
function.py をファンクションアップ。関数だけに感謝！
bug_fix.js のバグを虫のように退治。バグっとな！
README.md をリードしてみた。読んでみてね！
utils.py を有効活用。ユーティリティーって、言うてるって！
```

# 注意点
- ダジャレ生成は日本語が中心です。英語ファイル名やdiff内容には一部対応が限定されます。
- 生成メッセージはローカルでのみ保存・表示されます。自動コミットは行いません。
- 除外パスや特定ディレクトリ（例: .git, node_modules）は自動的に無視されます。
- チームの雰囲気や文化によっては利用を控えることを推奨します。

# 参考資料
- references/design_notes.md を参照してください。
- 公式: https://git-scm.com/doc
- 日本語ダジャレ生成: https://github.com/taizan-hokuto/pykakasi, https://pypi.org/project/word2vec-gensim/