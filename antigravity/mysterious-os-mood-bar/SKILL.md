---
name: mysterious-os-mood-bar
description: ユーザーがターミナルでコマンドを実行するたびに、コマンド内容や長さ、git statusの雰囲気などから気分温度ややる気指数を適当に判定し、OSのメニューバーやステータスバーにランダムな気分ワードや温度を表示するSkillです。"気分"や"やる気"などのキーワードや、コマンド実行時に自動発動します。
---

# 機能概要
mysterious-os-mood-barは、ターミナルでコマンドを実行するたびに、ユーザーの気分ややる気指数を“超適当”に判定し、OSのメニューバーやステータスバーに「本日やる気-3度」「情熱沸騰中」などの無意味な温度や気分ワードを表示します。判定はコマンド長やgit statusの内容からランダムに行われ、実用性は一切ありません。未来予報的な演出を楽しみたい方や、作業中にふと笑いたい時におすすめの小ネタSkillです。

# 使い方
このSkillは明示的な呼び出しは不要です。ターミナルでコマンドを実行するたびに自動で発動します。暗黙的な発動キーワードには「気分」「やる気」「テンション」などが含まれます。Skillが動作すると、OSのメニューバーやステータスバーに気分温度ややる気指数が表示されます。

# 出力例
```
$ git status
On branch main
nothing to commit, working tree clean
[やる気指数: -3度 本日: 低気圧注意報]

$ ls -la
[情熱沸騰中 本日の気分: 37.2度]

$ echo "hello"
[やる気指数: 0度 本日: 無風]
```

# 注意点
- 判定ロジックは完全にランダムまたは冗談的です。当たることはありません。
- ユーザーの操作ログやデータは一切保存されません。
- OSのメニューバー/ステータスバー表示にはmacOSではosascript、Linuxではlibappindicator等のAPIを使用します。
- 実際の気分や健康状態とは無関係です。

# 参考資料
- references/design_notes.md
- https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/introduction/ASLR_intro.html
- https://python-gtk-3-tutorial.readthedocs.io/en/latest/menus.html