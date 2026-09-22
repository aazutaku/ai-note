# 概要
このSkillは、作業中の孤独感やマンネリを打破するため、OS通知やターミナルメッセージとして“英雄召喚”を演出します。実用性よりエンタメ性・気分転換を重視した設計です。

# 公式ドキュメント抜粋
- Python random: https://docs.python.org/ja/3/library/random.html
- notify-send (Linux): https://wiki.archlinux.jp/index.php/Notify-send
- osascript (macOS): https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/
- win10toast (Windows): https://github.com/jithurjacob/Windows-10-Toast-Notifications

# 利用例
- 長時間のコーディングやバグ修正時に、突発的な通知で気分転換
- チーム開発での“ネタ”演出やリモートワークの孤独対策

# 注意点
- 通知は完全な演出目的で、作業データや環境を変更しません
- 履歴はユーザーホーム配下にのみ保存され、個人情報は一切記録しません

# 設計方針
- OSごとに最適な通知APIを自動選択
- メッセージ・英雄名は拡張しやすい構造
- CLIサブコマンドで履歴・要約も確認可能