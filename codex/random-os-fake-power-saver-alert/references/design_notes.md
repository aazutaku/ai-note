# 概要
本Skillは、ユーザーの作業中に意図的な“省エネ警告”をデスクトップ通知で表示し、ちょっとした息抜きやネタ演出を提供します。実際のOSや電力管理には一切影響を与えません。

# 公式ドキュメント抜粋
通知機能には [plyer.notification](https://plyer.readthedocs.io/en/latest/) を利用しています。plyerはクロスプラットフォームで、Windows/Mac/Linuxの主要デスクトップ環境で通知が可能です。

# 利用例
- `/skills random-os-fake-power-saver-alert run -i 300` で5分ごとに通知
- `/skills random-os-fake-power-saver-alert add "省エネ: 今日は早めに帰宅しましょう。"` で新メッセージ追加
- `/skills random-os-fake-power-saver-alert list` で登録済みメッセージ確認

# 注意点
通知は一時的なもので、履歴やログは保存されません。大量通知や業務用端末での使用は控えてください。plyerの仕様上、Linuxではlibnotify等の追加パッケージが必要な場合があります。

# 設計方針
メッセージ内容は都度ランダム選択し、ユーザーが自由に追加・削除可能です。CLIサブコマンド設計で柔軟な運用を実現しています。