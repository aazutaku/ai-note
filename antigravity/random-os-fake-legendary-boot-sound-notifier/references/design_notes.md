# 概要
このSkillは、作業開始時などのトリガーで毎回異なる“伝説のOS起動音”名をテキスト通知として表示し、ユーザーにユーモアとリフレッシュを提供します。音声は一切鳴らさず、あくまで通知演出のみを目的としています。

# 公式ドキュメント抜粋
Python標準のrandom, argparse, logging, osモジュールのみを利用し、外部APIやサウンド再生は行いません。通知内容はローカルログファイル (~/.random_os_fake_legendary_boot_sound_notifier.log) に記録され、履歴やサマリ表示も可能です。

# 利用例
- ターミナルから `python boot_sound_notifier.py log` で即時通知
- `python boot_sound_notifier.py list --limit 10` で直近10件の通知履歴を確認
- `python boot_sound_notifier.py summary` でよく出る“起動音”名を集計

# 注意点
通知はテキストのみで、実際の音声や外部通知APIは使用しません。明示的な除外パスやサイレントモードは未実装です。

# 設計方針
Skillは冗長な外部依存を避け、シンプルなPythonスクリプトのみで完結。通知名は毎回ランダム生成し、ユーザー体験を飽きさせません。