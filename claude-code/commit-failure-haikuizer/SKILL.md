---
name: commit-failure-haikuizer
description: コミットやプッシュ等のGit操作でエラーや失敗が発生した際、エラー内容を自動で五・七・五形式の俳句へ変換し、ターミナルに表示します。'commit failed'や'push error'などの失敗キーワード検知時に発動します。
---

# 機能概要
commit-failure-haikuizerは、Gitのコミットやプッシュなどの操作で失敗した際、エラー内容や状況を五・七・五の俳句に自動変換し、ターミナルに表示するスキルです。単なるエラー表示ではなく、ユーモラスかつ哀愁漂う一句によって、開発現場の空気を和ませます。繰り返し発生するエラーにも飽きず、気分転換やチームのコミュニケーション促進にも役立ちます。

# 使い方
- 明示呼び出し: `/commit-failure-haikuizer --error "push failed: remote rejected"`
- 暗黙発動: Git操作時に `commit failed`, `push error`, `merge conflict` などのエラー出力を検知した際に自動発動します。
- スクリプトは標準入力または引数でエラーメッセージを受け取り、俳句を生成します。

# 出力例
```
$ git push origin main
remote: error: failed to push some refs
To github.com:user/repo.git
! [rejected] main -> main (non-fast-forward)
error: failed to push some refs

俳句:
遠い空
届かぬ想い
pushできず
```

```
$ /commit-failure-haikuizer --error "commit failed: unresolved merge conflict"
俳句:
分かれ道
まだ解けぬまま
コンフリクト
```

# 注意点
- 俳句の生成はエラー文の日本語/英語を問わず対応しますが、完全な意味理解は保証されません。
- ローカルにエラーや生成俳句は保存されません。
- 重大なエラー内容を和らげるためのジョーク用途です。実運用時は本来のエラー内容も必ず確認してください。
- 除外パスや特定のGitフックとの併用時は競合に注意してください。

# 参考資料
- [Git公式ドキュメント](https://git-scm.com/docs)
- references/design_notes.md も参照してください。