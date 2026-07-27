---
name: os-fake-urgent-patch-alert
description: 作業中やコマンド実行時などのタイミングで、Codexが「緊急OSパッチ通知」風のジョーク通知をランダムにデスクトップへ表示したい場合に発動。通知・緊張感・演出・ジョーク・パッチなどのキーワードが検出された際にも自動発動します。
---

# 機能概要
本Skillは、開発現場や作業中に“謎のOS緊急パッチアラート”をデスクトップ通知としてランダムに生成・表示します。通知内容は毎回異なり、「超重要：バグ『脳内会議ループが止まらない』を修正」「新機能：やる気を一時的に1.5倍に加速」など、実際には意味のない“ウソパッチノート”が爆誕。無駄な緊張感・笑い・混乱を演出し、チームの雰囲気を和ませたり、集中力が切れたときの気分転換にも役立ちます。通知は実害ゼロで、ローカル環境のみに影響します。

# 使い方
- 明示呼び出し例: `/skills os-fake-urgent-patch-alert` または Skillメニューから選択
- 暗黙発動キーワード例: 「通知」「パッチ」「緊急」「ジョーク」「演出」などの単語を含む会話やコマンド

# 出力例
```
[OS Patch Alert] 超重要: バグ「脳内会議ループが止まらない」を修正しました。
[OS Patch Alert] 新機能: やる気を一時的に1.5倍に加速するモードを追加。
[OS Patch Alert] セキュリティ強化: “無限リファクタリング”の脆弱性を一時的に封印。
[OS Patch Alert] パフォーマンス改善: “Slack通知が止まらない”問題を根本から対策。
[OS Patch Alert] 既知の問題: “金曜日の集中力低下”は引き続き調査中です。
```

# 注意点
- 実際のOSやシステムには一切変更を加えません。
- 通知はローカル端末のみに表示され、ログや履歴は残りません。
- 一部Linux環境では通知機能の依存パッケージ（libnotify等）が必要な場合があります。
- 本Skillは演出目的であり、業務システムや本番環境での利用は推奨しません。

# 参考資料
- references/design_notes.md 参照
- Python公式: https://docs.python.org/3/library/subprocess.html
- Linux notify-send: https://specifications.freedesktop.org/notification-spec/latest/
- Windows通知API: https://docs.microsoft.com/en-us/windows/win32/shell/notification-platform-overview