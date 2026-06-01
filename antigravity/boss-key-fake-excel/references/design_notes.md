# 概要
boss-key-fake-excelは、作業画面を即座に“Excel風”のフェイクウィンドウで覆い隠すことで、緊急時の“ごまかし”や開発者同士の遊び心をサポートします。

# 公式ドキュメント抜粋
- [PySimpleGUI](https://pysimplegui.readthedocs.io/en/latest/): GUIウィンドウ表示
- [Pillow](https://pillow.readthedocs.io/en/stable/): 画像生成
- [pygetwindow](https://github.com/asweigart/pygetwindow): ウィンドウ制御
- [keyboard](https://github.com/boppreh/keyboard): グローバルショートカット監視

# 利用例
リモートワーク中に“Ctrl+Shift+E”を押すと、即座にExcel風ウィンドウが前面表示され、元の作業を隠せます。Escキーや再度ショートカットで元の画面に戻れます。

# 注意点
- 実際のExcel機能はありません。あくまで“見た目”のみです。
- 一部のOSや仮想環境ではウィンドウ制御が制限される場合があります。
- 必要なPythonパッケージのインストールが必要です。

# 設計方針
シンプルな依存関係で、ローカルPC上で即時動作することを重視。画像生成による“なんちゃってExcel”表現にこだわり、ショートカットやウィンドウ復帰もスムーズに設計しています。