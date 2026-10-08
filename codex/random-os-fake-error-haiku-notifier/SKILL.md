---
name: random-os-fake-error-haiku-notifier
description: このSkillは、コマンド実行や作業中に「エラー」「失敗」「バグ」などのキーワードを検知した際や、/skills menu など明示的な呼び出し時に、五・七・五の俳句形式でランダムな“OS風エラーハイク通知”を生成・表示します。
---

# 機能概要
random-os-fake-error-haiku-notifierは、あなたの作業中やCLIコマンドの実行時に、あたかもOSが発するかのようなエラー通知を、五・七・五の俳句形式でランダム生成し、デスクトップ通知やターミナルに表示します。内容は「ファイル消失」「プロセス停止」「404」などの技術ワードと、季語や詩的表現を組み合わせ、思わずクスッとする摩訶不思議な体験を提供します。実用性は皆無ですが、開発者の心に小さな余白と遊び心をもたらします。

# 使い方
- 明示呼び出し例: `/skills menu` から本Skillを選択、または `random-os-fake-error-haiku-notifier` を直接呼び出し
- 暗黙発動: コマンドラインやログに「error」「fail」「not found」「bug」などのキーワードが出現した際に自動発動
- 通知頻度や表示方法は環境変数やCLIオプションで調整可能

# 出力例
```
メモリ消ゆ    春まだ遠き    バグの夜
404          道に迷いて    春霞
プロセス落つ 静けさ満ちて  冬の朝
ファイル消え 風の行方に    秋の雲
アクセス拒否 月のしじまに  眠れず
```

# 注意点
- 本Skillはジョーク用途です。実際のエラーや障害通知には使えません。
- 通知が多すぎる場合は設定で頻度を調整してください。
- ローカル保存やログファイル出力は行いません。
- Linux/macOSの通知API（notify-send, osascript）を利用します。Windowsではターミナル出力のみ対応。

# 参考資料
- [参考: Bash notify-send](https://specifications.freedesktop.org/notification-spec/latest/)
- references/design_notes.md も参照