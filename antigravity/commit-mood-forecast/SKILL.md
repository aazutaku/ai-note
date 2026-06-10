---
name: commit-mood-forecast
description: Antigravityがgit commitアクションを検知した際、コミット内容や履歴に関係なく、毎回ランダムな“作業気分天気予報”コメントをターミナルへ表示します。commit, コミット, push, バージョン管理などのキーワードが含まれる操作時に発動します。
---

# 機能概要
commit-mood-forecastは、開発者がgit commit操作を行うたびに、完全ランダムな“本日の作業気分天気予報”をターミナルに表示するスキルです。天気アイコン風のテキストと短いコメントが毎回異なり、真面目な開発フローに遊び心をプラスします。実用性はありませんが、チームや個人の作業環境に和みや話題を提供します。

# 使い方
このSkillは明示的な呼び出しは不要です。Antigravityがgit commitやpushなどのバージョン管理操作を検知した際、自動的に発動します。暗黙的な発動キーワード例: commit, コミット, push, バージョン管理, git。

# 出力例
```
[commit-mood-forecast]
本日のあなたの作業気分天気予報：
快晴    ：今日は絶好調！やる気MAXで進めましょう。
---
[commit-mood-forecast]
本日のあなたの作業気分天気予報：
曇り    ：ちょっと迷い気味。無理せず一歩ずつ。
---
[commit-mood-forecast]
本日のあなたの作業気分天気予報：
雷      ：やる気ゼロ。コーヒーブレイク推奨！
```

# 注意点
- 出力はターミナル上の標準出力のみ。ファイル保存や通知機能はありません。
- 気分・天気は完全ランダムで、実際の作業状況や履歴とは無関係です。
- 過度に長いコメントや複雑な演出は行いません。
- 他のバージョン管理システム（例: Mercurial等）には未対応です。

# 参考資料
- references/design_notes.md に設計方針や利用例を記載
- 公式Git CLI: https://git-scm.com/docs/git-commit
- Python subprocess/標準出力: https://docs.python.org/ja/3/library/subprocess.html