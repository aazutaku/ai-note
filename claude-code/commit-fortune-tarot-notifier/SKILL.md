---
name: commit-fortune-tarot-notifier
description: このSkillは、Gitでcommitするたびに“タロット風の謎占い通知”を表示します。commitやpushなどの操作時に、完全ランダムなタロット風メッセージで開発現場にユーモアを提供します。
---

# 機能概要
commit-fortune-tarot-notifierは、Gitリポジトリでcommit操作が行われるたびに、タロットカード風の謎めいた占いメッセージをターミナルやデスクトップ通知で表示するSkillです。真面目な開発フローの中に突如現れる“運命の輪”や“愚者”などのメッセージが、作業現場の空気を一変させ、ちょっとした息抜きや話題作りに役立ちます。通知内容は完全ランダムで、吉凶や意味も毎回異なります。

# 使い方
- 明示呼び出し: `/commit-fortune-tarot-notifier`
- 暗黙発動: 「commit」「push」「git」「占い」「タロット」「通知」などのキーワードを含む操作時に自動発動します。
- Gitのcommit時に自動でターミナル/デスクトップ通知が表示されます。

# 出力例
```
[Tarot Fortune] 運命の輪が回り始めた。今日のコミットは大吉！
[Tarot Fortune] 愚者が新たな旅路に出る。大胆な変更が吉と出るか凶と出るか…
[Tarot Fortune] 塔が崩れる。バグの予感。慎重に進め！
[Tarot Fortune] 女教皇が静かに見守る。冷静なレビューを。
[Tarot Fortune] 太陽が輝く。最高の一日になるだろう。
```

# 注意点
- Gitのpre-commitやpost-commitフックを利用するため、ローカルリポジトリでのみ動作します。
- 通知内容は完全にランダムで、実際の運勢やコード品質とは無関係です。
- スクリプトはPython依存です。Linux/macOSでは`notify-send`や`osascript`を利用、Windowsは標準通知APIを使用します。
- 除外パスや特定ファイルには通知を抑制可能です。

# 参考資料
- references/design_notes.md
- https://git-scm.com/docs/githooks
- https://docs.python.org/3/library/random.html
- https://pypi.org/project/plyer/