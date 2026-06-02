---
name: commit-failure-haikuizer
description: コミットやpushなどのGit操作失敗時、エラー内容を五・七・五の俳句に変換し自動表示します。エラー、push失敗、commitエラー、merge衝突などのキーワード検知時に発動します。
---

# 機能概要
このSkillは、Gitのcommitやpush、mergeなどの操作でエラーが発生した際、通常のエラー表示だけでなく、その内容や状況を五・七・五の俳句に自動変換してターミナルに表示します。エンジニアの日常にユーモアと哀愁を添え、失敗の瞬間も和ませます。エラー内容を俳句化することで、毎回異なる一句が生成され、飽きずに楽しめます。

# 使い方
- 明示呼び出し: `/skills commit-failure-haikuizer "<エラーメッセージ>"` で任意のエラー文を俳句化
- 暗黙発動: `commit`, `push`, `merge`, `error`, `failed`, `conflict` などのエラーキーワード検知時に自動発動
- コミットフックやCI/CDスクリプトに組み込むことで、失敗時に自動俳句表示が可能

# 出力例
```
$ git push origin main
error: failed to push some refs to 'github.com:user/repo.git'

俳句:
遠き空
pushできぬ指
ため息よ

$ /skills commit-failure-haikuizer "merge conflict in file main.py"

俳句:
衝突して
main.pyの中
迷い道
```

# 注意点
- 俳句生成はエラー内容をもとにするため、必ずしも完璧な五・七・五になるとは限りません
- ローカルでのみ動作し、生成俳句の保存は行いません
- 日本語以外のエラーメッセージも俳句化しますが、意味が崩れる場合があります

# 参考資料
- [Git公式ドキュメント](https://git-scm.com/doc)
- references/design_notes.md に設計方針や利用例を記載