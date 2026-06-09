# 概要
このSkillは、コマンドライン作業時のエラー体験をユーモラスに演出するため設計されました。エラー発生時に“OS風”のパロディメッセージを自動生成し、作業者の気分転換やチーム内コミュニケーションのきっかけを提供します。

# 公式ドキュメント抜粋
- Python公式: https://docs.python.org/ja/3/library/argparse.html
- OSエラー一覧: https://man7.org/linux/man-pages/man3/errno.3.html

# 利用例
- ターミナルで `python random_os_error_translator.py run "File not found: foo.txt"` を実行
- ログ閲覧: `python random_os_error_translator.py log --tail 3`
- サマリー表示: `python random_os_error_translator.py summary`

# 注意点
- 実際のエラー解決には元のメッセージを参照してください。
- システムクリティカルな操作では自動変換を抑制してください。

# 設計方針
- パターンは拡張容易なdict構造で管理
- ログ保存で再利用性・検証性を確保
- 明示/暗黙の両トリガーに対応
- 実在するAPIのみ利用し、外部依存を最小化