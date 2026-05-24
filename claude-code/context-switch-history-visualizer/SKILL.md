---
name: context-switch-history-visualizer
description: Claude Code の context 切替履歴（directory, repository, path）を時系列で可視化し、各作業の滞在時間や切替イベントを一覧表示する Skill。monorepo や複数タスクの AI coding workflow で、context の移動傾向や集中力低下を発見しやすくする。
trigger:
  type: semantic-or-explicit
  explicit: /context-switch-history-visualizer
category: 可視化・レポート
paths:
  - scripts/extract_context_switch_history.py
  - references/context_switch_history_format.md
---

# Context Switch History Visualizer

## 概要

Claude Code の session 履歴・メタデータから、directory や repository の context 切替イベントと各作業の滞在時間を抽出し、時系列で可視化します。monorepo や複数タスクを横断する AI coding workflow で、どの path を行き来したか・どこで滞在時間が長かったかを一覧表示します。

## 出力例

- 直近の context 切替履歴（時刻・path・滞在時間）
- directory/repository 境界の移動イベント
- 合計切替回数・平均滞在時間
- 機密情報や個人情報を含まない形で整形

## 実行手順

1. scripts/extract_context_switch_history.py を実行し、Claude Code の履歴データから context 切替イベントを抽出
2. references/context_switch_history_format.md のフォーマットに従い整形出力
3. 必要に応じて directory 境界や滞在時間の集計も表示

## 注意点

- node_modules, build, generated など不要な path は除外
- 機密・個人情報は出力しない
- 長時間 workflow での stale context に注意