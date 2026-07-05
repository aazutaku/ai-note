---
name: random-os-sentiment-shift-alert
description: 作業中やコマンド実行時、または/skillsメニューやrandom-os-sentiment-shift-alertへの言及があった際に発動。通知・演出・OS連携カテゴリの明示・暗黙トリガーを検知し、シュールなOS人格変化通知を表示します。
---

# 機能概要
このSkillは、ユーザーが作業に集中しているときや、明示的に呼び出した際に、デスクトップに「OSの人格が急変した」と宣言するシュールな通知を表示します。通知内容は毎回ランダムで、「本日よりツンデレモードです」「しばらく詩人になります」など、OSのキャラクターが突如変化した旨を伝えます。実際のOS設定や作業には一切影響しませんが、思わず二度見してしまう不条理な演出を提供します。仕事や開発の合間にちょっとした驚きや笑いをもたらし、マンネリな作業環境に刺激を与えます。

# 使い方
- 明示呼び出し例: `/skills random-os-sentiment-shift-alert` または `random-os-sentiment-shift-alert` へのメンション
- 暗黙発動キーワード例: 「通知」「人格」「モード」「キャラ」「演出」「OS」「シュール」などを含む会話やコマンド実行時

# 出力例
```terminal
[通知] OS通知: 本日よりツンデレモードで対応します。ご注意ください。
[通知] OS通知: しばらく詩人として案内します。ご容赦ください。
[通知] OS通知: 今からやたら上から目線になります。
[通知] OS通知: 本日よりOSは無口モードです。
[通知] OS通知: しばらく厨二病モードで動作します。
```

# 注意点
- 通知はユーザーのデスクトップにのみ表示され、OSやファイル設定、作業内容には一切影響しません。
- 通知内容はランダム生成され、実際のOS動作やUIには変更を加えません。
- ローカルに通知履歴や個人情報を保存することはありません。
- Linux/macOS: `notify-send` または `osascript` を利用。Windows: `win10toast` を利用。

# 参考資料
- references/design_notes.md 参照
- [notify-send (Linux)](https://specifications.freedesktop.org/notification-spec/latest/)
- [osascript (macOS)](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/introduction/ASLR_intro.html)
- [win10toast (Windows)](https://pypi.org/project/win10toast/)