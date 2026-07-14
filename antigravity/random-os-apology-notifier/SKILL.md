---
name: random-os-apology-notifier
description: 作業中やコマンド実行時など、通常の進行に影響を与えず、ランダムなタイミングやキーワード（例:通知, OS, 謝罪, 演出, フェイク, ユーモア）にマッチした際に、OSの通知領域へフェイク謝罪メッセージを表示します。
---

# 機能概要
random-os-apology-notifierは、作業中に突然OS風の謝罪通知をデスクトップへ表示するスキルです。実際のエラーや業務進行には一切影響せず、完全なフェイク通知として、OSが「原因不明の遅延」「謎の障害」「無責任な謝罪」などを繰り返します。職場やリモートワークの雰囲気を和らげたり、ユーモラスな演出を加えたい場合に最適です。

# 使い方
このスキルはAntigravityのsemantic-match-onlyトリガーにより、明示的な呼び出しは不要です。通知, OS, 謝罪, 演出, フェイク, ユーモアなどのキーワードや、作業進行中の任意タイミングで自動的に発動します。スクリプトはローカル環境で直接実行も可能です。

# 出力例
```
[通知] 本日はご迷惑をおかけしております。詳細は不明ですが、引き続きご理解ください。
[通知] 謎の遅延が発生しましたが、原因不明です。ご不便をおかけします。
[通知] 大変申し訳ありませんが、さっきのコマンドは無かったことにしてください。
[通知] 予期せぬ問題が発生しましたが、何も対応しません。
[通知] システムは正常ですが、念のためお詫び申し上げます。
```

# 注意点
- 本スキルは完全なフェイク通知であり、実際のエラーや業務進行には一切干渉しません。
- 通知はローカル環境のOS通知API（Windows: Toast, macOS: AppleScript, Linux: notify-send等）を利用します。
- 通知履歴やログはローカルにのみ保存されます。
- セキュリティや業務規定により、通知機能が制限されている場合は動作しません。

# 参考資料
詳細仕様や設計方針、各OSの通知API利用例は references/design_notes.md を参照してください。公式ドキュメント：
- Windows Toast Notifications: https://docs.microsoft.com/en-us/windows/uwp/design/shell/tiles-and-notifications/
- macOS AppleScript: https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/
- Linux notify-send: https://specifications.freedesktop.org/notification-spec/latest/