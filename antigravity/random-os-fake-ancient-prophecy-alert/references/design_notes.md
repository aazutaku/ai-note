# 概要
このSkillは、開発現場に遊び心と非日常感をもたらすことを目的とした演出系スキルです。完全な実用性よりも、通知演出の面白さ・多様性・干渉しない設計を重視しています。

# 公式ドキュメント抜粋
OS通知にはmacOSのosascript、Linuxのnotify-send、Windowsのwin10toastを利用しています。各APIの詳細は以下を参照してください。
- macOS: https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/
- Linux: https://specifications.freedesktop.org/notification-spec/latest/
- win10toast: https://pypi.org/project/win10toast/

# 利用例
- チームの朝会や作業中の気分転換
- コマンド実行直後のサプライズ通知
- "預言"や"未来"などのキーワード出現時の演出

# 注意点
通知内容は保存されず、業務上の警告やエラーとは一切関係ありません。Linuxではnotify-sendコマンドのインストールが必要な場合があります。

# 設計方針
通知内容は毎回ランダム生成され、他の通知や作業への干渉を最小化。CLIからも柔軟に呼び出せるよう設計しています。