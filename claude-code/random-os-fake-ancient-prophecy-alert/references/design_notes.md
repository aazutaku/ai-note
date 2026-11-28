# 概要
本Skillは、開発現場に遊び心と非日常体験をもたらすため、完全にジョーク用途として設計されています。意味深な“預言”が、作業の合間に通知として現れます。

# 公式ドキュメント抜粋
- Python subprocess: https://docs.python.org/3/library/subprocess.html
- Python random: https://docs.python.org/3/library/random.html

# 利用例
- ターミナルで `python ancient_prophecy_alert.py alert` を実行
- 明示呼び出し `/random-os-fake-ancient-prophecy-alert`
- 自動発動時は特定キーワードで通知

# 注意点
- 実用的な警告やエラー通知は一切含みません。
- 通知はローカル表示のみ。外部送信や保存は行いません。
- Linux/macOS/Windowsで動作しますが、Windowsはwin10toastが必要です。

# 設計方針
- ランダム生成の預言文で毎回異なる体験を提供
- 他の通知や作業と干渉しないよう配慮
- 明示・暗黙両方の発動に対応