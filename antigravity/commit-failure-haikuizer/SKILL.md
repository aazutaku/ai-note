---
name: commit-failure-haikuizer
description: git commitやpushなどのバージョン管理操作でエラーや失敗が発生した際に、エラーメッセージをもとに五・七・五の俳句へ自動変換し、ターミナルに表示するSkillです。エラー発生時に自動で発動します。
---

# 機能概要
commit-failure-haikuizerは、gitのcommitやpush等でエラーが発生した際、単なるエラーメッセージの表示だけでなく、その内容や状況をもとに五・七・五形式の俳句を自動生成し、ターミナルへ出力します。これにより、繰り返される失敗やトラブルの瞬間にも、ユーモアや哀愁が漂う一句で場の空気を和ませ、開発者の気持ちを少し軽くします。毎回異なる俳句が生成されるため、飽きずに楽しめます。

# 使い方
このSkillは、git commit/push/pullなどの失敗時に自動で発動します（明示的な呼び出しは不要）。エラー発生時、エラーメッセージや状況をもとに俳句が生成され、標準出力に表示されます。

**暗黙発動キーワード例:**
- commit failed
- push rejected
- merge conflict
- authentication error

# 出力例
```
$ git push origin main
error: failed to push some refs to 'origin/main'

俳句:
遠いリモート
拒まれしpush
明日こそは

$ git commit -m 'fix bug'
error: pathspec 'fix bug' did not match any file(s) known to git

俳句:
ファイルなし
静かなリポジトリ
手が止まる
```

# 注意点
- 俳句の品質はエラーメッセージ内容や自動生成ロジックに依存します。
- 日本語エラー以外もサポートしますが、意味不明な句になる場合があります。
- 生成された俳句はローカルに保存されません。
- 一部の特殊なエラーは正しく俳句化できない場合があります。

# 参考資料
- [Git公式ドキュメント](https://git-scm.com/doc)
- references/design_notes.md を参照してください。