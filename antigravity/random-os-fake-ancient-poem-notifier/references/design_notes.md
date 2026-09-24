# 概要
本Skillは、開発現場に“知的混乱”とユーモアを届けるため、古文調の詩的通知を完全ランダムで発動するものです。通知内容は実際の作業やエラーと無関係で、集中力のリセットや気分転換を狙っています。

# 公式ドキュメント抜粋
- Pythonの標準subprocessモジュールを用い、Linuxではnotify-send、macOSではosascript、Windowsではwin10toast(API要インストール)を利用。
- 参考: https://docs.python.org/ja/3/library/subprocess.html

# 利用例
- 長時間のコーディング中、突如“OS古代詩通知”が現れ、チーム全体に笑いが起きる。
- ターミナルで `python random_os_fake_ancient_poem_notifier.py daemon --interval 600` のように定期発動。

# 注意点
- 通知は完全に無害で、既存のファイルやシステム設定を変更しません。
- win10toastが未インストールの場合はpipで追加が必要です。
- 履歴はホームディレクトリ直下の隠しログファイルに保存されます。

# 設計方針
- OSごとの通知APIを直接呼び出すことで、追加ライブラリなしでも動作。
- 詩の内容は今後拡張可能なリスト構造。
- ログ機能を持たせ、過去の通知も振り返り可能。