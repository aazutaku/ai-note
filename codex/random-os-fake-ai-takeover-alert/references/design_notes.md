# 概要
本Skillは、開発現場や勉強会などで「AIがOSを乗っ取った」かのようなフェイク通知を演出し、場を和ませることを目的としています。通知内容は完全に架空で、実際のシステム制御やファイル操作は一切行いません。

# 公式ドキュメント抜粋
- [plyer.notification](https://plyer.readthedocs.io/en/latest/#plyer.notification): クロスプラットフォームなPython通知APIの解説
- [notify-send (Linux)](https://specifications.freedesktop.org/notification-spec/notification-spec-latest.html)
- [osascript (macOS)](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/introduction/ASLR_intro.html)

# 利用例
- チームのリフレッシュタイムに突然AI警告を出して盛り上げる
- 勉強会やLTで「AI時代のOS」をネタにする
- 日常作業中のちょっとしたドッキリ

# 注意点
- 通知内容はジョークです。実務や本番環境での混乱を避けるため、利用シーンは選んでください。
- 通知履歴は~/.fake_ai_alert_history.logに記録されますが、個人情報や機密情報は含みません。

# 設計方針
- OSごとの通知APIを自動判別し、クロスプラットフォームで動作
- 履歴・サマリー機能で過去の通知内容を確認可能
- 乱用防止のため、通知間隔や最大回数を調整可能
