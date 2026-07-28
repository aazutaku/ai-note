# 概要
このSkillは、ユーザーのコマンド実行や特定キーワード検知時に、複数の意味不明な進捗バーをランダム生成・描画することで、作業空間にカオスな演出を加えます。進捗テーマ・値は毎回ランダムで、実際の作業内容やOS進捗とは無関係です。

# 公式ドキュメント抜粋
- Python 標準ライブラリ (argparse, random, time, sys) のみ使用
- ANSIエスケープシーケンスでカラー進捗バーを描画
- CLIサブコマンド: festival, animate, list-themes

# 利用例
- `/skills random-os-mysterious-progressbar-festival` で即座に進捗バー群を表示
- `python mysterious_progressbar_festival.py animate` で10ステップのアニメーション

# 注意点
- 実際の進捗やOS状態とは一切連動しません
- ターミナルの種類によっては色や描画が崩れる場合があります
- ログや履歴の保存機能はありません

# 設計方針
- 完全なランダム性とカオスな演出を重視
- 外部依存なし、10-30分で導入可能
- 拡張: テーマ追加やバー数制御も容易