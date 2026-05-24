---
name: context-timeline-annotator
description: |
  Claude Code の session 履歴や編集ログを時系列で列挙し、各ステップに短い意図注釈を自動付与する Skill。monorepo や複数タスクが混在する作業履歴を、directory や path ごとに流れと意図を整理する。
category: コンテキスト管理
trigger:
  type: semantic-or-explicit
  explicit: /context-timeline-annotator
  description: "履歴や編集経緯を時系列でまとめたい、意図の流れを短く把握したい場合"
script: scripts/timeline_annotator.py
references:
  - references/context-timeline-annotator-usage.md
---

# context-timeline-annotator

## 概要

Claude Code の session 履歴・編集ログ・やりとりを時系列で整理し、各ステップに短い注釈コメント（例：編集理由や意図）を自動付与する Skill。  
複数の directory や monorepo の package を跨ぐ作業でも、全体の流れや decision の経緯を簡潔に把握できる。

## 指示

1. Claude Code の session 履歴・編集ログ（ファイル編集・追加・削除・チャット履歴）を時系列順に列挙する
2. 各ステップごとに、編集ややりとりの意図・理由・タスク概要を簡潔な注釈（1行コメント）として付与する
3. directory や path、package の切り替わりを明示し、monorepo 構造を意識して整理する
4. 履歴の改変やデータ損失は絶対に行わない
5. 出力は時系列順、最大15件程度まで。重要なイベントを優先

## 出力例

[2024-06-14 10:03]  /src/app/main.py 編集開始  # 新機能追加のため
[2024-06-14 10:15]  /src/app/utils.py 編集  # 共通ロジックを移動
[2024-06-14 10:21]  /tests/app/test_main.py 追加  # テストケース追加

## 想定用途

- session 再開時の context 復元
- monorepo での package 跨ぎ作業履歴の整理
- onboarding 時の全体像把握
- 長時間 workflow の context snapshot