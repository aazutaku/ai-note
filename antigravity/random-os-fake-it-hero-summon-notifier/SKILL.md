---
name: random-os-fake-it-hero-summon-notifier
description: このSkillは、作業やコーディングの合間に「英雄召喚」風の通知をランダムなタイミングで表示します。triggerType: always で、通知・演出・OS連携系のキーワード（例: 孤独, モチベーション, エンタメ, 通知, OS, 勇者, 英雄, バグ, デバッグ, 召喚）を含む状況で発動します。
---

# 機能概要
random-os-fake-it-hero-summon-notifierは、作業中に突如として“OS公式”や“IT英雄”が召喚されたかのような通知をデスクトップやターミナルへ表示するエンタメ系Skillです。通知内容は毎回ランダムで、架空のデバッグ勇者や伝説のコマンド使いが現れ、あなたの作業を（精神的に）支援します。孤独な開発や長時間の作業に謎の勇気と笑いを提供し、気分転換やモチベーション維持に役立ちます。

# 使い方
このSkillは自動発動型です。特定の明示呼び出しは不要で、triggerType: always のため、エージェントが「通知」「英雄」「バグ」「孤独」などのキーワードや状況を検知した際に自動的に発動します。ターミナルまたはデスクトップ通知として演出されます。

# 出力例
```
[OS通知] 伝説のデバッグ勇者「タカシ」が参上しました！
[OS通知] バグ討伐の時！“コマンド使いのジョン”が出動します。
[OS通知] 謎のOS公式「バーチャル管理者」があなたの作業を見守っています。
[OS通知] 伝説のリファクタリング忍者「サクラ」が召喚されました。
[OS通知] 今こそバグ退治の時！“スクリプト魔術師”が現れた！
```

# 注意点
- 通知は完全にエンタメ目的であり、作業データや環境には一切影響を与えません。
- ローカルに通知履歴や個人情報は保存されません。
- 通知内容は毎回ランダム生成され、繰り返し出現もあります。
- OSの通知機能（Linux: notify-send, macOS: osascript, Windows: Toast通知）を利用します。

# 参考資料
- references/design_notes.md
- https://docs.python.org/ja/3/library/random.html
- https://github.com/jithurjacob/Windows-10-Toast-Notifications
- https://wiki.archlinux.jp/index.php/Notify-send