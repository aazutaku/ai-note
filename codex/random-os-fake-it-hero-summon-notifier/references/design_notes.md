# 概要
このSkillは、作業中の孤独感やマンネリを打破するため、IT界の“英雄召喚”風通知をOS標準API経由でランダム表示します。実用性はありませんが、エンタメ・癒やし・作業リフレッシュを主目的としています。

# 公式ドキュメント抜粋
- [notify-send (Linux)](https://specifications.freedesktop.org/notification-spec/latest/)
- [osascript (macOS)](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/introduction/ASLR_intro.html)
- [win10toast (Windows)](https://github.com/jithurjacob/Windows-10-Toast-Notifications)

# 利用例
- 長時間のコーディングやデバッグ時の気分転換
- チーム作業でのちょっとした話題作り
- 自宅作業やリモートワーク時の孤独緩和

# 注意点
- 実際の作業データや環境には一切影響を与えません。
- 通知内容は完全に架空で、実在の人物や団体とは無関係です。
- OS通知APIが利用できない場合は端末出力のみとなります。

# 設計方針
- OS依存を最小限にし、Linux/macOS/Windowsで動作可能に設計
- ログはユーザーホーム直下の隠しファイルに記録
- 英雄メッセージは今後拡張・カスタマイズ可能