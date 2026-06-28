# 概要
本Skillは、開発現場にユーモアとリフレッシュをもたらすため、完全に架空のOSパッチノートをランダムなタイミングで通知するものです。通知内容はスクリプト内でランダム生成され、実際の作業や環境には一切影響を与えません。

# 公式ドキュメント抜粋
- plyer: https://plyer.readthedocs.io/en/latest/
- notify-send (Linux): https://specifications.freedesktop.org/notification-spec/latest/
- osascript (macOS): https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/

# 利用例
- チーム開発中のリラックスやアイスブレイク
- 長時間作業時の気分転換
- オンラインミーティング中の話題作り

# 注意点
- 通知内容は完全なジョークであり、実務やシステム運用に使うものではありません。
- ログはローカルファイル(.random_os_fake_patch_notifier.log)にのみ保存されます。
- 通知APIは環境依存のため、見え方や動作が異なる場合があります。

# 設計方針
- 実在APIのみを利用し、環境に依存しない安定動作を目指す
- 通知タイミング・内容ともに完全ランダム
- 履歴管理やサマリー表示など、最低限のCLI機能を実装