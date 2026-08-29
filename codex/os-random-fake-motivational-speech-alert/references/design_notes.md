# 概要
このSkillは、OSの通知機能を活用し、コマンド実行や作業タイミングでユーザーを“謎のOS公式”が熱く激励する演出を実現します。実害ゼロ・エンタメ特化設計です。

# 公式ドキュメント抜粋
- [notify-send (Linux)](https://specifications.freedesktop.org/notification-spec/latest/)
- [osascript (macOS)](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/introduction/ASLR_intro.html)
- [win10toast (Windows)](https://pypi.org/project/win10toast/)

# 利用例
- ターミナルで作業中に `/skills os-random-fake-motivational-speech-alert` を実行
- コマンド実行ごとに自動で発火
- 連続通知や全メッセージ一覧表示も可能

# 注意点
- OS通知APIは環境依存。Linuxはnotify-send、macOSはosascript、Windowsはwin10toast(Python)が必要
- 通知内容はジョークです。真剣に受け止めないでください

# 設計方針
- システムやファイルへの副作用ゼロ
- 毎回異なるメッセージで飽きさせない
- CLIサブコマンドで拡張性を確保