# 概要
このSkillは、クロスプラットフォームで動作するデスクトップ通知APIを活用し、完全ランダムな“謎のOSメモ”を投下します。実用性は一切なく、ユーザー体験や遊び心を重視した設計です。

# 公式ドキュメント抜粋
- Linux: `notify-send` コマンドはFreedesktop.orgの通知仕様に準拠
- macOS: `osascript` によるAppleScript通知
- Windows: Python `win10toast`ライブラリ

# 利用例
- `/random-desktop-fake-os-memo` コマンドで即座に通知
- 会話中に「通知」「演出」などのキーワードで自動発動

# 注意点
- 通知内容は毎回異なり、再現性はありません
- ローカル通知のみで、履歴や保存機能はありません
- Windows利用時は`pip install win10toast`が必要

# 設計方針
通知APIのみを利用し、OSごとに最も標準的な方法で通知を実現。怪文書リストは拡張可能で、今後のバリエーション追加も容易です。