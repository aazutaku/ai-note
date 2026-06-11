---
name: random-os-startup-movie
description: ターミナルやエディタの起動、または /random-os-startup-movie コマンド実行時に、毎回異なる“架空OSの起動画面”をテキストアニメーションとして表示します。発動条件は『起動』『open』『start』『launch』などのキーワード検知、または明示的なSkill呼び出しです。
---

# 機能概要
このSkillは、ターミナルやエディタの起動時、または明示的なコマンド実行時に、毎回異なる“架空OS起動画面”をテキストアニメーションとして表示します。『Windows 11.5』『Antigravity 3000』『Codex Limited Edition』など、実在しないOS名や、意味不明な進捗バー、『AIを目覚めさせています』といった怪しい演出を自動生成。作業前の一瞬に、ありえない未来感と謎の緊張を演出し、実用性ゼロの“無駄な儀式”を楽しみたい方に最適です。

# 使い方
- 明示呼び出し: `/random-os-startup-movie` を実行
- 暗黙発動: ターミナル/エディタの起動、または『start』『open』『launch』『起動』等のキーワードを含む操作時に自動実行

# 出力例
```
[Codex Limited Edition OS] 起動中...
-------------------------------
| █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ | 12%
| モジュールを量子展開中
| ビットを配置中...
| AIを目覚めさせています
-------------------------------
System Ready. Welcome, Operator.
```

# 注意点
- 実用的な機能はありません
- 出力は毎回ランダム生成、ローカル保存や履歴機能はありません
- 既存のOSやシステムに影響は与えません
- 除外パス: システムクリティカルなスクリプトや自動化バッチでは発動しません

# 参考資料
- [references/design_notes.md](references/design_notes.md) に設計方針や利用例を記載
- 公式URL: https://ai-note.tech/skills/random-os-startup-movie