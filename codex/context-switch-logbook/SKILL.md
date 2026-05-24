---
name: context-switch-logbook
description: 作業エージェントやタスクの切り替え時（例: agent switch, branch change, context shift, task jump）に発動し、切り替え元・先・理由を記録するSkillです。明示的な呼び出しや、切り替え関連のキーワード検出時に自動発動します。
---

# 機能概要
context-switch-logbookは、作業エージェントやタスク、ブランチの切り替え時に、そのタイミング・切り替え元と先・理由メモを自動記録するSkillです。これにより「なぜそのタスクに移ったか」「どの順で作業したか」といった作業の流れや思考経路を後から簡単に振り返ることができます。コンテキストの喪失や作業履歴の断絶を防ぎ、複数タスク/エージェント間のスムーズな切り替えを支援します。

# 使い方
明示的には `/skills context-switch-logbook log --from agentA --to agentB --reason "バグ修正のため"` のようにCLIで呼び出します。また、"switch agent", "change branch", "jump task", "context shift" などのキーワードを含む発話や指示があった場合にも自動で発動します。記録済みのログは `list` サブコマンドで確認できます。

# 出力例
```
$ python context_switch_logbook.py log --from "dev" --to "review" --reason "レビュー依頼対応"
[2024-06-21 14:32:10] dev -> review: レビュー依頼対応
$ python context_switch_logbook.py list
[2024-06-21 14:10:00] main -> dev: バグ修正作業
[2024-06-21 14:32:10] dev -> review: レビュー依頼対応
```

# 注意点
ログはローカルのJSONファイル（.context_switch_log.json）に保存されます。他端末との同期やチーム共有は自動では行われません。記録対象は明示的な呼び出しまたはキーワード検出時のみです。機密情報の記載には注意してください。

# 参考資料
詳細設計やAPI利用例は references/design_notes.md を参照してください。公式CLI設計指針は https://click.palletsprojects.com/ を参考にしています。