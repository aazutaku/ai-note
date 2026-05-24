---
name: context-hopper
description: |
  進行中の複数タスクやブランチ間で、直近の作業コンテキスト（要点や課題、メモ）を自動でsnapshot/restoreし、Antigravityに適用するSkill。repository understanding・path管理・重要なmemoryの維持をサポートし、AI coding workflowの混線や記憶負荷を軽減する。
trigger:
  type: semantic-match-only
category: コンテキスト管理
verificationFocus:
  - 切替時に要約や課題が正確に提示されるか
  - 複数タスク間で情報が混線しないか
  - 保存・復元操作がシンプルか
---

# context-hopper

## 概要
- 複数タスク・複数ブランチの作業context（要点・課題・メモ）を自動でsnapshot/restore
- session再開・monorepo移動・onboarding時などに、最小プロンプトでcontextを復元
- directory単位・package単位でrepository understandingを維持

## 指示

- 作業ディレクトリ・直近の課題・重要メモを自動要約しsnapshotとして保存する
- 保存済みsnapshotからcontextを復元し、Antigravityのmemoryに適用する
- monorepoや長時間workflowでも、必要なdirectory boundary・path管理を意識してcontextを切り替える
- irrelevantなpath（node_modules, build, dist等）は除外
- 重要な未解決課題やメモはcontext内で強調
- 出力フォーマットは references/context-format.md に準拠

## 期待する出力例

- repository名、作業ディレクトリ、直近タスク、未解決課題、重要メモ、主要ファイルなどを箇条書きで提示
- monorepoの場合はpackage間依存も明示
- context復元時は「このcontextをAntigravityに適用しました」などの完了メッセージを出す