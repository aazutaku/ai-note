# 概要
random-os-apology-notifierは、OS標準の通知API（plyer経由）を利用して、完全にフェイクな“謝罪通知”をランダムに表示します。主に職場やリモートワークの雰囲気作り、話題提供、ジョーク用途を想定しています。

# 公式ドキュメント抜粋
- plyer: https://github.com/kivy/plyer
- Python標準: argparse, random, time, threading

# 利用例
- `/random-os-apology-notifier once` で1回だけ通知
- `/random-os-apology-notifier loop -i 120 -n 5` で2分ごとに5回通知
- `/random-os-apology-notifier list` で全メッセージ表示

# 注意点
- plyerがインストールされていない場合は、標準出力にフォールバックします。
- 通知内容は完全にランダムで、実際のエラーや業務進行には影響しません。
- 通知APIの仕様上、環境によっては通知が表示されない場合があります。

# 設計方針
- シンプルで拡張性のある構成（メッセージ追加容易）
- CLIサブコマンドで柔軟な利用が可能
- 業務アラートと混同しないよう、タイトルや文面に明確な差別化