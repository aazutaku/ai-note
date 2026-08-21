---
name: random-os-breakup-notifier
description: 作業中やコマンド実行時など、ユーザーが集中しているタイミングで“デジタル失恋通知”を突発的に発動。明示的な /skills menu 呼び出しや、breakup, notification, joke, OS, 失恋, 通知, 笑い などのキーワード検知時にも発動します。
---

# 機能概要
random-os-breakup-notifierは、作業中の緊張感や単調さを和らげるため、突如“謎のOS失恋通知”をデスクトップやターミナルに表示します。内容は毎回ランダムで、マウスやエディタ、ショートカットキーなど身近なデジタル存在がユーザーを振るというシュールなジョークを演出。真面目な現場に非日常の笑いを届け、リラックス効果やチーム内のコミュニケーション促進にも役立ちます。

# 使い方
- 明示呼び出し: `/skills menu` から「random-os-breakup-notifier」を選択、または `$random-os-breakup-notifier` を直接実行。
- 暗黙発動: 「breakup」「notification」「joke」「OS」「失恋」「通知」「笑い」などのキーワードが会話やコマンドラインに現れた際、自動的にランダムな通知が発動します。

# 出力例
```
[重要] あなたの愛用マウスが新しいパートナーに乗り換えました。
[悲報] エディタがそっとあなたのもとを去りました。
[通知] ごめん、今日からCtrlキーはAltキーと付き合うことに。
[警告] ターミナルがあなたのコマンドに飽きてしまったようです。
[速報] あなたのフォルダが別のユーザーと新生活を始めました。
```

# 注意点
- 本Skillはジョーク用途専用です。システムや作業内容には一切干渉しません。
- 通知内容はローカルに保存されません。
- 通知の表示にはOSごとの標準APIを利用しますが、環境によってはターミナル通知のみとなる場合があります。
- 重要な作業中の誤発動を避けたい場合は、Skillの一時停止を推奨します。

# 参考資料
- references/design_notes.md に設計方針や利用例を記載
- [Python公式notify2ドキュメント](https://pypi.org/project/notify2/)
- [macOS通知: osascript](https://ss64.com/osx/osascript.html)
- [Windows通知: win10toast](https://pypi.org/project/win10toast/)