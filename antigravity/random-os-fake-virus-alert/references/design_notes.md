# 概要
このSkillは、作業の合間に完全なジョークとして“ウイルスアラート風”通知を表示し、ユーザーの気分転換やリフレッシュを促すために設計されています。通知内容は本物と絶対に誤認されないよう、意図的にユーモアとフィクション性を強調しています。

# 公式ドキュメント抜粋
- Python subprocess: https://docs.python.org/ja/3/library/subprocess.html
- macOS通知: https://developer.apple.com/documentation/usernotifications
- Linux notify-send: https://specifications.freedesktop.org/notification-spec/

# 利用例
- 長時間のコーディングや単調作業中に、突如デスクトップ通知で笑いを誘う。
- チームメンバーへのサプライズや、ペアプロの合間の気分転換に。

# 注意点
- 本Skillは絶対に本物のウイルス検出やシステム異常と誤解されない表現のみを採用しています。
- OS標準APIのみを利用し、追加の外部ライブラリは不要です（Windowsのみwin10toastがあれば高速通知可能）。
- 通知履歴や個人情報の保存は一切行いません。

# 設計方針
- 通知内容のユーモア性と安全性を最優先。
- 作業の妨げにならない頻度・タイミング制御。
- ローカル環境への依存を極力排除し、どの主要OSでも動作することを重視。