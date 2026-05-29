# 概要
このSkillは、作業中のユーザーに対して“無意味な緊張度”をデスクトップに通知し、作業環境にユーモラスな緊張感を演出することを目的としています。実用性よりも遊び心や職場の雰囲気づくりに重きを置いています。

# 公式ドキュメント抜粋
- [Python tkinter](https://docs.python.org/3/library/tkinter.html): クロスプラットフォームなGUI通知用
- [notify-send (Linux)](https://specifications.freedesktop.org/notification-spec/latest/): Linuxデスクトップ通知
- [osascript (macOS)](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/introduction/ASLR_intro.html): macOS通知
- [win10toast (Windows)](https://pypi.org/project/win10toast/): Windows通知

# 利用例
- チームの休憩時間に“謎の緊張度”を表示し、話題作りやアイスブレイクに
- リモートワーク時の気分転換や集中力リマインダーとして

# 注意点
- 実際の緊張度やストレスを測定するものではありません。
- 通知頻度や内容はスクリプト設定で調整可能です。
- ログはユーザーのホームディレクトリに保存されます。

# 設計方針
- 主要OS（Windows/macOS/Linux）で動作するよう通知APIを分岐実装
- commit数やタイピング速度は“それっぽさ”重視でランダム補正
- 強制終了してもデータ損失や副作用がない設計