# 概要
このSkillは、実際のOSズーム処理を一切行わず、純粋に“警告演出”としてフェイク通知を表示します。通知内容は毎回ランダムで、ユーザーや周囲の空気を和ませたり、ちょっとした混乱を演出する目的で設計されています。

# 公式ドキュメント抜粋
- Python subprocess: https://docs.python.org/ja/3/library/subprocess.html
- notify-send (Linux): https://specifications.freedesktop.org/notification-spec/latest/
- osascript (macOS): https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/

# 利用例
- オンライン会議やペアプロで、空気を一瞬で和ませる演出として
- 長時間作業時のリフレッシュや“謎のイベント”として

# 注意点
- 実際の画面ズームやシステム設定は一切変更しません
- 通知が表示されない場合は、OSの通知権限やコマンドの有無を確認してください

# 設計方針
- OSごとに最適な通知APIを選択し、失敗時はターミナル出力にフォールバック
- メッセージは拡張・追加可能な構造
- 実害ゼロの“演出専用”Skill