---
name: commit-dajare-generator
description: コミット時や /skills menu, commit, message, joke, ダジャレ などのキーワードが含まれる場合に発動し、変更内容やファイル名に基づいた理系ダジャレのコミットメッセージを自動生成します。
---

# 機能概要
commit-dajare-generatorは、コミット時に変更内容やファイル名を解析し、理系ギャグ漫画家も顔負けのダジャレコミットメッセージを自動で提案するSkillです。真面目な開発現場にユーモアを持ち込み、チームの雰囲気を和らげます。コミットメッセージのマンネリ化を防ぎ、エンジニア同士のアイスブレイクにも最適です。

# 使い方
- 明示呼び出し例: `/skills menu` で一覧から選択、または `@commit-dajare-generator` で直接呼び出し。
- 暗黙発動キーワード例: commit, message, joke, ダジャレ, push, add, fix, update などのコミット関連語を含む操作時に自動発動。

# 出力例
```
$ git add src/algorithm.py
$ git commit -m ""
[commit-dajare-generator] src/algorithm.py を修正したので、アルゴリズムにアルゴリズム（あるごり無）！

$ git add bugfix.js
$ git commit -m ""
[commit-dajare-generator] bugfix.js のバグを直したので、バグがバグっと消えた！

$ git add README.md
$ git commit -m ""
[commit-dajare-generator] README.md を更新、読んでみー（README）！
```

# 注意点
- 生成されるダジャレは日本語ベースで、英語ファイル名にも無理やり対応します。
- すべてのファイル名や変更内容で必ずしも秀逸なダジャレが生成されるとは限りません。
- コミットメッセージの自動上書きに注意し、必要に応じて手動修正してください。
- ローカルでのみ動作し、外部APIへの送信はありません。

# 参考資料
- references/design_notes.md に設計方針・利用例を記載
- 公式Gitコミットメッセージガイド: https://www.git-scm.com/book/ja/v2/Git-%E3%81%AE%E5%9F%BA%E6%9C%AC-%E3%82%B3%E3%83%9F%E3%83%83%E3%83%88%E3%83%A1%E3%83%83%E3%82%BB%E3%83%BC%E3%82%B8