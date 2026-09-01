# 概要
本Skillは、実際のOSコマンドやユーザーデータに一切アクセスせず、完全にランダムな“フェイクコマンド”通知を生成します。作業中の息抜きや、集中力が切れたタイミングで不条理な演出を提供することを目的としています。

# 公式ドキュメント抜粋
- Pythonの`subprocess`や`platform`モジュールを使い、OSごとの通知APIに対応。
- Windowsの場合は`win10toast`パッケージを利用（インストールされていない場合は標準出力）。
- [notify-send](https://specifications.freedesktop.org/notification-spec/notification-spec-latest.html)（Linux）、[osascript](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/introduction/ASLR_intro.html)（macOS）対応。

# 利用例
- `/random-os-fake-telepathic-command-alert`で明示的に発動
- 作業の合間やコマンド実行後に自動発動
- Slackやチャットの雑談ネタとしても活用可能

# 注意点
- 通知内容は完全に架空で、実行・記録・保存はされません。
- ユーザーのプライバシーやセキュリティに配慮し、実データには一切触れません。

# 設計方針
- ランダム性と安全性を重視し、妄想コマンドのバリエーションを豊富に用意。
- OSごとに適切な通知APIを選択し、環境依存の問題を回避。
- 履歴管理はメモリのみ（Skill実行中のみ有効）。