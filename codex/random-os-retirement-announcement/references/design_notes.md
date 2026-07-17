# 概要
このSkillは、OSの擬人化キャラクターが突然退職や転職を宣言する通知を、完全ランダムな内容で発生させるジョーク系演出ツールです。作業中のちょっとした息抜きや、システムに親しみを感じたいユーザー向けに設計されています。

# 公式ドキュメント抜粋
- Linux: notify2 (https://pypi.org/project/notify2/)
- Windows: win10toast (https://pypi.org/project/win10toast/)
- macOS: terminal-notifier (https://github.com/julienXX/terminal-notifier)

# 利用例
- 長時間作業の合間に、唐突な別れの通知で気分転換
- チーム内の雑談ネタや、開発現場の和み用途

# 注意点
- 実用的な通知ではなく、完全なジョークです。
- 通知は1時間に1回までに制限されています。
- 通知履歴は保存されません。

# 設計方針
- OSごとに最適な通知APIを利用し、クロスプラットフォーム対応
- 内容は毎回ランダム生成、同じ通知が続かないよう工夫
- シンプルなCLIサブコマンド設計で明示/暗黙呼び出し両対応