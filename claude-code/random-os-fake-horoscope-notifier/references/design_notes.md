# 概要
このSkillは、開発者の日常にユーモアをもたらすため、完全にランダムな“OS風星占い通知”を1日1回自動生成・表示するものです。通知はターミナルとOSの両方に現れ、開発セッションの開始時や明示呼び出しで発動します。

# 公式ドキュメント抜粋
- [notify-send (Linux)](https://specifications.freedesktop.org/notification-spec/latest/)
- [osascript (macOS)](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/introduction/ASLR_intro.html)
- [win10toast (Windows)](https://pypi.org/project/win10toast/)

# 利用例
- 朝一番のターミナル起動時に自動で通知
- `/random-os-fake-horoscope-notifier` コマンドで明示的に呼び出し
- 過去10日分の通知履歴を`history`サブコマンドで確認

# 注意点
- 1日1回のみ通知。履歴は`~/.random_os_horoscope_history.json`に保存
- OS通知は環境によって失敗する場合がある（Linuxは`notify-send`コマンド、macOSは`osascript`、Windowsは`win10toast`が必要）

# 設計方針
- ユーザーの作業開始を楽しく演出するため、通知内容は完全に架空でネタ要素を重視
- OS横断的な通知APIをサポートし、どの環境でも分かりやすい通知体験を提供
- 履歴管理とエラーハンドリングを重視し、複数回通知や通知失敗時もユーザーに配慮