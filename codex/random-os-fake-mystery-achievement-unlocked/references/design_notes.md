# 概要
本Skillは、作業中にOS風の実績解除通知をランダムなタイミングで表示し、ユーザーの集中力を絶妙にかき乱すことを目的としています。通知内容はシュールかつ多彩な称号を用意し、飽きずに楽しめる設計です。

# 公式ドキュメント抜粋
- plyer: https://plyer.readthedocs.io/en/latest/
- win10toast: https://github.com/jithurjacob/Windows-10-Toast-Notifications
- pync: https://github.com/setem/pync

# 利用例
- ターミナルでコマンド実行中に自動発動
- `python achievement_notifier.py run` で即時通知
- `python achievement_notifier.py random-loop --min-interval 120 --max-interval 600` で作業中にランダム通知

# 注意点
- OSの通知APIに依存するため、各OSで必要なPythonパッケージのインストールが必要
- 実績内容はジョーク要素が強く、業務用途には向きません

# 設計方針
- 通知の存在感は強すぎず弱すぎず、集中を妨げすぎない絶妙なタイミングを狙う
- 実績リストを随時追加・拡張可能な構造
- ローカル環境での動作を前提