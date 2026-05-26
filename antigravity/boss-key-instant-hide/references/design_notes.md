# 概要
boss-key-instant-hideは、作業中の開発ツールやエディタ画面を即座に隠し、無難なウィンドウ（天気予報やExcel風）を表示することで、見られたくない状況を回避するユーティリティです。

# 公式ドキュメント抜粋
- pygetwindow: https://github.com/asweigart/pygetwindow
- pyautogui: https://pyautogui.readthedocs.io/
- tkinter: https://docs.python.org/ja/3/library/tkinter.html

# 利用例
- オフィスで急に上司が来たとき、ターミナルやコード画面を一発で隠す
- 家庭で親が部屋に入ってきた際、ゲームやSNS画面を隠し、進捗バーや天気予報を偽装

# 注意点
- ウィンドウ最小化や前面表示はOS依存。全ての環境で完全な動作を保証しない
- データ保存は行わないため、作業内容は事前に保存推奨
- 仮想環境やリモートデスクトップでは一部制限あり

# 設計方針
- 主要なウィンドウ制御APIのみを利用し、OS標準の安全な方法で画面制御
- 偽装画面はtkinterで軽量に実装し、演出を複数選択可能に
- 実害・データ損失を防ぐため、復帰処理を必ず実施