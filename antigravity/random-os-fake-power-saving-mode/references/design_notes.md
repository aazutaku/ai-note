# 概要
このSkillは、実際のOSやアプリケーションには一切作用せず、作業者に対して“省エネモード突入”などのフェイク通知をランダムに表示することで、ユーモラスな演出と軽い現実感覚の揺さぶりを提供します。通知内容は毎回変化し、実害ゼロです。

# 公式ドキュメント抜粋
- Python公式: [random](https://docs.python.org/ja/3/library/random.html), [argparse](https://docs.python.org/ja/3/library/argparse.html), [logging](https://docs.python.org/ja/3/library/logging.html)

# 利用例
- 長時間作業時の気分転換や、チーム内でのジョーク演出
- 「最近パソコンが重い気がする」といった発言への自動応答

# 注意点
- 本Skillは通知演出のみで、実際のシステム設定やパフォーマンスには一切影響を与えません。
- ログ出力先を指定しない限り、履歴は残りません。

# 設計方針
- サブコマンド型CLI設計で、notify/list/summaryを明確に分離
- 通知文はテンプレート＋パラメータ挿入でバリエーションを確保
- OS依存のAPIや権限は一切使用せず、完全なノンインパクト設計
