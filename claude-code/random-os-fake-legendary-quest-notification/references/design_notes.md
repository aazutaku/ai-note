# 概要
このSkillは、現実には存在しない“伝説のOSクエスト”を通知としてランダム生成し、ユーザーの気分転換や遊び心を刺激することを目的としています。実際のシステムやファイルには一切影響を与えません。

# 公式ドキュメント抜粋
- Python subprocess: https://docs.python.org/ja/3/library/subprocess.html
- OS通知API: macOS (osascript), Linux (notify-send), Windows (win10toast)

# 利用例
- `/random-os-fake-legendary-quest-notification` で即座にクエスト通知
- デーモンモードで30分ごとに自動通知
- 履歴保存・閲覧・サマリー表示

# 注意点
- 実在の通知や業務連絡と混同しないよう明確に“フェイク”である旨を明示
- 履歴ファイルはユーザーのホームディレクトリに保存され、必要に応じて削除可能

# 設計方針
- OS依存部分はtry/exceptで安全にフォールバック
- クエスト内容はテンプレート+ランダム要素で毎回異なる体験を保証
- 実害ゼロ・データ損失ゼロの安全設計