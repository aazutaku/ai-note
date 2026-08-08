---
name: random-os-fake-screenshot-alert
description: このSkillは、Claude Codeでコマンド実行時や作業の節目（例: ビルド、テスト、デバッグ開始/終了）などのキーワード検出時、または明示的な /random-os-fake-screenshot-alert 呼び出し時に発動します。通知内容は毎回ランダムで、実際には何も保存されません。
---

# 機能概要
このSkillは、作業中やコマンド実行時に「謎のOS偽スクリーンショット保存通知」をデスクトップに表示します。通知内容は毎回ランダムで「スクリーンショット保存済み：バグ発生の瞬間」「証拠画像を保存しました」「あなたの集中顔を記録しました」など、意味不明かつ混沌としたメッセージが飛び出します。実際には何も保存されず、現場の緊張感やマンネリを一撃粉砕するジョーク枠Skillです。

# 使い方
- 明示呼び出し: `/random-os-fake-screenshot-alert`
- 暗黙発動: `ビルド開始`, `デバッグ`, `run`, `test`, `compile`, `実行`, `エラー`, `バグ`, `証拠`, `保存`, `スクリーンショット` などのキーワードを含むコマンドや会話時に自動発動します。

# 出力例
```terminal
[通知] スクリーンショット保存済み：バグ発生の瞬間
[通知] 証拠画像を保存しました
[通知] あなたの集中顔を記録しました
[通知] 画面全体の謎画像を保存しました
[通知] 何もしていませんが保存しました
```

# 注意点
- 実際には何も保存されません（ファイル出力・画像生成なし）
- 通知内容は毎回ランダムです
- 頻度やタイミングは迷惑にならないよう調整されています
- ローカルの通知API（notify-send, win10toast等）を利用しますが、環境によっては表示されない場合があります

# 参考資料
- [references/design_notes.md](references/design_notes.md)
- [Python公式: notifications](https://docs.python.org/ja/3/library/subprocess.html)
- [notify-send (Linux)](https://specifications.freedesktop.org/notification-spec/notification-spec-latest.html)
- [win10toast (Windows)](https://pypi.org/project/win10toast/)