---
name: context-path-history-visualizer
description: Claude Code で複数のプロンプトやファイル間を移動した際、コンテキストのパス履歴や思考経路を自動で可視化したい場合に発動します。履歴の分岐・合流や出発点、編集フローの全体像を把握したいときに有効です。
---

# 機能概要
context-path-history-visualizer は、Claude Code 上でのプロンプトやファイル間の移動履歴（コンテキストパス）を自動的に抽出・記録し、ツリー状に可視化するスキルです。これにより、過去の思考経路や編集フロー、分岐点・合流点・回り道した箇所などを直感的に把握できます。検討漏れや再利用できる情報の発見、作業の出発点の確認など、コンテキスト管理の課題を解決します。

# 使い方
- 明示呼び出し例: `/context-path-history-visualizer list` または `/context-path-history-visualizer summary`
- 暗黙発動キーワード例: 「履歴を可視化」「過去の経路」「編集フロー」「分岐点」「作業の流れ」「どこから始めたか」などの発話時に自動発動

# 出力例
```
root
├── prompt_2024-06-01_10-00
│   ├── file_edit_main.py
│   │   └── file_edit_utils.py
│   └── prompt_2024-06-01_10-15
│       └── file_edit_config.yaml
└── prompt_2024-06-01_11-00
    └── file_edit_main.py
```

# 注意点
- 履歴はセッション単位で自動抽出され、ローカルファイルとして保存されます
- 除外パス（例: システムファイルや一時ファイル）は自動的に省略されます
- 履歴の完全性はセッション内の操作に依存します
- プライバシー保護のため、外部送信は行いません

# 参考資料
- [references/design_notes.md](references/design_notes.md)
- 公式: https://platform.anthropic.com/docs/claude-code
