---
name: mysterious-os-mood-bar
description: ターミナルでコマンド実行時や /mysterious-os-mood-bar 呼び出し時、コマンド内容やgit statusの雰囲気から“気分温度”や“やる気指数”を適当に算出し、OSのメニューバーやステータスバーへ冗談的に表示します。明示コマンドや on-demand キーワードで発動。
---

# 機能概要
mysterious-os-mood-barは、ターミナルでコマンドを実行するたびに、ユーザーの気分ややる気を“気分温度”や“やる気指数”として適当に判定し、OSのメニューバーやステータスバーに冗談めいたメッセージとして表示するSkillです。判定ロジックはコマンドの長さやgit statusの内容などから超適当に生成されるため、実際の気分とは全く関係ありません。日々の作業にちょっとしたユーモアや“未来予報”的演出を加え、真顔で見ているとじわじわ来る小ネタ枠として活用できます。

# 使い方
明示的には `/mysterious-os-mood-bar` コマンドで発動できます。また、ターミナルでコマンド実行時や「やる気」「気分」「テンション」などのキーワードを含む会話やスクリプト内で自動的に発動する場合もあります。設定不要で、コマンドごとに気分温度が無意味に変化します。

# 出力例
```
[OSメニューバー] 本日やる気-3度 (情熱沸騰中)
[OSメニューバー] やる気指数: 42%（気分：曇りのち晴れ）
[ステータスバー] 本日の気分温度: +12度（やる気急上昇）
[OSメニューバー] やる気-15度（省エネモード）
[ステータスバー] 気分指数: 99（やる気爆発中）
```

# 注意点
- 気分温度や指数は完全にランダムまたは冗談的に決まります。実際の気分や生産性とは無関係です。
- ユーザーの操作ログやデータは一切保存しません。
- メニューバー/ステータスバーへの表示にはOSごとの通知API（例: macOSではosascript、Linuxではnotify-send等）を利用します。
- 本Skillは小ネタ・演出目的であり、実用性や診断機能はありません。

# 参考資料
- [osascript (AppleScript)](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/introduction/ASLR_intro.html)
- [notify-send (Linux)](https://specifications.freedesktop.org/notification-spec/latest/)
- references/design_notes.md 参照