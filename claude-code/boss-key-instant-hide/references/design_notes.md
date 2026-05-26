# 概要
boss-key-instant-hide は、作業中のエディタやターミナル画面を一発で隠し、無難な偽装画面（Excel風・天気予報風・空白画面）を全画面表示することで、突発的な監視や来客時に作業内容をカモフラージュします。進捗バー表示や解除ホットキーも実装し、実用性と遊び心を両立しています。

# 公式ドキュメント抜粋
- pygetwindow: https://github.com/asweigart/pygetwindow
- pyautogui: https://pyautogui.readthedocs.io/en/latest/
- tkinter: https://docs.python.org/ja/3/library/tkinter.html
- psutil: https://psutil.readthedocs.io/

# 利用例
- 開発現場で「親・上司が来た！」とき、`/boss-key-instant-hide --style excel --progress 80` で即座に偽装
- コマンド一発で全作業ウィンドウを安全に最小化し、解除は Ctrl+Shift+Q で可能

# 注意点
- ウィンドウの検出はタイトル名ベースのため、カスタムエディタや特殊なターミナルは検出できない場合あり
- Wayland環境や一部Linuxデスクトップでは最小化APIが制限されることがある

# 設計方針
- 主要なデスクトップ環境での安全なウィンドウ操作を最優先
- 偽装画面はTkinterでローカル描画し、外部通信やログ送信は一切行わない
- 万一の強制終了時も、作業ウィンドウの状態は維持