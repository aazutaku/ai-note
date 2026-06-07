# 概要
このSkillは、現実には絶対に発生しない“OSパニック”通知をランダムに生成し、作業中のユーザーにデスクトップ通知として表示することで、ユーモラスなリフレッシュや集中力の緩和を目的としています。

# 公式ドキュメント抜粋
- macOS: `osascript`による通知表示 ([AppleScript公式](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/introduction/ASLR_intro.html))
- Linux: `notify-send` (freedesktop.org [manページ](https://man.archlinux.org/man/notify-send.1))
- Windows: `win10toast`またはPowershellによるトースト通知

# 利用例
- 長時間のコーディングやリモートワーク中に、作業の合間の“息抜き”として活用
- チームの雑談ネタや、集中しすぎたときのリマインダーとして

# 注意点
- 通知内容は現実の障害通知と絶対に混同されないよう、誇張・ユーモアを重視しています
- 通知頻度は1時間に1回以下を推奨。頻繁な通知は逆効果になることがあります
- 各OSで通知APIの仕様や権限により表示されない場合があります

# 設計方針
- シンプルで安全な通知のみを実装し、システムへの影響を極力排除
- ログ機能やサマリー表示により、通知履歴の可視化もサポート
- 拡張性を考慮し、通知メッセージや頻度のカスタマイズが容易な構成