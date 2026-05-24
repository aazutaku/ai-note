---
name: mysterious-os-mood-bar
description: コマンド実行時や /skills menu などの明示呼び出し時に、ユーザーの気分ややる気温度を冗談的に推定し、macOS/Linuxのメニューバーやステータスバーに即時表示するSkill。コマンド長やgit status等のキーワードをトリガーに発動。
---

# 機能概要
mysterious-os-mood-barは、ターミナルでコマンドを入力するたびに、ユーザーの気分ややる気温度を完全にランダムかつ冗談的に推定し、OSのメニューバーやステータスバーに「本日やる気-3度」「情熱沸騰中」などの無意味なワードを表示するSkillです。コマンドの長さやgit statusの雰囲気などを適当に参照し、まったく当たらない未来予報的な演出を楽しめます。作業中にふと目に留まると、じわじわとした笑いを誘う小ネタ枠として設計されています。

# 使い方
- 明示呼び出し: `/skills menu mysterious-os-mood-bar` または `mysterious-os-mood-bar` を直接実行
- 暗黙発動: コマンド実行時、`git status`や`make`などの開発系コマンド、または「やる気」「テンション」などの単語を含む操作時

# 出力例
```
$ ls -la
[MOOD BAR] 本日のやる気指数：-3度（低気圧注意報）
$ git status
[MOOD BAR] 情熱沸騰中！コードが踊り出す予感
$ make build
[MOOD BAR] やる気の雲行き：曇り時々晴れ
$ echo hello
[MOOD BAR] 平常運転。やる気温度：21度
$ mysterious-os-mood-bar --show
[MOOD BAR] 未来の自分に期待指数：42%
```

# 注意点
- 気分や温度の判定は完全にランダムまたは冗談的で、実際の心理状態やパフォーマンスとは無関係です。
- 出力はOSのメニューバー（macOS: AppleScript, Linux: libappindicator等）または標準出力に即時反映されます。
- ユーザーの操作ログやデータは一切保存されません。
- システムによっては追加ライブラリ（osascript, python-appindicator等）が必要です。

# 参考資料
- [AppleScript公式](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/introduction/ASLR_intro.html)
- [python-appindicator](https://wiki.ubuntu.com/DesktopExperienceTeam/ApplicationIndicators)
- references/design_notes.md 参照