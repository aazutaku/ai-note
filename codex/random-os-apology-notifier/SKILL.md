---
name: random-os-apology-notifier
description: 作業中に突如『OSが無責任に謝罪する通知』をランダムに表示したい時や、職場の雰囲気を和ませたい場面で発動します。triggerType: always/semantic。通知内容は毎回異なり、実際のエラーや業務進行には影響しません。
---

# 機能概要
このSkillは、作業中のデスクトップに「謎のOS謝罪通知」をランダムなタイミング・内容で表示します。通知は完全にフェイクで、実際のエラーやシステム障害とは無関係です。例えば「本日はご迷惑をおかけしております」「原因不明の遅延が発生しました」など、OSがひたすら無責任に謝り続ける演出を楽しめます。リモートワークやオフィスでのムードメーカー、あるいはちょっとしたジョーク用途に最適です。

# 使い方
- 明示呼び出し例: `/skills menu` から random-os-apology-notifier を選択、または `$random-os-apology-notifier` メンションで即時発動。
- 暗黙発動キーワード例: 「OS 謝罪」「無責任」「通知ジョーク」「エラーっぽい演出」などを含む会話やコマンドで自動発動。

# 出力例
```
[通知] OSよりお詫び: 本日はご迷惑をおかけしております。
[通知] OSよりお詫び: 謎の遅延が発生しましたが、原因不明です。
[通知] OSよりお詫び: 先ほどの操作は無かったことにしてください。
[通知] OSよりお詫び: 何もしていませんが、一応謝っておきます。
[通知] OSよりお詫び: 予期せぬ問題が発生したかもしれません。
```

# 注意点
- 通知は完全なフェイクで、実際のシステムやファイルには一切影響しません。
- ローカル保存やログ記録は行いません。
- macOS/Linux の通知API (osascript/notify-send) を利用。Windowsでは動作対象外です。
- 通知内容は毎回ランダム生成。

# 参考資料
- [osascript (AppleScript) 公式](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/introduction/ASLR_intro.html)
- [notify-send (freedesktop.org)](https://specifications.freedesktop.org/notification-spec/notification-spec-latest.html)
- references/design_notes.md も参照