# 概要
本Skillは、作業に没頭しがちなユーザーに“謎のOSダウンタイム”というフェイク通知を送り、単調な空間に遊び心と一瞬の緊張感を提供します。実際のシステムやデータには一切影響しません。

# 公式ドキュメント抜粋
- Python argparse: https://docs.python.org/ja/3/library/argparse.html
- Python random: https://docs.python.org/ja/3/library/random.html

# 利用例
- `/skills os-random-fake-sudden-downtime-alert` で即座に通知
- 長時間の作業や「ダウンタイム」等の発話時に自動発動

# 注意点
- 通知は全てランダム生成で、現実の障害やOSイベントとは無関係です。
- 履歴は実行中のプロセス内でのみ保持し、永続化しません。
- 実際のOSやファイルには一切アクセスしません。

# 設計方針
- ユーザーの安全・安心を最優先し、冗談通知のみを提供
- CLIサブコマンドで通知履歴や統計も確認可能
- 拡張性を考慮し、通知文や理由・対策の追加が容易な構造