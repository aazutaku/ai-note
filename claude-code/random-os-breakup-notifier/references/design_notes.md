# 概要
random-os-breakup-notifierは、作業中に突発的な“デジタル失恋”通知を表示することで、ユーザーにリフレッシュや笑いを提供するジョーク系スキルです。通知内容は毎回ランダムで、OSごとに最適な通知APIを利用します。

# 公式ドキュメント抜粋
- macOS: [osascript](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/introduction/ASLR_intro.html)
- Linux: [notify-send](https://specifications.freedesktop.org/notification-spec/notification-spec-latest.html)
- Windows: [win10toast](https://pypi.org/project/win10toast/)

# 利用例
- チームの朝会で雰囲気を和ませたい時
- 長時間のコーディングや作業中にリフレッシュしたい時
- 雑談や「失恋」「別れ」などのキーワードが出た際のネタとして

# 注意点
- 通知内容はシステムや作業に影響しません。
- 一部の環境では通知が表示されない場合があります。
- 本Skillはジョーク用途専用です。

# 設計方針
- OS判定と通知APIの自動選択
- メッセージのバリエーションとランダム性重視
- シンプルなCLI構成と明示/暗黙両対応