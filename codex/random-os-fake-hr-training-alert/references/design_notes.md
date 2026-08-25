# 概要
このSkillは、現実には絶対に体験したくない“謎の人事研修通知”を、ランダムでターミナルやデスクトップに表示する演出系ツールです。通知内容は毎回異なり、作業中の息抜きやジョークとして利用できます。

# 公式ドキュメント抜粋
- Python subprocess: https://docs.python.org/3/library/subprocess.html
- notify-send (Linux): https://specifications.freedesktop.org/notification-spec/latest/
- osascript (macOS): https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/

# 利用例
- `/skills menu`や`$random-os-fake-hr-training-alert alert --desktop`で即時通知
- `batch`サブコマンドで複数回通知の連発

# 注意点
- 通知内容は完全なフィクションであり、実在の人事イベントや個人情報とは無関係です。
- OSの通知APIやターミナル出力のみを利用し、ファイルやシステム設定には一切影響を与えません。

# 設計方針
- ランダム性・バリエーション重視で、テンプレートとタイトルを多数用意
- OSごとの通知APIを自動判別し、失敗時は必ずターミナル出力にフォールバック
- 履歴や記録を一切残さず、完全な一時通知のみを実現