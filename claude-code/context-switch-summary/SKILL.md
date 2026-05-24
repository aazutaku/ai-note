---
name: context-switch-summary
description: |
  Claude Code の作業セッションで、タスク切り替えやブランチ移動の直前に進捗・変更点・TODO・directory 構造などを自動要約し、再開時に参照できるメモを生成する Skill。repo の履歴やdiffを解析し、AI coding workflow の context 管理・path management をサポート。日本語/英語どちらにも対応。
category: コンテキスト管理
trigger:
  type: semantic-or-explicit
  explicit: "/context-switch-summary"
  semantic: ["作業切り替え", "セッション再開", "要約メモ", "context snapshot"]
references:
  - ./references/context-summary-format.md
scripts:
  - ./scripts/summarize_context.py
---

# Context Switch Summary Skill

## 概要

このSkillは、Claude Code での作業セッション中に「別のタスクやブランチへ切り替える直前」や「長時間 workflow の区切り」などで、直前の進捗・変更点・TODO・directory 構造などを自動で要約し、再開時に即参照できるメモを生成します。

## 実行指示

- 直前の作業内容・変更点・未完了TODO・現在のdirectory・branch・関連pathを抽出し、箇条書きで簡潔にまとめてください。
- 可能であれば git diff, git status, open files, recent commands も参照し、重要な変更や未commit内容を明示してください。
- monorepo や複雑な repository では、package boundary・directory boundary を明記してください。
- 出力は [Context Switch Summary] という見出しで始め、再開時に迷わない構成にしてください。
- 英語/日本語どちらでも出力できるようにしてください。

## 参考テンプレート

{{ ./references/context-summary-format.md }}