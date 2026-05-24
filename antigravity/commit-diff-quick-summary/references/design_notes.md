# 概要
このSkillは、コミット前の差分確認・要約をAIで自動化し、開発者のレビュー効率向上と見落とし防止を目的としています。git diffの出力をOpenAI APIに送信し、主要な変更点・影響範囲を日本語で簡潔にまとめます。

# 公式ドキュメント抜粋
- [git diff](https://git-scm.com/docs/git-diff): ファイル間の差分を表示
- [OpenAI Chat API](https://platform.openai.com/docs/api-reference/chat): AIによる自然言語要約

# 利用例
- コミット前に `python diff_quick_summary.py summary` を実行し、変更内容を短時間で把握
- レビュー前のセルフチェックや、意図しないファイル混入の検出

# 注意点
- 差分が大きすぎる場合は要約精度が低下するため、コミット粒度を適切に保つことを推奨
- OpenAI APIキーが必要（環境変数で指定）
- バイナリファイルや巨大diffは対象外

# 設計方針
- 追加ファイル不要・履歴非汚染・即時利用可能
- コマンドラインとAI要約を組み合わせ、既存ワークフローに自然に組み込める設計