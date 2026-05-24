# 概要
context-switch-logbookは、作業エージェントやブランチ、タスクの切り替え履歴をローカルで簡単に記録・参照できるCLI Skillです。主に複数タスクを横断する開発・運用現場で、作業経緯の可視化や振り返りを支援します。

# 公式ドキュメント抜粋
CLI設計にはPython標準のargparseを利用し、サブコマンド型UI（log, list, summary, delete）を採用。ログはJSON形式で ~/.context_switch_log.json に保存されます。

# 利用例
- エージェント切り替え時に `/skills context-switch-logbook log --from "dev" --to "review" --reason "レビュー依頼"`
- ブランチ作業開始時に `--from main --to hotfix --reason "緊急修正"`
- ログ一覧や傾向集計もワンコマンドで取得可能

# 注意点
ログはローカル保存のため、他端末やチーム共有には未対応。機密情報の扱いに注意し、必要に応じてファイルの権限管理を行ってください。

# 設計方針
シンプルな操作性と拡張性を重視し、CLIツールとして完結。今後は外部API連携やチームシェア機能も検討可能。