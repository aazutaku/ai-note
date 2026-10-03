# 概要
このSkillは、ユーザーの作業体験に“謎のOS公式BGM推奨通知”という演出を加えることで、単調な作業やコマンド実行の合間に気分転換や小ネタを提供することを目的としています。実際に音は鳴らさず、通知やターミナル出力のみで安全に“雰囲気”を演出します。

# 公式ドキュメント抜粋
- Windows: win10toast (https://github.com/jithurjacob/Windows-10-Toast-Notifications)
- Linux: notify-send (https://specifications.freedesktop.org/notification-spec/latest/)
- macOS: osascript 経由の通知

# 利用例
- 長時間のコーディングやビルド後に唐突なBGMタイトル通知で気分転換
- チーム内のリモート作業時の雑談ネタやアイスブレイク

# 注意点
- 実際の音楽再生は行いません
- 通知APIの利用には各OSでの権限や環境設定が必要な場合があります
- ネタ要素が強いため、業務環境での利用は適切なタイミングを選んでください

# 設計方針
- クロスプラットフォームで動作し、OSごとに最適な通知APIを選択
- BGMタイトルは毎回ランダム生成で“ジャンル不明感”を重視
- ローカル保存や履歴管理は行わず、シンプルな演出に徹する