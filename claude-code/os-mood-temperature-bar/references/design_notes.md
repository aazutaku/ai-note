# 概要
本Skillは、作業中の「気分温度」を完全ランダムで生成し、OSのステータスバーやメニューバー風にターミナルへ出力する演出系ツールです。ユーザーの作業テンションを可視化することで、チームや個人の作業環境にユーモアとリフレッシュ効果をもたらします。

# 公式ドキュメント抜粋
- Python random: https://docs.python.org/ja/3/library/random.html
- argparse: https://docs.python.org/ja/3/library/argparse.html
- JSON: https://docs.python.org/ja/3/library/json.html

# 利用例
- ターミナルで `python os_mood_temperature_bar.py log` を実行し、その瞬間の「気分温度」を記録
- `list` で過去の気分温度履歴を閲覧
- `summary` で平均・最高・最低温度を確認

# 注意点
- 実際の気分や健康状態を反映するものではありません
- ログはローカルファイル（ユーザーホーム直下）に保存されます
- GUIのOSメニューバー統合はありません

# 設計方針
CLIサブコマンドでの操作性と、シンプルなJSONログによる履歴管理を重視。演出コメントは温度帯ごとに分岐し、カオスな演出を意図的に強調しています。