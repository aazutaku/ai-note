# 概要
本Skillは、作業環境に遊び心を加えるための演出系通知スクリプトです。歴史パロディと無意味なカウントダウンを組み合わせ、ユーザーの集中を邪魔しない範囲で気分転換を図ります。

# 公式ドキュメント抜粋
- Python公式: https://docs.python.org/ja/3/
- OS通知API: Windows (win10toast), macOS (osascript), Linux (notify-send)

# 利用例
- `/skills menu` から選択し、即時に幕末アラートを発動
- "カウントダウン"や"幕末"などの単語を含む会話時に自動発動
- `python bakumatsu_countdown_alert.py alert --os --log` でターミナル＋OS通知＋履歴記録

# 注意点
- 実際のシステム操作やファイル削除は一切行いません
- win10toastが未インストールの場合はpipで追加が必要
- 履歴ファイル(bakumatsu_alert.log)は同ディレクトリにのみ保存

# 設計方針
- 通知内容は毎回異なるよう乱数とテンプレートを組み合わせ
- OSごとの通知APIを自動判別し、最適な方法で表示
- コマンド履歴管理機能も実装し、ユーザーが通知履歴を振り返れるよう配慮