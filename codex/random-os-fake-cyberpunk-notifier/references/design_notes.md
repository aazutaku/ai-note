# 概要
本Skillは、実在しないサイバーパンク風の通知をデスクトップ標準通知API経由で表示することを目的としています。現実のOS状態には一切影響せず、演出・気分転換・配信向けのネタ用途を重視しています。

# 公式ドキュメント抜粋
- macOS: osascript (AppleScript経由) [公式](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/introduction/ASLR_intro.html)
- Linux: notify-send (libnotify) [公式](https://developer.gnome.org/libnotify/)
- Windows: win10toast [PyPI](https://pypi.org/project/win10toast/)

# 利用例
- 作業中の気分転換や、配信・実況の演出
- SF・サイバーパンクな雰囲気を演出したいとき
- チーム内でのジョーク通知

# 注意点
- 通知は一時的で、履歴やログは残りません。
- 標準通知領域に表示されない場合は、OSや通知APIの設定をご確認ください。

# 設計方針
- クロスプラットフォーム対応
- 実在しない通知のみを厳選
- 迷惑にならない頻度・回数制御
- 追加パッケージ依存は最小限