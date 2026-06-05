# 概要
random-excuse-notifierは、ターミナル操作や明示呼び出し時に、OSの通知領域へ完全ランダムな“言い訳”を表示する演出系Skillです。主に作業中の気分転換やユーモア提供を目的としています。

# 公式ドキュメント抜粋
- [notify2 (Linux)](https://pypi.org/project/notify2/)
- [plyer (クロスプラットフォーム通知)](https://plyer.readthedocs.io/en/latest/)
- [win10toast (Windows)](https://pypi.org/project/win10toast/)
- macOSではosascriptやterminal-notifierが利用可能

# 利用例
- ターミナルでコマンド実行時に自動発動
- `/skills menu`や明示呼び出しで手動発動
- 業務用途ではなく、純粋な“無駄演出”として利用

# 注意点
- 通知APIが利用できない環境では標準出力にフォールバック
- 履歴保存はメモリ上のみで永続化しません
- ネタが被りにくいよう履歴管理を実装していますが、完全な重複排除は行いません

# 設計方針
- OSごとに最適な通知手段を自動選択
- シンプルなCLIサブコマンド設計（log/list/summary）
- Skill本体から直接呼び出し可能な構造