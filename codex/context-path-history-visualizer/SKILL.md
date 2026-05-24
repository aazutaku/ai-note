---
name: context-path-history-visualizer
description: Codexが複数のプロンプトやファイル間での作業経路や履歴を可視化したい場合、または「履歴」「経路」「分岐」「ツリー」「作業フロー」などのキーワードを含むリクエスト時に発動。
---

# 機能概要
context-path-history-visualizerは、Codexでの作業中に発生するプロンプトやファイル間の移動履歴（コンテキストパス）を自動で記録・可視化するSkillです。思考や編集の経路がツリー状に一覧表示されるため、過去の分岐点や合流点、作業の出発点、回り道したポイントなどを直感的に把握できます。これにより、検討漏れや再利用すべき情報の発見が容易になり、複雑な検討フローの整理や振り返りが効率化されます。

# 使い方
明示的な呼び出し例:
- `/skills menu` から context-path-history-visualizer を選択
- `$context-path-history-visualizer` とプロンプトで指定

暗黙発動キーワード例:
- 「履歴を見せて」「作業経路を可視化」「どこで分岐したか」「編集フローのツリー」「過去の流れを一覧」など

# 出力例
```
Context Path History Tree:
└── Start: main.py
    ├── edit: main.py:12-24
    ├── jump: utils.py:5-30
    │   └── edit: utils.py:10-20
    └── branch: experiment/
        ├── edit: experiment/test1.py
        └── edit: experiment/test2.py
```

# 注意点
- 履歴はセッション単位で自動抽出され、ローカル保存や特別な環境構築は不要です。
- 除外パスや一時ファイルは自動的にフィルタされますが、意図しない履歴が混入する場合は手動で除外設定も可能です。
- 極端に長大な履歴は要約表示されることがあります。

# 参考資料
詳細な設計方針や利用例は references/design_notes.md を参照してください。Codex公式ドキュメント（https://platform.openai.com/docs/）も参考にしてください。