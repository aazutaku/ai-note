# 概要
このSkillは、OSの通知APIを使い、ターミナル操作時に“言い訳”をジョークとして通知する演出用ツールです。Python標準のsubprocessと、各OSの通知手段（notify-send, osascript, win10toast）を採用しました。

# 公式ドキュメント抜粋
- Linux: notify-send (freedesktop.org)
- macOS: osascript (AppleScript)
- Windows: win10toast (PyPI)

# 利用例
- ターミナルで何か操作するたびに通知
- `/random-excuse-notifier notify` で明示的に通知
- `list`/`history` サブコマンドで言い訳一覧や履歴も確認可能

# 注意点
- サーバやWSLなど通知API未対応環境では端末出力のみ
- win10toastはWindowsでのみ動作し、pipでの事前インストールが必要
- 履歴はホームディレクトリの `.random_excuse_history` に保存

# 設計方針
- 直近の言い訳履歴を避けてランダム性を担保
- OSごとに最適な通知手段を自動選択
- コードは100行超の可読性・拡張性重視