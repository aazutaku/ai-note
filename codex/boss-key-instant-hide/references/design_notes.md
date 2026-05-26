# 概要
boss-key-instant-hide Skillは、開発者が“見られたくない”作業画面を即座に隠し、無難なウィンドウや進捗バーで偽装するためのユーティリティです。主要な用途は、上司・親・同僚の突然の来訪時のリスク回避です。

# 公式ドキュメント抜粋
- pygetwindow: https://github.com/asweigart/pygetwindow
- tkinter: https://docs.python.org/ja/3/library/tkinter.html
- pywinauto: https://pywinauto.readthedocs.io/

# 利用例
- CLIで `python boss_key_instant_hide.py --mode weather` を実行
- 明示呼び出し `/skills boss-key-instant-hide` で即発動
- 解除は Ctrl+Shift+B で元の画面復帰

# 注意点
- 隠蔽ウィンドウの検出はタイトル名・プロセス名に依存し、カスタマイズ可能
- データ保存は自動で行わず、既存アプリの状態は維持
- 一部Linux環境ではウィンドウ制御に制限あり

# 設計方針
- 実害やデータ損失を防ぐため、ウィンドウは最小化のみ
- 偽装画面はtkinterで軽量実装、解除操作も明示
- 将来的にカスタム偽装画面や自動保存連携も検討