---
name: random-os-fake-telepathic-command-alert
description: このSkillは、作業やコマンド実行の合間に「OSがあなたの心の中のコマンドを検出した」とするフェイク通知をランダムで表示します。通知・演出・OS連携のキーワードが含まれる場面や、集中作業中の息抜きとして自動発動します。
---

# 機能概要
このSkillは、日常の作業空間に突如現れる「OSテレパシーコマンド検出通知」を演出します。実際には存在しないコマンドや妄想的な命令（例：「deploy to mars」「make coffee」など）を、まるでOSがユーザーの心を読んだかのようにランダムで通知。現実逃避や笑いを誘い、真面目な作業空間にユーモアと不条理な混乱をもたらします。実行中のコマンドや実データには一切触れず、完全に安全なフェイク通知のみを生成します。

# 使い方
このSkillは明示的な呼び出しを必要とせず、Antigravityが「通知」「演出」「OS連携」などのキーワードや、長時間の作業・コマンド実行の合間を検知した際に自動で発動します。手動での明示呼び出しはサポートされていません。

# 出力例
```
[Telepathic OS Alert]
あなたが心の中で考えたコマンドを検出しました：'brew install unicorn'
---
[Telepathic OS Alert]
念波検出：'sudo teleport /dev/brain mars:'
---
[Telepathic OS Alert]
OSがあなたの妄想コマンドを察知しました：'rm -rf bad_vibes/'
---
[Telepathic OS Alert]
思念コマンド受信：'make coffee --now'
---
[Telepathic OS Alert]
念波検出：'deploy to mars'
```

# 注意点
- このSkillは実際のコマンドやデータには一切アクセスしません。
- 通知内容は毎回完全ランダムで生成され、実行や記録はされません。
- ローカル環境に通知履歴等を保存しません。
- 本Skillはジョーク・演出目的であり、業務用途の通知とは区別してください。

# 参考資料
詳細な設計方針や参考実装例は references/design_notes.md を参照してください。公式Python通知APIについては https://docs.python.org/ja/3/library/subprocess.html および https://pypi.org/project/plyer/ をご覧ください。