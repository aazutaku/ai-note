---
name: random-os-fake-printer-jam-alert
description: このSkillは、コマンド実行や作業中に“プリンタ紙詰まり警告”を完全ランダムなタイミング・内容で発生させます。triggerType: always/semantic。通知・警告・紙詰まり・プリンタ・理不尽などのキーワードや明示呼び出しで発動します。
---

# 機能概要
`random-os-fake-printer-jam-alert`は、現代のPC利用環境で突然「プリンタ紙詰まり」や「印刷エラー」などの謎のOS通知をランダムに発生させるSkillです。実際にはプリンタを使っていなくても、理不尽な警告や指示がデスクトップ通知またはターミナルに表示され、作業中のユーザーを小さく混乱させます。通知内容は完全ランダム生成で、紙詰まりやトナー切れ、謎のファイル名などバリエーション豊富な“あるある”を再現します。

# 使い方
- 明示呼び出し: `/random-os-fake-printer-jam-alert` を入力すると即時発動します。
- 暗黙発動: 「通知」「警告」「プリンタ」「紙詰まり」「理不尽」などのキーワードを含む会話やコマンド実行時に自動発動します。
- スクリプトは自動的にランダムな間隔で通知を生成し、OSの通知APIまたはターミナル出力を利用します。

# 出力例
```
[OS通知] 重要: プリンタで“report_2024.txt”が紙詰まりを起こしました。
[OS通知] 警告: 印刷待ちジョブが渋滞中です。トナーを補充してください。
[Terminal] エラー: ファイル“main.py”の印刷中に謎の紙詰まりが発生しました。
[OS通知] 注意: プリンタが“手動給紙”を要求しています。
[Terminal] 警告: プリンタが“未定義エラー”で停止しました。
```

# 注意点
- 本Skillは実際のプリンタ状態とは無関係です。
- 通知内容は完全に架空であり、実際の印刷ジョブやファイル操作には影響しません。
- ローカル環境でOS通知を利用する場合、`notify-send`(Linux)や`osascript`(Mac)等のAPIが必要です。
- ログや履歴はローカルに保存されません。

# 参考資料
- references/design_notes.md に設計方針や利用例を記載
- OS通知API: https://developer.gnome.org/notification-spec/ , https://developer.apple.com/documentation/usernotifications
