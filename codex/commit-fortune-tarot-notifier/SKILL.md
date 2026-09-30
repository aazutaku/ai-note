---
name: commit-fortune-tarot-notifier
description: Gitのcommit時や/skills menu、commit-fortune-tarot-notifierの明示呼び出し時に発動。コミットごとに完全ランダムなタロット風ジョーク通知を表示し、開発現場にカオスな演出を加えます。
---

# 機能概要
このSkillは、Gitでコミットするたびに“タロットカード風の謎占い通知”をデスクトップまたはターミナルに表示します。通知内容は「運命の輪が回る」「愚者が新たな旅路に」など、完全ランダムなタロット風メッセージ。日々の開発作業に突如現れる謎の演出で、真面目な作業フローにユーモアとカオスをもたらします。コミット作業のたびに一喜一憂でき、チームの雰囲気を和ませるジョークSkillです。

# 使い方
- 明示呼び出し: `/skills menu` から選択、または `$commit-fortune-tarot-notifier` をターミナルで実行
- 暗黙発動: Gitのcommitコマンド実行時（例: `git commit -m "fix bug"`）

# 出力例
```
$ git commit -m "add new feature"
[タロット占い] 愚者が新たな旅路に出た。今日のコミットは冒険の始まり。
$ git commit -m "refactor code"
[タロット占い] 運命の輪が回る。変化の兆し、コードに吉兆あり。
$ git commit -m "fix typo"
[タロット占い] 塔が崩れる。油断大敵、慎重に進め。
$ commit-fortune-tarot-notifier
[タロット占い] 恋人たちが微笑む。協力が成功の鍵。
```

# 注意点
- 通知内容は完全にランダムで実用性はありません
- 作業を過度に阻害しないよう、通知は1行表示のみ
- 除外パスや特定ファイルには影響しません
- 通知履歴はローカル保存されません

# 参考資料
- references/design_notes.md
- https://docs.python.org/ja/3/library/subprocess.html
- https://git-scm.com/docs/githooks