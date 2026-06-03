# 概要
本Skillは、コードレビューの指摘数をRPGのHPゲージとして可視化することで、レビューの進捗や緊張感を演出し、開発現場に遊び心を提供します。

# 公式ドキュメント抜粋
- [GitHub Pull Request Review Comments API](https://docs.github.com/en/rest/pulls/comments)
- [GitLab Merge Request Notes API](https://docs.gitlab.com/ee/api/notes.html)

# 利用例
GitHubのPR番号やGitLabのMR番号を指定することで、指摘数に応じたHPゲージをターミナル上に表示します。HPが0になると「力尽きた」演出が現れ、レビュー体験を盛り上げます。

# 注意点
- Botコメントやシステムコメントは自動で無視します。
- HPや減点値はカスタマイズ可能。
- APIトークンの管理に注意してください。

# 設計方針
シンプルなCLI設計とし、APIレスポンスの信頼性・拡張性を重視。レビュー文化にユーモアを加えつつ、実用的な指摘傾向の可視化を目指しました。