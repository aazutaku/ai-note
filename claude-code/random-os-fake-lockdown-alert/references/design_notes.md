# 概要
本Skillは、現実には発生し得ない『OSロックダウン通知』を完全ランダムな内容で生成し、チームや個人作業の場に一瞬の非日常を演出します。実際のファイルや環境には一切影響を与えません。

# 公式ドキュメント抜粋
- [Python random](https://docs.python.org/3/library/random.html)
- [argparse](https://docs.python.org/3/library/argparse.html)
- [notify-send (Linux)](https://man7.org/linux/man-pages/man1/notify-send.1.html)
- [osascript (macOS)](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/introduction/ASLR_intro.html)

# 利用例
- `/random-os-fake-lockdown-alert --notify` でデスクトップ通知
- `/random-os-fake-lockdown-alert alert --repeat 3 --interval 10` で10秒ごとに3回発令
- `/random-os-fake-lockdown-alert list` で過去発令履歴を表示

# 注意点
- 実際のシステムやファイルには何も影響を与えません。
- 通知内容は完全に架空で、演出目的です。
- 履歴はメモリ上のみで永続化されません。

# 設計方針
- シンプルかつ安全な構成
- OSごとの通知APIを自動判別
- ランダム性・非現実性・ジョーク性を重視