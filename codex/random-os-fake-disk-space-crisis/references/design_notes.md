# 概要
このSkillは、現実のストレージ状況と無関係な“ディスク残量危機”通知をランダム生成し、ユーザーの端末に表示することを目的としたジョーク系演出ツールです。実害やシステム操作は一切ありません。

# 公式ドキュメント抜粋
- [notify-send (Linux)](https://specifications.freedesktop.org/notification-spec/latest/)
- [osascript (macOS)](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/introduction/ASLR_intro.html)
- [win10toast (Windows)](https://pypi.org/project/win10toast/)

# 利用例
- チームのリモート会議で突然フェイク通知を発生させて笑いを誘う
- プログラミング学習やペアプロ中に“正気度テスト”として利用

# 注意点
- 実際のディスク容量やファイルシステムには一切アクセスしません
- 通知内容は完全なランダム生成です
- 一部Linux環境ではnotify-sendが未インストールの場合があります

# 設計方針
- OSごとに標準API/CLIのみ利用し、追加依存は最小限
- テンプレートと単位は拡張容易なリスト構造
- 履歴やローカル保存は行わず、純粋な“その場限り”の演出に徹する