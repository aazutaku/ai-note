# context-branch-snapshot Skill 活用ガイド

## できること
- Claude Code の context (directory, path, memory) を snapshot で保存・分岐・復元
- monorepo でも package ごとに context を安全に切替
- onboarding, 長時間 session, 複数案の比較検討時に便利

## コマンド例
- `/context-branch-snapshot create [name]` で現在の context を snapshot
- `/context-branch-snapshot restore [name]` で保存済み snapshot を復元
- `/context-branch-snapshot list` で一覧表示

## 注意点
- スナップショットは .claude/skills/context-branch-snapshot/snapshots/ 配下に保存
- 不要な snapshot は手動で削除可能
- context window を圧迫しすぎないよう、適宜整理推奨