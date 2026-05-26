---
name: boss-key-instant-hide
description: 作業中に“見られたくない画面”を即座に隠したいとき（例: 上司・親が背後に来た、画面を一瞬で切り替えたい等）、boss-key-instant-hide Skillはワンコマンドでエディタやターミナルを隠し、無難なウィンドウや偽装進捗画面を表示します。キーワード: 画面隠す・一発切替・偽装。
---

# 機能概要
boss-key-instant-hide Skillは、作業中に見られたくない画面（エディタ、ターミナル等）をワンコマンドで即座に隠し、天気予報やエクセル風の無難なウィンドウ、または進捗バー付きの偽装画面に切り替えます。開発現場や自宅で“今ここで見られたくない！”という状況を瞬時に回避でき、エンタメ枠ながらも切実な需要に応えます。画面切替はOSのウィンドウ管理APIを利用し、データ損失や実害を防ぎつつ、凝った演出も選択可能です。

# 使い方
明示的には `/skills boss-key-instant-hide` または `@codex boss-key-instant-hide` で発動。暗黙的には「画面を一発で隠したい」「上司が来た」「親フラ対策」「偽装画面」などのキーワードを含む発話でトリガーされます。コマンドラインで `python boss_key_instant_hide.py --mode excel` など、偽装画面タイプを指定可能です。

# 出力例
```
[INFO] 隠蔽対象: code.exe, powershell.exe
[INFO] 画面を非表示にしました
[INFO] 偽装画面: Excel風進捗バーを表示中...
[PROGRESS] [██████      ] 60% 完了
[INFO] 解除は Ctrl+Shift+B です
```

# 注意点
- サポートOSはWindows/macOS/Linux（X11）
- 隠蔽対象ウィンドウは設定可能
- データは自動保存せず、既存アプリの状態は維持
- 一部環境ではウィンドウ検出に制限あり

# 参考資料
- references/design_notes.md を参照
- 公式: https://docs.python.org/ja/3/library/ctypes.html, https://github.com/pywinauto/pywinauto, https://pypi.org/project/pygetwindow/