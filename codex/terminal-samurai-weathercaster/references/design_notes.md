# 概要
terminal-samurai-weathercasterは、ターミナル起動時や明示呼び出しで、現実の天気やAPI参照を一切行わず、完全ランダムな侍風天気コメントを生成・表示するSkillです。作業開始時の演出や気分転換を主目的としています。

# 公式ドキュメント抜粋
- [Python random](https://docs.python.org/ja/3/library/random.html): ランダムな天気・コメント選択に利用
- [argparse](https://docs.python.org/ja/3/library/argparse.html): CLIサブコマンド・引数処理に利用

# 利用例
- ターミナルを開くたびに自動で侍コメントが表示され、開発現場の雰囲気を和ませる
- 明示的に `python samurai_weathercaster.py log` で発動履歴を記録
- `list` サブコマンドで過去の侍コメントを確認
- `summary` で発動傾向を分析

# 注意点
- 現実の天気や位置情報は一切利用しません
- 出力内容は完全にランダムです
- ログはローカルファイル (samurai_weather.log) のみ保存

# 設計方針
- シンプルなPythonスクリプトでOS・環境依存性を最小化
- ユーモアと演出性を重視し、実用性よりも体験価値を優先
