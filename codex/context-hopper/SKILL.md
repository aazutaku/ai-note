---
name: context-hopper
description: |
  複数タスクやブランチ間で作業コンテキスト（要点・課題・メモ）を自動保存・切替・復元するSkill。CodexのAI coding workflowで、repository understandingやpath managementの記憶負荷を軽減し、onboardingやlong context時のストレスを減らす。
category: コンテキスト管理
trigger:
  type: semantic-or-explicit
  explicit: ["/skills menu", "$skill-name mention"]
  semantic: ["context 切替", "context 復元", "onboarding", "monorepo", "directory", "repo 構造", "progress 要約", "課題リスト", "重要ファイル", "context snapshot"]
verificationFocus:
  - 切替時に要約や課題が正確に提示されるか
  - 複数タスク間で情報が混線しないか
  - 保存・復元操作がシンプルか
---

# context-hopper Skill 指示

## 目的
- ユーザーが複数タスクやブランチ間で、直近の作業コンテキストを即座に切替・復元できるようにする
- 各作業単位ごとに要約・課題・メモ・重要ファイルを自動で保持し、指示一つで現在のcontextに展開する
- onboardingやsession再開時も、repositoryやdirectory構造の要点を再現する

## 出力指針
- context切替/復元時は、下記情報を必ず提示:
  - repository名、作業ブランチ/ディレクトリ
  - 直近要約（進捗/課題/メモ/重要ファイル）
- monorepoの場合は、packages/*などディレクトリ単位でcontextを分離
- 長時間workflowやonboarding時は、重要なpathとdirectoryあらすじを要約
- irrelevantなpathやbuild成果物は除外
- 出力例は references/context-hopper-usage.md を参照

## 保存・復元フロー
- context保存: scripts/save_context.py で現在の要点・課題・メモを保存
- context復元: scripts/load_context.py で指定タスク/ディレクトリのcontextを出力

## 注意
- context混線やstale contextを防ぐため、タスク/ディレクトリ単位で分離管理
- 長大なrepoでは重要箇所のみ抽出