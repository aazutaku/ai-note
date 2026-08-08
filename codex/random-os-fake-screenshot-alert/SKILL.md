---
name: random-os-fake-screenshot-alert
description: このSkillは、コマンド実行や作業中に「スクリーンショット保存通知」をOSの通知API経由でランダム表示します。trigger: screenshot, save, 証拠, バグ, alert, 集中, などのキーワードや明示呼び出し時に発動します。
---

# 機能概要
このSkillは、作業やコマンド実行の合間に、まるでOSが勝手に“謎のスクリーンショット”を保存したかのような通知をデスクトップに表示します。通知内容は毎回ランダムで、「証拠画像を保存しました」「バグ発生の瞬間を記録」「あなたの集中顔を記録しました」など、実際には何も保存されず、意味不明な演出が現場に混沌とした笑いと緊張感をもたらします。マンネリ打破や休憩のきっかけ、場の空気を和ませるジョーク枠として最適です。

# 使い方
- 明示呼び出し例: `/skills random-os-fake-screenshot-alert` や `$random-os-fake-screenshot-alert` をチャットやCLIで実行
- 暗黙発動キーワード例: 「screenshot」「証拠」「バグ」「alert」「集中」などを含むコマンドや会話時に自動発動
- 通知はOSのネイティブ通知API（Windows: Toast, macOS: osascript, Linux: notify-send）を利用

# 出力例
```
[通知] スクリーンショット保存済み：バグ発生の瞬間
[通知] 証拠画像を保存しました（保存先：？？？）
[通知] あなたの集中顔を記録しました
[通知] システムが謎の瞬間をキャプチャしました
[通知] 何もしていませんが保存完了です
```

# 注意点
- 実際に画像やファイルは一切保存されません
- 通知内容は毎回ランダム生成され、同じメッセージはほぼ出ません
- 通知頻度やタイミングは迷惑にならないよう制御されています
- 一部の環境（WSL, SSH, headless等）では通知が表示されない場合があります

# 参考資料
- [Python公式: plyer, notify2, win10toast](https://pypi.org/project/plyer/), [osascript通知](https://ss64.com/osx/osascript.html)
- references/design_notes.md も参照