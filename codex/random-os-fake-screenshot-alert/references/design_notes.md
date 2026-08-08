# 概要
このSkillは、実際には何も保存しないが、OS風の“スクリーンショット保存通知”をデスクトップにランダム表示することで、場の空気を和ませたり、緊張感を和らげるジョーク演出を提供します。

# 公式ドキュメント抜粋
- [plyer通知API](https://plyer.readthedocs.io/en/latest/)
- [notify-send(Linux)](https://specifications.freedesktop.org/notification-spec/latest/)
- [osascript(macOS)](https://ss64.com/osx/osascript.html)
- [win10toast(Windows)](https://pypi.org/project/win10toast/)

# 利用例
- チーム開発中に突如表示して場を和ませる
- コマンド実行時の“謎の緊張感”演出
- 雑談やバグ報告時のネタ枠通知

# 注意点
- SSHやWSL、headless環境では通知が出ない場合があります
- 通知内容は毎回ランダムで、実害や実ファイル保存はありません

# 設計方針
- OSごとに標準的な通知APIを利用し、追加インストール不要を目指す
- 通知内容はリストからランダム選択、今後拡張も容易
- ジョーク性と安全性（実害ゼロ）を両立