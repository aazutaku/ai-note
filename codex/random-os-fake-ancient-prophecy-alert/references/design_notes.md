# 概要
本Skillは、開発現場に“古代OS預言”というユーモアを即時注入するための通知演出ツールです。通知内容は毎回ランダム生成され、ターミナル・デスクトップ両対応。副作用ゼロで安全です。

# 公式ドキュメント抜粋
- Python標準random: https://docs.python.org/ja/3/library/random.html
- notify-send (Linux): https://specifications.freedesktop.org/notification-spec/latest/
- osascript (macOS): https://ss64.com/osx/osascript.html
- win10toast (Windows): https://pypi.org/project/win10toast/

# 利用例
- `/skills random-os-fake-ancient-prophecy-alert` で即時発動
- `python prophecy_alert.py run --interval 300 --desktop` で5分ごとに通知

# 注意点
- データ損失や副作用は一切ありません
- 通知頻度・回数はCLI引数で柔軟に調整可能

# 設計方針
- どのOS環境でも動作するよう通知APIを分岐実装
- 予言テンプレートは拡張容易なリスト構造
- 明示/暗黙トリガー両対応で多様な現場に適応