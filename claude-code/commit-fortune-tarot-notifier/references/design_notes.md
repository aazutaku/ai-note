# 概要
commit-fortune-tarot-notifierは、Gitのcommit操作にユーモアを加えるためのジョーク系Skillです。開発現場の雰囲気を和らげ、コミュニケーションのきっかけを作ることを目的としています。

# 公式ドキュメント抜粋
- [Git Hooks](https://git-scm.com/docs/githooks): Gitのcommit時にスクリプトを自動実行する仕組み。
- [Python random](https://docs.python.org/3/library/random.html): 完全ランダムなメッセージ生成に利用。
- [plyer](https://pypi.org/project/plyer/): クロスプラットフォームな通知API。

# 利用例
- post-commitフックに本スクリプトを登録することで、毎回異なるタロットメッセージが表示されます。
- ターミナル通知だけでなく、デスクトップ通知もサポート。

# 注意点
- 実際の運勢や開発品質には一切影響しません。
- ローカル環境依存のため、CI/CDやリモート実行では動作しません。

# 設計方針
- シンプルな導入と運用を重視。
- 履歴記録や統計機能で、長期的な楽しみも提供。