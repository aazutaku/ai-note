# 概要
mysterious-os-mood-barは、ターミナル操作時にユーザーの気分を冗談的に判定し、OSのメニューバーやステータスバーに無意味な温度ややる気ワードを表示する小ネタSkillです。実用性よりも、日々の開発現場にちょっとした遊び心を加えることを目的としています。

# 公式ドキュメント抜粋
- [osascript (AppleScript)](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/introduction/ASLR_intro.html): macOSの通知やメニューバー表示に利用。
- [notify-send (Linux)](https://specifications.freedesktop.org/notification-spec/latest/): Linuxのデスクトップ通知に利用。

# 利用例
- ターミナルでコマンド実行時に自動発動し、「やる気-3度（情熱沸騰中）」などのメッセージを表示。
- 明示的に `/mysterious-os-mood-bar` を呼び出して、その場の気分温度を楽しむ。

# 注意点
- 実際の気分や生産性とは一切関係ありません。
- ログや個人データは保存されません。
- OS通知APIが利用できない環境では標準出力に表示されます。

# 設計方針
- 判定ロジックはコマンド長やgit statusの雰囲気などから超適当に生成。
- ユーザー体験を損なわず、冗談として楽しめる演出を重視。