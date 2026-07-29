---
name: random-os-fake-patch-note-generator
description: このSkillは、Claude Codeでコマンド実行やファイル編集などのアクション時に自動発動し、または /random-os-fake-patch-note-generator で明示的にも呼び出せます。発動キーワード例: 実行、保存、ビルド、run、save、commit。
---

# 機能概要
random-os-fake-patch-note-generatorは、コマンド実行やファイル保存などの作業時に、まるで本物のOSアップデートのような“謎のパッチノート”を毎回ランダム生成し、ターミナルやデスクトップ通知として表示するSkillです。内容は完全に架空で、現実とは無関係なバグ修正・機能追加・既知の問題などが並び、作業のシリアスさを和らげ、オフィスや自宅の空気を一変させます。真面目な開発現場にユーモアとカオスを提供し、作業効率を下げすぎない絶妙な頻度制御も組み込まれています。

# 使い方
- 明示呼び出し: `/random-os-fake-patch-note-generator` をターミナルやチャットで入力
- 暗黙発動: `run`, `save`, `commit`, `build`, `実行`, `保存` などの操作時に自動表示
- CLIサブコマンド例: `python random_os_fake_patch_note_generator.py log` で過去のパッチノート一覧、`python random_os_fake_patch_note_generator.py summary` で直近の要約

# 出力例
```
=== OS Patch Note v3.14.159 ===
[新機能] コーヒーの温度を自動調整するAIを搭載
[バグ修正] 机の上の書類が片付かない問題を修正
[既知の問題] おやつの消費が止まらない
-------------------------------
=== OS Patch Note v2.71.828 ===
[改善] ウィンドウの角が丸くなりました（見た目のみ）
[バグ修正] 集中力が一瞬だけ上昇する不具合を修正
[既知の問題] 夕方になると眠くなる
```

# 注意点
- 出力内容は完全にフィクションです。実際のOSや作業には影響しません。
- ログはローカルファイルに保存されます（.os_patch_notes.log）。
- 頻度制御により、短時間連続発動は抑制されます。
- デスクトップ通知はOS環境によっては表示されない場合があります。

# 参考資料
詳細設計や参考実装は references/design_notes.md を参照。notify2, random, argparse等の標準/一般的ライブラリのみ利用。