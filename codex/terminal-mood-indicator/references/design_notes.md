# 概要
terminal-mood-indicatorは、環境変数や履歴ファイルを利用してユーザーの気分を可視化し、ターミナルの作業体験を演出するSkillです。Python標準ライブラリのみで完結し、OSやシェルを問わず利用できます。

# 公式ドキュメント抜粋
- os.environ: https://docs.python.org/3/library/os.html#os.environ
- argparse: https://docs.python.org/3/library/argparse.html
- json: https://docs.python.org/3/library/json.html

# 利用例
- 朝一番で `python mood_indicator.py set "やる気MAX"` を実行
- コマンド実行時に `python mood_indicator.py show` を.bashrcや.zshrcに追記して自動表示
- 過去の気分履歴を `python mood_indicator.py list` で確認

# 注意点
- シェルプロンプト自体を自動で変更するには、追加の設定やスクリプトが必要
- チームで共有する場合は各自の環境変数・履歴ファイルに依存

# 設計方針
- シンプルなCLI設計とし、拡張性を意識してサブコマンド形式を採用
- 履歴はJSONでローカルに保存し、プライバシーも配慮