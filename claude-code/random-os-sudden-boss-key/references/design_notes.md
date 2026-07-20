# 概要
このSkillは、作業中の画面を一時的に完全ランダムなダミー画面へ切り替える「ボスキー」演出をPythonで実現します。TkinterによるGUI表示とmatplotlibによるグラフ生成を組み合わせ、毎回異なる内容を即座に表示します。

# 公式ドキュメント抜粋
- Tkinter: https://docs.python.org/ja/3/library/tkinter.html
- matplotlib: https://matplotlib.org/stable/users/index.html
- Pillow: https://pillow.readthedocs.io/en/stable/

# 利用例
- 明示的に`/random-os-sudden-boss-key`を実行
- CLIから`python random_boss_key.py --mode auto`で実行
- "画面を隠したい"などの発話で自動発動

# 注意点
- 本Skillはジョーク・演出用途です。実際の業務用途やセキュリティ対策には不向きです。
- 画面切替は一時的で、内容は保存されません。
- 環境によってはウィンドウが最前面に来ない場合があります。

# 設計方針
- Python標準GUI(Tkinter)を利用し、追加インストール不要で動作する設計
- ダミー内容は毎回乱数で生成し、常に新鮮な演出を保証
- CLIオプションで警告画面/グラフ画面を選択可能
