# 概要
本Skillは、作業中の緊張感を和らげるためのフェイクOSセキュリティスキャン通知をデスクトップに表示します。実際のシステム操作やファイルアクセスは行わず、完全にジョーク目的です。

# 公式ドキュメント抜粋
通知表示には Python の plyer.notification モジュールを利用しています。plyerはクロスプラットフォーム対応で、Windows/Mac/Linuxの標準通知APIを呼び出します。

# 利用例
- CLIから `python random_os_fake_security_scan.py scan --duration 20 --interval 3` で実行
- 明示コマンド `/random-os-fake-security-scan` で即時発動
- チームのリモート作業中にネタとして投入

# 注意点
通知APIが無効な場合や、仮想環境・一部のLinuxディストリビューションでは通知が表示されない場合があります。

# 設計方針
- メッセージは毎回ランダムで選択し、進捗バー演出を実装
- 実在API(plyer)のみ利用し、外部依存やシステム操作は排除
- ログや履歴は一切保存せず、ローカル通知のみ
