# 概要
本Skillは、エラー検知時に開発者の気分転換・和み・話題作りを目的として、完全ランダムな和風俳句をOS通知で表示します。エラー内容には一切依存せず、通知の演出性を重視しています。

# 公式ドキュメント抜粋
- Python通知ライブラリ `plyer` : https://plyer.readthedocs.io/en/latest/
- macOS: `osascript` で通知、Linux: `notify-send`、Windows: PowerShell経由でトースト通知

# 利用例
- `python haiku_notifier.py monitor < error.log` でエラー出力を監視し、エラー検知時に俳句通知
- `/skills menu` や `notify` サブコマンドで即時俳句通知

# 注意点
- 通知内容は俳句のみで、エラー内容や詳細は一切通知されません
- OS通知APIの仕様により、環境によっては通知が表示されない場合があります
- ログ保存や履歴機能はありません

# 設計方針
- 俳句リストは拡張可能
- 複数OS対応のため、plyer優先・なければOS標準APIを利用
- 開発現場に“和風カオス”な演出をもたらすことを主眼としています