# 概要
このSkillは、実在しないOS機能やデバイスの“ライセンス失効”を模した通知を、Pythonスクリプトでランダムに生成・表示します。主に開発現場や作業中の息抜き、ジョーク用途を想定しています。

# 公式ドキュメント抜粋
- plyer: クロスプラットフォームな通知API。https://plyer.readthedocs.io/en/latest/
- notify2: Linux向け通知API。https://notify2.readthedocs.io/en/latest/
- Python標準: os, random, argparse, time

# 利用例
- `/skills random-os-fake-mystery-license-alert` で即時通知
- `python random_os_fake_mystery_license_alert.py loop --min-interval 600 --max-interval 1200` で10～20分ごとに自動通知
- `python random_os_fake_mystery_license_alert.py list` でテンプレート一覧

# 注意点
- 実際のシステムやファイルには影響を与えません。
- 通知内容は完全なフィクションです。
- 通知頻度が高すぎると作業妨害になる場合があります。

# 設計方針
- 実害ゼロ・外部送信ゼロ・ユーザー体験のみに特化
- CLIから柔軟に制御可能
- 拡張性を考慮し、テンプレートや対象アイテムはリストで管理