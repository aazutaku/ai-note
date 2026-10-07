# 概要
このSkillは、ユーザーの作業状況や文脈に関係なく、完全ランダムなタイミングで“OS公式警告”風の通知を表示することで、作業空間に緊張感や笑いをもたらす演出を目的としています。実用性は一切追求せず、理不尽な警告体験を重視しています。

# 公式ドキュメント抜粋
- Windows通知: https://docs.microsoft.com/en-us/windows/uwp/design/shell/tiles-and-notifications
- macOS通知: https://developer.apple.com/documentation/usernotifications
- Linux通知: https://specifications.freedesktop.org/notification-spec/latest/

# 利用例
- オフィスやリモートワーク中の“ネタ”として活用
- チームビルディングやイベントでのアイスブレイクに
- 真面目な作業空間に意図的な緊張感を演出

# 注意点
- 実際のウィンドウ制御やセキュリティ対策機能はありません
- 通知APIの利用には各OSの標準コマンドやPythonパッケージ（例: win10toast）が必要
- 通知が表示されない場合は環境依存のため、端末やOSの仕様を確認してください

# 設計方針
- 発動タイミングや内容は完全ランダム
- ログや履歴は一時的にメモリ保持のみ
- ユーザーの作業内容や実際の上司の接近とは無関係