# 概要
本Skillは、エラー発生時に開発者へ和風のユーモアを提供するための通知演出ツールです。技術的なエラー内容を一切参照せず、俳句のみをランダム表示することで、気分転換やストレス軽減を狙っています。

# 公式ドキュメント抜粋
- Pythonデスクトップ通知: [notify2 (Linux)](https://github.com/caronc/apprise)
- [win10toast (Windows)](https://github.com/jithurjacob/Windows-10-Toast-Notifications)
- macOS通知: osascript経由でAppleScript利用

# 利用例
- ターミナルで `python haiku_notifier.py log` を実行すると、即座に俳句通知が表示されます。
- エラー発生時にSkill連携から自動で呼び出す運用も可能です。

# 注意点
- 通知内容はエラーとは無関係です。
- 通知の自動消去はOS依存で、macOSでは明示的な消去は不可です。
- Web IDEやリモート環境では通知が表示されない場合があります。

# 設計方針
- シンプルかつOS横断的な通知実装
- 俳句リストは拡張可能
- ログ保存やエラー内容との連携はあえて行わず、混乱と和みを優先