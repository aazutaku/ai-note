# 概要
本Skillは、作業中の緊張感を和らげるために、意味不明なOS風休憩通知をランダムに表示する演出系ツールです。実作業やファイルには一切干渉せず、純粋な気分転換・ユーモア注入を目的としています。

# 公式ドキュメント抜粋
- plyer: https://plyer.readthedocs.io/en/latest/
- notify-send: https://wiki.archlinux.jp/index.php/Notify-send
- osascript: https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/introduction/ASLR_intro.html

# 利用例
- チームの朝会や長時間作業時のリフレッシュ演出
- 一人作業の集中力維持や、会議のアイスブレイク
- /random-os-fake-breaktime-alert send で即座に通知、loopで定期的に発動

# 注意点
- OSの通知機能が無効・非対応の場合は標準出力のみ
- plyer未導入時はnotify-send/osascript/標準出力で代替
- ログや履歴は保存されません

# 設計方針
- ユーザー操作不要でランダム発動可能
- メッセージ内容・発動タイミングともにカオス性を重視
- 実作業やデータの安全性を最優先