---
name: random-os-sudden-boss-key
description: Codexは「上司が近づく」「画面を一時的に隠したい」「作業を誤魔化したい」などのキーワードや明示呼び出し時に、このSkillを発動してください。発動時は現在のウィンドウを隠し、完全ランダムな謎のダミー画面を一瞬表示します。
---

# 機能概要
このSkillは、作業中に突如“謎のボスキー”を発動し、現在アクティブなウィンドウを一時的に隠して、完全ランダム生成のダミー画面（意味不明なグラフ、偽OS警告、ナンセンスな業務風チャート等）を全画面で表示します。通常のボスキーとは異なり、むしろ怪しまれるカオスな演出を提供します。緊張感のある仕事場で、真面目な雰囲気を一瞬で壊したい時に最適です。

# 使い方
- 明示呼び出し: `/skills menu` から `random-os-sudden-boss-key` を選択、または `$random-os-sudden-boss-key` と入力
- 暗黙発動: 「上司が来た」「画面を隠したい」「ボスキー」などのキーワードを含む指示で自動発動

# 出力例
```shell
[INFO] Sudden Boss Key Activated!
[DEBUG] Hiding active window: code.exe (Visual Studio Code)
[DEBUG] Displaying dummy screen: [Fake OS Alert - Error Code 0xDEADBEEF]
[DEBUG] Dummy screen type: Random Nonsense Graph
[INFO] Returning to original window.
```

# 注意点
- ダミー画面は毎回完全ランダム生成
- 10秒以内に自動で元のウィンドウへ復帰
- 一部OSやウィンドウマネージャでは挙動が異なる場合あり
- ダミー画面の内容はローカル保存されません

# 参考資料
- [Python公式: tkinter, matplotlib, pygetwindow](https://docs.python.org/3/library/tkinter.html)
- references/design_notes.md 参照