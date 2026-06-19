# 概要
random-os-soundtrack-notifierは、作業開始時にOS通知で“今日の作業BGM”をランダムに提案し、日常のルーチンにユーモアと意外性を加えるためのSkillです。通知内容は実際に再生されず、ユーザーの集中や作業フローを妨げません。

# 公式ドキュメント抜粋
- [Python subprocess](https://docs.python.org/3/library/subprocess.html)
- [macOS osascript](https://ss64.com/osx/osascript.html)
- [Linux notify-send](https://specifications.freedesktop.org/notification-spec/latest/)
- [win10toast](https://pypi.org/project/win10toast/)

# 利用例
- ターミナルやエディタの起動時に自動発動し、BGMタイトルを通知。
- CLIから `python random_os_soundtrack_notifier.py notify` で手動実行も可能。
- 履歴やランキング表示で過去の通知を振り返る用途も。

# 注意点
- OS通知APIの制約により、通知が表示されない場合があります。
- Windowsはwin10toastが必要です（pip install win10toast）。
- ログファイルはホームディレクトリに保存されます。

# 設計方針
- 外部APIやネットワークアクセスを排除し、セキュリティと安定性を重視。
- ユーザーの作業を妨げない“理不尽なエンタメ”を追求しています。