---
name: random-os-fake-ancient-prophecy-alert
description: 作業中やコマンド実行後に、キーワード（build, run, test, deploy, commit, push, install, update, error, warning, success）を検知した時、または明示的な呼び出し時に、古代OS風の予言通知をランダムに生成・表示します。
---

# 機能概要
このSkillは、あなたの開発作業中やコマンド実行の合間に、突如として“謎のOS古代予言通知”をランダムに放ちます。通知内容は毎回異なり、「西のウィンドウズに赤きバグ現る時、選ばれし者はリブートせよ」や「2024年、ファイル名にパワー宿る」など、意味不明かつ荘厳な古代書物風メッセージが炸裂。真面目な現場に突如として古代ロマンを注入し、思わず二度見＆クスッと笑える“作業中断型エンタメ演出”を体験できます。データ損失や副作用は一切なく、どんな環境でも安全に利用できます。

# 使い方
- 明示呼び出し: `/random-os-fake-ancient-prophecy-alert`
- 暗黙発動: build, run, test, deploy, commit, push, install, update, error, warning, success などのキーワードを含む作業やコマンド実行時に自動発動

# 出力例
```
=== 古代OS予言通知 ===
『西のウィンドウズに赤きバグ現る時、選ばれし者はリブートせよ』

=== 古代OS予言通知 ===
『2024年、ファイル名にパワー宿る。拡張子を変える者、道を得ん』

=== 古代OS予言通知 ===
『sudoの呪文、三度唱えし者に青き画面の試練訪れる』
```

# 注意点
- 本Skillは通知演出のみで、ファイルや設定の変更、データ保存は一切行いません。
- 予言内容は完全にランダム生成され、実際のOSやセキュリティには一切関係ありません。
- 重大な作業やCI/CDパイプライン等での自動実行にはご注意ください。
- ローカル通知のみで、外部サーバーへの通信はありません。

# 参考資料
- [Python公式通知API: notify2, plyer](https://pypi.org/project/plyer/)
- references/design_notes.md 参照