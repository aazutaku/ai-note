# 概要
boss-key-fake-excelは、業務中の“見られたくない”作業を即座にカモフラージュするためのフェイクExcel画面表示ツールです。PythonとPySimpleGUI、pygetwindow、keyboardを活用し、ショートカット操作で素早く画面を切り替えられます。

# 公式ドキュメント抜粋
- [PySimpleGUI公式](https://pysimplegui.readthedocs.io/en/latest/): クロスプラットフォームなGUI構築ライブラリ。
- [pygetwindow](https://github.com/asweigart/pygetwindow): ウィンドウの取得・制御。
- [keyboard](https://github.com/boppreh/keyboard): グローバルホットキー検知。

# 利用例
- 開発者が趣味コードやSNSを隠したい時
- 上司や同僚が突然近づいた際の“逃げ”として
- チーム内のちょっとしたイタズラや演出

# 注意点
- 本SkillはローカルPC上でのみ動作し、リモートデスクトップや一部Linux環境では制限あり
- フェイク画面は静的で、本物のExcel機能はありません

# 設計方針
- ショートカット常駐と明示呼び出しの両対応
- 元の作業画面復帰を重視し、ウィンドウ最小化/復元を組み合わせ
- 依存ライブラリはpipで簡単に導入可能なもののみ