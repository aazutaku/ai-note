# 概要
本Skillは、作業現場の空気を和らげるためのジョーク通知演出を目的としています。実際のウイルス検出やセキュリティ機能は一切ありません。

# 公式ドキュメント抜粋
Pythonのデスクトップ通知には、Windowsではwin10toast、macOSではosascript、Linuxではnotify2などのAPIを使用しています。
- win10toast: https://github.com/jithurjacob/Windows-10-Toast-Notifications
- notify2: https://pypi.org/project/notify2/

# 利用例
長時間の単調作業や、集中力が切れたタイミングで自動発動。SlackやTeamsの通知に飽きた現場でも、ちょっとした話題やリフレッシュのきっかけに。

# 注意点
通知内容は100%フィクションです。Skillは一切のファイル変更やシステム操作を行いません。通知履歴も保存されません。

# 設計方針
- 通知内容は毎回ランダム生成
- OSごとに最適な通知APIを選択
- 明示呼び出し不要・常時監視型
- 業務現場でも誤解されないよう、明らかにジョークと分かる内容のみ採用
