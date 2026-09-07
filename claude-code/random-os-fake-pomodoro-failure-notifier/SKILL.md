---
name: random-os-fake-pomodoro-failure-notifier
description: Claude Codeがポモドーロタイマー開始や終了、または明示的なコマンド呼び出し（/random-os-fake-pomodoro-failure-notifier）を検知した際に発動します。triggerType: always/semantic。キーワード例: タイマー, ポモドーロ, 集中, timer start, pomodoro。
---

# 機能概要
このSkillは、ポモドーロタイマーの開始・終了時に、架空のOSから“ポモドーロ失敗”をテーマにしたフェイク通知をランダムに生成し、デスクトップやターミナルに表示します。通知内容は毎回異なり、「失敗：トマトが爆発しました」や「警告：集中力が鍋底にこびりつきました」など、実用性ゼロのユーモラスな演出で、まじめに集中したい時ほど謎の邪魔が入ります。エンタメ性重視で、作業の合間に笑いを提供します。

# 使い方
- 明示呼び出し：`/random-os-fake-pomodoro-failure-notifier start` または `end` サブコマンドで通知を発生させます。
- 暗黙発動："ポモドーロ", "タイマー開始", "timer start", "pomodoro" などのキーワードを含む会話やコード実行時に自動で発動します。

# 出力例
```
[FakeOS Notification]
失敗: トマトが爆発しました。机の上が真っ赤です。

[FakeOS Notification]
警告: 集中力が鍋底にこびりつきました。再加熱してください。

[FakeOS Notification]
注意: タイマーがピザに変身したため無効です。

[FakeOS Notification]
エラー: ポモドーロがカプレーゼサラダになりました。
```

# 注意点
- 本Skillは実際のタイマー機能や進捗管理は行いません。
- 通知は完全なジョークであり、実用性や生産性向上は期待できません。
- ローカルファイルやシステム設定には一切変更を加えません。
- 10分程度で動作確認できる簡易設計です。

# 参考資料
詳細な設計方針や通知文例、API仕様は references/ 以下や公式Pythonドキュメント（https://docs.python.org/3/library/random.html, https://docs.python.org/3/library/subprocess.html）を参照してください。