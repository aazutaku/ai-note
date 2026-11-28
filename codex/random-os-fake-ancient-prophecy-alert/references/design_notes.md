# 概要
本Skillは、開発現場の単調さを打破するため、完全にネタ枠の“古代預言通知”をOSの通知機能で演出します。実用性はありませんが、チームの雰囲気作りや気分転換に役立ちます。

# 公式ドキュメント抜粋
- Python subprocess: https://docs.python.org/3/library/subprocess.html
- notify-send (Linux): https://wiki.archlinux.jp/index.php/Desktop_notifications
- osascript (macOS): https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/

# 利用例
- コマンド実行後に自動発動
- `/skills random-os-fake-ancient-prophecy-alert alert` で即時通知
- `list`/`summary`で履歴を確認

# 注意点
- 通知は完全に架空で実用性はありません
- OS通知機能が動作しない場合は標準出力に表示
- 履歴はホームディレクトリの隠しファイルに保存

# 設計方針
- OSごとに最適な通知APIを選択し、環境非依存性を重視
- 毎回異なる預言を生成し、履歴記録・参照も可能に設計