---
name: random-os-fake-mystery-achievement-unlocked
description: コマンド実行や作業中に、Codexがランダムなタイミングで“謎のOS実績解除通知”を発動します。通知・演出・集中力低下などのキーワードがトリガー条件です。
---

# 機能概要
このSkillは、コマンド実行や作業の合間に、まるでOS公式のような“謎の実績解除通知”をランダムに表示します。通知内容は毎回異なり、「Ctrl+C連打名人」「5分間マウス未使用」「このコマンド誰も使ってない王」など、誰も求めていない称号が炸裂。作業中の集中力を絶妙にかき乱しつつ、謎の達成感とユーモアを提供します。通知はデスクトップ（Linux/macOS/Windows）またはターミナル上に表示され、日常の作業に遊び心を加えます。

# 使い方
- 明示呼び出し: `/skills random-os-fake-mystery-achievement-unlocked` またはスキルメニュー経由
- 暗黙発動: 「通知」「演出」「集中力低下」「実績」「OS連携」などのキーワードや、コマンド実行の合間に自動発動
- CLI: `python achievement_notifier.py run` で即時実績通知、`python achievement_notifier.py list` で称号一覧表示

# 出力例
```
[ACHIEVEMENT UNLOCKED] : ターミナルで5分間マウス未使用
説明: あなたの手はキーボードと一体化しました

[ACHIEVEMENT UNLOCKED] : Ctrl+C連打名人
説明: プロセスを止める速度が常人離れしています

[ACHIEVEMENT UNLOCKED] : このコマンド誰も使ってない王
説明: 世界初の実行記録が誕生しました
```

# 注意点
- 通知はローカル環境でのみ動作します（リモート/クラウド環境では制限あり）
- 通知履歴はファイル保存されません
- 実績内容はジョーク要素が強く、業務利用には不向きです
- OSの通知API（notify-send/win10toast/pync）に依存します

# 参考資料
- references/design_notes.md に設計方針や利用例を記載
- 公式API: https://notify.readthedocs.io/ , https://github.com/jithurjacob/Windows-10-Toast-Notifications , https://github.com/SylvainDe/py-notifier