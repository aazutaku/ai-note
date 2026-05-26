---
name: boss-key-instant-hide
description: 作業中に『見られたくない画面』を即座に隠したい状況（上司・親の接近、監視の気配、緊急回避など）で発動。hide/隠す/見られたくない/一発/ボスキー/進捗バー/偽装画面 などのキーワードで発動を推奨。
---

# 機能概要
boss-key-instant-hide は、作業中に見られたくない画面（エディタ・ターミナル等）を一発で隠し、無難な偽装画面（天気予報・エクセル風・進捗バー付き等）を即座に表示するスキルです。突発的な監視や来客時に、データ損失なく安全に画面を切り替え、作業の痕跡をカモフラージュします。実用性とエンタメ性を両立し、開発現場の「今ここで見られたくない！」を解決します。

# 使い方
- 明示呼び出し例: `/boss-key-instant-hide --style excel --progress 72`
- 暗黙発動キーワード例: 「ボスキー」「一発で隠す」「進捗バー」「偽装画面」「hide now」「親が来た」などを含む指示文
- オプション: `--style [excel|weather|blank]` で偽装画面を選択、`--progress [0-100]` で進捗バー表示率を指定

# 出力例
```
[INFO] 隠したウィンドウ: code.exe, terminal.exe
[INFO] 偽装画面 (Excel風) を表示中...
[PROGRESS] 進捗: [██████████░░░░░░░░░░] 72%
[INFO] 解除は Ctrl+Shift+Q で可能
```

# 注意点
- 対応OS: Windows/macOS/Linux (主要デスクトップ環境)
- 偽装画面はローカルでのみ表示、ネットワーク送信なし
- 強制終了時も元の作業ウィンドウは維持（自動保存なし）
- 一部ウィンドウマネージャ/Wayland環境では動作制限あり

# 参考資料
- references/design_notes.md に設計方針・利用例を記載
- 公式API: pygetwindow, pyautogui, tkinter, psutil
- https://pyautogui.readthedocs.io/en/latest/
- https://github.com/asweigart/pygetwindow
