# 概要
このSkillは、開発現場の「作業マンネリ化」や「緊張感の緩和」を目的に、未来予言風の架空エラーメッセージをランダム表示します。実用性よりもユーモア・演出を重視した設計です。

# 公式ドキュメント抜粋
- Python random: https://docs.python.org/3/library/random.html
- argparse: https://docs.python.org/3/library/argparse.html

# 利用例
- ターミナルのコマンド実行時に自動発動し、気分転換や話題作りに。
- 明示的に`python random_os_fake_error_prophecy.py prophecy`で呼び出し、Slackやチャットに貼る用途も。

# 注意点
- 本物のエラー通知と混同しないよう、色分けやprefixで区別。
- ログはユーザーのホームディレクトリに保存、履歴や統計も確認可能。
- 実際のファイルやシステムには影響を与えません。

# 設計方針
- ランダム性と演出の自然さを両立。
- ログ・統計機能で「振り返り」も可能に。
- 拡張性（予言メッセージ追加や頻度調整）を考慮。