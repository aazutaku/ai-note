---
name: os-fake-random-sleep-mode-alert
description: 作業やコーディングの集中が長時間続いた場合や、/os-fake-random-sleep-mode-alert コマンドが明示的に呼ばれた際に発動。通知・アラート・スリープ・休憩・OS管理などのキーワード検知時にも自動発火します。
---

# 機能概要
このSkillは、OSの公式通知を装って「強制スリープモード突入」などの理不尽なアラートをランダムなタイミングで表示します。実際のスリープや休止動作は一切行わず、作業中にユーモラスな緊張感やリフレッシュ効果をもたらします。通知内容は毎回ランダム生成され、まるでOSが勝手に生活リズムを管理しているかのような演出を体験できます。長時間の作業や集中の合間に、気軽な気分転換や話題作りとして最適です。

# 使い方
- 明示呼び出し: `/os-fake-random-sleep-mode-alert` を実行
- 暗黙発動: 「通知」「スリープ」「休憩」「アラート」などのキーワードを含む会話やコード内で自動発火
- スクリプトはCLIから `python os_fake_random_sleep_mode_alert.py` で起動可能

# 出力例
```
[OS ALERT] 重大: あなたのPCは3分後に強制的に昼寝モードへ移行します。
[OS WARNING] 警告: 集中力がOS基準値を下回りました。自動スリープを推奨します。
[OS NOTICE] 注意: システム管理者の指示により、5分間の休憩モードが推奨されます。
[OS ALERT] 重要: 連続作業が検出されました。健康維持のため休憩を強く推奨します。
[OS WARNING] 警告: マウス/キーボード操作が一定時間ありません。自動スリープ準備中です。
```

# 注意点
- 実際にPCがスリープや休止状態になることはありません。
- 通知は標準出力またはデスクトップ通知で表示され、ローカルファイルへの保存は行いません。
- 業務や重要作業中の誤解に注意してください（本物のOS通知ではありません）。
- Linux/macOS/Windowsの主要デスクトップ通知APIに対応。

# 参考資料
- references/design_notes.md
- [Python公式: notifications/toast通知](https://pypi.org/project/plyer/)
- [OS通知API: Windows Toast, macOS Notification Center, Linux notify-send]