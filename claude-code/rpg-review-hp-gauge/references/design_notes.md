# 概要
このSkillは、コードレビューの指摘数をゲーム的なHPゲージで表現し、開発現場に遊び心と可視化の工夫をもたらします。指摘数が多いPRはHPが減り、0になると「力尽きた」演出を表示します。

# 公式ドキュメント抜粋
GitHub REST APIのPull Request Review Commentsエンドポイント（[公式ドキュメント](https://docs.github.com/en/rest/pulls/comments)）を利用し、PRごとの指摘数を集計します。

# 利用例
- `/rpg-review-hp-gauge --pr 1234 --repo myorg/myrepo --total-hp 100`
- レビュー完了時の自動実行や、定期的なPRレビュー状況の可視化にも活用可能です。

# 注意点
- 指摘数の定義は「レビューコメント数」としており、レビュワーごとの重複や除外条件は現状未対応です。
- GitHub APIトークンが必須です。

# 設計方針
CLI/スクリプト形式でPR番号を指定し、HPゲージをターミナルまたはMarkdownで出力。HP減少率や初期値は柔軟に調整可能です。