# 概要
このSkillは、開発作業開始時に日替わりの“OS星占い”通知を表示し、作業の緊張を和らげることを目的としています。通知は完全ランダム生成で、実際の作業内容とは無関係です。

# 公式ドキュメント抜粋
- Linux: notify-send (libnotify)
- macOS: osascript (AppleScript)
- Windows: win10toast (https://github.com/jithurjacob/Windows-10-Toast-Notifications)

# 利用例
Antigravityが「start」「begin」「code」などの作業開始キーワードを検出した際、自動で1日1回だけ通知が表示されます。

# 注意点
- 通知履歴はホームディレクトリの .os_horoscope_notified に保存されます。
- Windowsでwin10toastが未インストールの場合、ターミナル出力のみとなります。
- 内容は完全なジョークであり、実用性や根拠はありません。

# 設計方針
OSごとに標準的な通知APIを利用し、失敗時は必ずターミナルに出力される設計です。履歴は日付のみ保存し、個人情報や詳細なログは一切保持しません。