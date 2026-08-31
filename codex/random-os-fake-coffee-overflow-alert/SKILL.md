---
name: random-os-fake-coffee-overflow-alert
description: 作業中や集中タイム、または/skillsメニューやrandom-os-fake-coffee-overflow-alertへの明示呼び出し時に、実用警告風の“コーヒーあふれ”通知をランダム発火。キーワード例: コーヒー、alert、集中、OS警告。
---

# 機能概要
このSkillは、作業中のデスクトップ環境に“OSコーヒーあふれ警告”をランダムで表示し、まじめな作業空間にユーモアをもたらします。通知内容は毎回異なり、「重大：コーヒーカップが満杯です」「警告：OSのカフェイン値が限界突破」など、現実には起こりえないデジタル・カフェイン事故を演出。作業効率や集中力を損なわず、ちょっとした息抜きやチーム内の話題作りに最適です。

# 使い方
- 明示呼び出し: `/skills menu` から本Skillを選択、または `$random-os-fake-coffee-overflow-alert` を直接メンション
- 暗黙発動: 「コーヒー」「alert」「集中」「OS警告」などのキーワードを含む会話や作業ログ中に自動発火
- CLI: `python coffee_overflow_alert.py trigger` で即時通知

# 出力例
```
[OS通知] 重大: コーヒーカップが満杯です。溢れる前に一時的なコーヒー断ちを推奨します。
[OS通知] 警告: システムのカフェイン値が限界を超えました。再起動を検討してください。
[OS通知] 注意: コーヒー残量が異常に多いです。作業効率低下の恐れあり。
[OS通知] エラー: 仮想マグカップがオーバーフローしました。
[OS通知] 情報: コーヒーインジェクションが検出されました。ご注意ください。
```

# 注意点
- 実際のシステム警告やエラーとは無関係です
- 通知はローカル環境でのみ表示されます（Linux/macOS: notify-send/osascript、Windows: win10toast利用）
- ネタ通知のため、重要な作業中の混乱を避ける用途での利用は非推奨
- ログや履歴はデフォルトで保存されません

# 参考資料
- [notify2](https://pypi.org/project/notify2/) / [win10toast](https://pypi.org/project/win10toast/) / [osascript](https://ss64.com/osx/osascript.html)
- references/design_notes.md 参照