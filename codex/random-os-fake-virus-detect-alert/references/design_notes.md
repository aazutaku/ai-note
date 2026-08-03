# 概要
このSkillは、作業現場にユーモアとリフレッシュをもたらすための完全ジョーク通知システムです。実害ゼロ・誤認ゼロを徹底し、通知内容は毎回カオスなオリジナルネーミングで構成されます。

# 公式ドキュメント抜粋
- plyer: https://github.com/kivy/plyer
- notify2: https://pypi.org/project/notify2/
- win10toast: https://pypi.org/project/win10toast/

# 利用例
- `/skills random-os-fake-virus-detect-alert` で即時発動
- Pythonスクリプトの `trigger` サブコマンドでCLIからも利用可能
- 定期通知モードで作業中のリフレッシュやチームのアイスブレイクに

# 注意点
- 実在のウイルスやセキュリティ脅威とは一切関係ありません
- 通知履歴や個人情報は一切保存されません
- 一部Linux環境では通知ライブラリの追加インストールが必要な場合があります

# 設計方針
- 100%ジョークと分かる文言のみ使用
- システムやユーザーデータへの影響ゼロ
- OSごとに最適な通知APIを自動選択
- CLIサブコマンドで柔軟な運用を実現