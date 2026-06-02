# 概要
commit-failure-haikuizerは、git操作の失敗時にエラーメッセージをもとに俳句を自動生成し、開発現場にユーモアと癒しをもたらすためのSkillです。

# 公式ドキュメント抜粋
- Git公式: https://git-scm.com/doc
- Python subprocess: https://docs.python.org/3/library/subprocess.html

# 利用例
- pushやcommit失敗時、即座に五・七・五の俳句が表示され、エラーの重さを和らげます。
- チーム開発での小ネタや、ペアプロ・レビュー時のアイスブレイクにも活用可能です。

# 注意点
- 俳句の内容はエラー文脈から自動生成されるため、必ずしも文意が正確とは限りません。
- ログは .commit_failure_haiku.log に追記されますが、容量肥大に注意してください。

# 設計方針
- テンプレートとランダム選択を組み合わせ、毎回異なる句を生成。
- サブコマンド(run/list/summary)で操作性を確保。
- 日本語エラー・英語エラー双方に対応し、汎用性を重視しています。