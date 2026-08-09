# 概要
このSkillは、懐かしのOSやソフトウェアの“サポート終了”通知を完全ランダムで表示する演出系ツールです。実際のシステムやファイルには一切影響せず、開発者の気分転換や話題作りに最適です。

# 公式ドキュメント抜粋
- [plyer通知API](https://plyer.readthedocs.io/en/latest/): クロスプラットフォームなデスクトップ通知を実現。
- [Python argparse](https://docs.python.org/3/library/argparse.html): CLIサブコマンド実装に利用。

# 利用例
- ターミナルから `python legacy_support_alert.py trigger` で即座に通知。
- `periodic` サブコマンドで一定間隔ごとに通知を発火。

# 注意点
- 通知履歴はメモリ上のみで永続化しません。
- 実際のサポート終了情報とは無関係です。

# 設計方針
- 実環境やデータを変更しない安全設計。
- 通知内容は完全ランダム・固定リストから選択。
- CLI/エディタからの呼び出し両対応。