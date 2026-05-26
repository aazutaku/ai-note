# 概要
このSkillは、開発者の気分状態を環境変数やシェルプロンプト、Slackステータス等にリアルタイムで反映することで、メンタルの可視化やチーム内コミュニケーションの促進を目指します。

# 公式ドキュメント抜粋
Slack Webhookの利用には https://api.slack.com/messaging/webhooks を参照。シェルプロンプトのカスタマイズは Bash のPS1やzshのPROMPT変数を利用します。

# 利用例
- 朝一番で `export MOOD='最高'` をセットし、プロンプトやSlackに気分を表示
- 気分が落ち込んだとき `python mood_light.py set --mood='つらい' --slack-webhook-url=...` で周囲に通知
- 日々の気分ログを `python mood_light.py summary` で集計

# 注意点
- 環境変数MOODはシェルごとに異なるため、ターミナルを跨ぐ場合は再設定が必要
- Slack通知はWebhook URLの管理に注意
- ログファイルはホームディレクトリ直下に保存されます

# 設計方針
- 実在API・標準的なシェルカスタマイズのみ利用
- ローカルで完結し、外部依存は最小限
- 日替わりネタやツッコミ文は拡張可能な辞書形式で管理