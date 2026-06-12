---
name: random-os-notification-confetti
description: 作業中やコマンド実行時、または /skills メニューや skill名の明示呼び出し時に、完全ランダムな“祝福”通知をOSの通知領域へ表示します。出社やlsコマンドなど、脈絡のないネタ祝福が突然現れ、気分転換や非日常の演出を提供します。
---

# 機能概要
このSkillは、日々のコマンド操作や作業の合間に、まったく脈絡のない“祝福”メッセージをOSの通知領域（システムトレイ等）にランダム表示します。「本日も出社おめでとう」「意味なく祝福します」「さっきのls、最高でした」など、ユーモラスで非日常的な通知が突然現れ、真面目な作業空間にちょっとした笑いや驚きをもたらします。通知内容は完全ランダムで、繰り返しやパターン化を避ける工夫もあり、気分転換やチームの雰囲気づくりにも役立ちます。

# 使い方
- 明示呼び出し例:
  - `/skills menu` から「random-os-notification-confetti」を選択
  - `$random-os-notification-confetti` で直接実行
- 暗黙発動キーワード例:
  - 「ls」「cd」「git pull」など、よく使うコマンド直後
  - 作業が一定時間継続したタイミング

# 出力例
```
$ ls
（通知領域に表示）
[祝福] さっきのls、最高でした！

$ cd project
（通知領域に表示）
[祝福] 本日も出社おめでとうございます！

$ git commit -m "fix"
（通知領域に表示）
[祝福] 意味なく祝福します！

$ /skills menu
（通知領域に表示）
[祝福] きょうも素晴らしいスキル選択です！
```

# 注意点
- OSの通知API（Windows: win10toast, macOS: osascript, Linux: notify-send）を自動判別し利用します
- 通知頻度は過剰にならないよう調整されていますが、長時間の作業時は意図せず複数回表示される場合があります
- ローカルでのみ動作し、通知内容・履歴は保存されません
- サーバー環境やGUIのない端末では通知が表示されません

# 参考資料
- references/design_notes.md も参照
- [notify-send (Linux)](https://specifications.freedesktop.org/notification-spec/notification-spec-latest.html)
- [win10toast (Windows)](https://github.com/jithurjacob/Windows-10-Toast-Notifications)
- [osascript (macOS)](https://ss64.com/osx/osascript.html)