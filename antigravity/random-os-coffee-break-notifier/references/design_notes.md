# 概要
本Skillは、OS公式風のコーヒーブレイク通知を完全ランダムなタイミング・内容で表示し、作業空間に遊び心を提供することを目的としています。通知内容は説得力がありそうで全く役に立たないものを厳選しています。

# 公式ドキュメント抜粋
- PythonでのOS通知: https://docs.python.org/3/library/subprocess.html
- Windows通知: https://github.com/jithurjacob/Windows-10-Toast-Notifications
- Linux notify-send: https://specifications.freedesktop.org/notification-spec/latest/

# 利用例
- 長時間のコーディングや集中作業時のリフレッシュ促進
- チームの雑談ネタやリモートワークの雰囲気作り

# 注意点
- 実際のOSや業務通知と混同しないよう、通知タイトルや内容にジョーク性を持たせています。
- 履歴ファイルはユーザーHOME配下にのみ保存され、個人情報や機密データは一切記録しません。

# 設計方針
- クロスプラットフォーム対応（macOS, Linux, Windows）
- 完全ランダムなタイミングと内容、かつ実害ゼロ
- シンプルなCLIで履歴やサマリーも確認可能