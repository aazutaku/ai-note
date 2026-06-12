# 概要
このSkillは、日常的なコマンド操作や作業イベントの合間に、完全ランダムな祝福通知をOSの標準通知領域へ送信します。開発中の気分転換や、作業空間へのユーモア提供が主目的です。

# 公式ドキュメント抜粋
- macOS: [pync](https://github.com/setem/pync)
- Windows: [win10toast](https://github.com/jithurjacob/Windows-10-Toast-Notifications)
- Linux: [notify2](https://github.com/caronc/notify2)

# 利用例
- ターミナルで `python random_os_notification_confetti.py run` を実行し、バックグラウンドでランダム通知を受ける
- `monitor` サブコマンドでコマンド履歴ファイルを監視し、作業イベントごとに祝福
- `test` サブコマンドで通知動作確認

# 注意点
- 通知はローカルPCの通知APIに依存し、リモートやサーバー環境では表示されません
- 通知頻度は過剰にならないよう、前回通知時刻をファイル保存し制御します
- ユーザーの作業ログやコマンド履歴を直接保存・送信することはありません

# 設計方針
- シンプルな構成でOS横断的な通知API利用を優先
- ユーザーの作業を妨げない頻度・タイミングで祝福を挿入
- メッセージは完全ランダム選択、内容もネタ要素を重視