---
name: context-branch-snapshot
description: |
  Claude Code の context (directory, path, memory) を一時的に分岐・スナップショット化し、好きなタイミングで復元・切替・比較できる Skill。monorepo や長時間 workflow での context 管理・onboarding 効率化に最適。
category: コンテキスト管理
trigger:
  type: semantic-or-explicit
  explicit: /context-branch-snapshot
  description: スナップショット, context 分岐, context 戻す, context 比較, context 復元, context 切替
---

# context-branch-snapshot Skill

## 概要

Claude Code の作業 context (directory, path, memory, repository understanding) を snapshot として保存・分岐・復元・比較できる Skill です。
- 明示コマンド (/context-branch-snapshot) または semantic マッチで発動
- monorepo や複数 package の context を安全に切り替え
- 長時間の AI coding workflow で重要な context を保持
- onboarding や session 再開時に即座に context を復元

## 使用方法

- snapshot の作成:  
  `/context-branch-snapshot create [name]`  
  現在の context を name 付きで保存

- snapshot の復元:  
  `/context-branch-snapshot restore [name]`  
  指定した snapshot から context を復元

- snapshot の一覧:  
  `/context-branch-snapshot list`  
  保存済み snapshot を一覧表示

## 例

```
/context-branch-snapshot create design-proposal-A
/context-branch-snapshot restore core-main
/context-branch-snapshot list
```

## 注意事項

- snapshot ごとに context (directory, path, memory) を完全に分離
- context 混在やデータ損失は発生しません
- 不要な snapshot は定期的に削除推奨