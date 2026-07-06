# 概要
本Skillは「OS公式っぽい」説得力を持つ通知を、完全ランダムな間隔と内容でユーザーに送り、意図的に生産性を妨害するユーモアを提供します。Pythonのクロスプラットフォーム通知APIを活用し、実害やデータ損失が絶対に発生しない設計です。

# 公式ドキュメント抜粋
- Windows: win10toast, Powershell通知
- macOS: osascript (AppleScript)
- Linux: notify-send
- Python subprocess: https://docs.python.org/3/library/subprocess.html

# 利用例
- 長時間作業時の気分転換やチームの雑談ネタ
- ペアプロやリモートワークでの“理不尽な休憩”演出

# 注意点
- 通知内容はすべてSkill内で完結し、外部送信やファイル破壊等は一切ありません
- ログはホームディレクトリの隠しファイルにのみ保存されます

# 設計方針
- OS種別ごとに最適な通知方式を自動選択
- サブコマンドで履歴・要約も確認可能
- ユーザー体験を損なわない「安全なジョーク」用途に特化