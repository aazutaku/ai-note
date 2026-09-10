# 概要
このSkillは、ユーザーの作業中に現実には発生しない“プリンタ紙詰まり”警告をOS通知として再現し、理不尽な演出や混乱を意図的に発生させるために設計されました。通知内容は完全ランダムで、毎回異なるファイル名やエラーコード、指示が含まれます。

# 公式ドキュメント抜粋
Linuxでは `notify-send`、macOSでは `osascript` を利用してOS通知を実現しています。仕様詳細は [Freedesktop Notification Spec](https://specifications.freedesktop.org/notification-spec/latest/) を参照。

# 利用例
- `/skills random-os-fake-printer-jam-alert alert` で即時通知
- `/skills random-os-fake-printer-jam-alert run --duration 600` で10分間ランダム通知

# 注意点
実際のプリンタや印刷処理には一切影響を与えません。通知APIが利用できない環境では標準出力に代替表示されます。

# 設計方針
理不尽さ・無関係さ・バリエーションを重視し、現実には起こりえない状況も積極的に演出します。履歴機能はセッション内のみ（永続化なし）で簡易実装。