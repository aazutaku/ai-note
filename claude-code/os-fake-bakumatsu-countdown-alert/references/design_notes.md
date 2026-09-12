# 概要
このSkillは、CLIやデスクトップ環境に幕末日本をテーマにしたパロディカウントダウンアラートを無害に表示することを目的としています。通知内容は毎回ランダム生成され、歴史的な出来事や人物をもじったテキストで演出を行います。

# 公式ドキュメント抜粋
- Python標準の `argparse` によるCLIサブコマンド設計
- macOS: `osascript`、Linux: `notify-send`、Windows: PowerShell経由のToast通知を利用
- すべての通知はユーザー空間のみで完結し、システム設定やファイルには一切影響しません

# 利用例
- `/os-fake-bakumatsu-countdown-alert` コマンドで即時発動
- CLIで `python bakumatsu_countdown_alert.py log --desktop --countdown` など
- 作業中の気分転換やイベント演出、ネタ枠として活用

# 注意点
- 通知内容や残り時間は完全ランダムです
- ログや履歴は保存されません
- 一部のLinux/Windows環境では通知APIが未インストールの場合があります

# 設計方針
「実害ゼロ」「歴史パロディ」「毎回異なる演出」を重視し、通知APIの標準的な実装のみを採用しています。