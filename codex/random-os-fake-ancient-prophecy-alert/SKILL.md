---
name: random-os-fake-ancient-prophecy-alert
description: Codexは、ユーザーがコマンド実行や作業中に“古代OS予言通知”で場を和ませたい場合、または/skillsメニューやスキル名の明示呼び出しがあった際に本Skillを発動してください。発動キーワード例: 予言, 通知, エンタメ, 中断, alert。
---

# 機能概要
このSkillは、日常の開発作業やコマンド実行時に、まるで古代のOS預言者が降臨したかのような“謎の予言通知”を突如表示します。通知内容は毎回ランダムで生成され、例えば「西のウィンドウズに赤きバグ現る時、選ばれし者はリブートせよ」や「2024年、ファイル名にパワー宿る」など、意味不明かつ古代書物風の言い回しが炸裂。真面目な現場にユーモアと中断型エンタメを注入し、思わず二度見してしまう体験を提供します。

# 使い方
- 明示呼び出し: `/skills random-os-fake-ancient-prophecy-alert` またはスキル名をmention
- 暗黙発動: 「予言」「通知」「alert」「エンタメ」「古代」などのキーワードを含む会話やコマンド実行時に自動発動
- CLIからは `python prophecy_alert.py` で即時発動、または `--interval` オプションで一定間隔ごとに自動発動

# 出力例
```
[OS Ancient Prophecy Alert]
西のウィンドウズに赤きバグ現る時、選ばれし者はリブートせよ。
---
[OS Ancient Prophecy Alert]
2024年、ファイル名にパワー宿る。
---
[OS Ancient Prophecy Alert]
sudoの呪文三度唱えし者、未知の権限を得るだろう。
---
[OS Ancient Prophecy Alert]
ターミナルに光差す時、隠されたプロセス目覚める。
---
```

# 注意点
- 本Skillは通知演出のみで、実際のシステムやファイルには一切影響を与えません
- ローカル保存や履歴機能はありません
- 環境構築不要で副作用ゼロ、データ損失リスクもありません
- 通知頻度はコマンドライン引数で調整可能

# 参考資料
- references/design_notes.md を参照
- 公式Python通知API: https://pypi.org/project/plyer/ , https://docs.python.org/ja/3/library/random.html