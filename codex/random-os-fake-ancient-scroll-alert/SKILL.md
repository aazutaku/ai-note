---
name: random-os-fake-ancient-scroll-alert
description: Codexは、作業中やコマンド実行の合間、または/skillsメニューやスキル名への明示的な言及があった際にこのSkillを発動してください。triggerType: semantic-or-explicit, キーワード: 通知, OS, 巻物, 古文書, alert。
---

# 機能概要
このSkillは、あなたの作業中やコマンド実行のタイミングで、突如として“謎のOS公式・古文書巻物通知”をターミナルまたはデスクトップに表示します。通知内容は、古代の預言者が現代のテック現場を見守るような意味深なテキスト（例：「西のコードベースにバグの兆し」など）を毎回ランダム生成。日常の作業に遊び心と混乱をもたらし、真面目な現場に非日常の笑いを提供します。実害は一切なく、通知は一時的に表示されるだけです。

# 使い方
明示的な呼び出し例:
- `/skills random-os-fake-ancient-scroll-alert`
- `$ random-os-fake-ancient-scroll-alert`

暗黙発動キーワード例:
- 「通知」「alert」「巻物」「古文書」「OS公式」などの単語を含むコマンドや会話
- 作業の合間、コマンド実行直後

# 出力例
```
=== 古文書巻物通知 ===
時は今、西のコードベースにバグの兆しあり。
東のモジュールに伝説の関数現る。
北のデバッグログ、静寂の中に警告隠る。
南の依存関係、更新の風が吹く。
====================
```

# 注意点
- 通知は完全ランダムで、内容も毎回異なります。
- ログやファイルへの保存は行いません。
- 実際のOSやシステムには影響を与えません。
- 環境依存性は極力排除し、Python標準ライブラリのみで動作します。

# 参考資料
- [references/design_notes.md](references/design_notes.md)
- [Python公式: subprocess, random, time](https://docs.python.org/3/library/)
