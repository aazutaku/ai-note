---
name: random-os-fake-it-hero-summon-notifier
description: このSkillは、作業中やコマンド実行時などに「英雄召喚」風のランダム通知を発動します。通知・演出・孤独感緩和・OS連携を求める場面や、/skills メニューや skill名を明示的に呼び出した時に発動します。
---

# 機能概要
random-os-fake-it-hero-summon-notifierは、作業中の端末やデスクトップに、まるでOSが勝手にIT界の英雄を召喚したかのような通知をランダムなタイミングで表示するエンタメ系Skillです。通知内容は毎回異なり、「伝説のデバッグ勇者が参上」「バグ退治の時！コマンド使いのジョン出動」など、IT作業者の孤独を和らげ、ちょっとした勇気や笑いを提供します。実用性はありませんが、長時間の作業や集中が続く場面で精神的なサポートを演出します。

# 使い方
- 明示呼び出し例: `/skills random-os-fake-it-hero-summon-notifier` または `random-os-fake-it-hero-summon-notifier` を含むコマンド
- 暗黙発動キーワード例: 「バグ」「デバッグ」「疲れた」「集中」「孤独」「やる気」「ヒーロー」などの文脈や、一定時間操作がない場合

# 出力例
```
[OS通知] 伝説のデバッグ勇者「メモリ・マスター」が召喚されました！
[OS通知] 今こそバグ退治の時！“コマンド使いのジョン”出動
[OS通知] シェルの魔法使い「Zshの賢者」が現れた！
[OS通知] あなたの作業を見守る“Gitの守護者”が加勢します
[OS通知] バグの洞窟に“Stack Overflowの精霊”が舞い降りました
```

# 注意点
- 本Skillは実用的な効能はなく、通知内容も完全に架空です。
- 作業データや環境に一切影響を与えません。
- ローカル通知はOSの通知API（notify-send, osascript等）を利用。環境によっては端末出力のみになる場合があります。
- 通知履歴や個人情報は保存しません。

# 参考資料
- [notify-send (Linux)](https://specifications.freedesktop.org/notification-spec/latest/)
- [osascript (macOS)](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/introduction/ASLR_intro.html)
- references/design_notes.md を参照