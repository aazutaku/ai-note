# 概要
このSkillは、日々の作業開始時に「理不尽なBGM通知」というエンタメ体験を提供します。実際に音楽は再生せず、通知のみを表示することで、気軽に導入できる点が特徴です。

# 公式ドキュメント抜粋
- Python subprocess: https://docs.python.org/ja/3/library/subprocess.html
- Linux通知: https://github.com/notify2/notify2
- Windows通知: https://docs.microsoft.com/ja-jp/windows/uwp/design/shell/tiles-and-notifications/

# 利用例
ターミナルやエディタの起動時、または /skills menu から明示呼び出しすることで、毎回異なるBGMタイトルが通知されます。スクリプト単体で `python random_os_soundtrack_notifier.py notify` でも利用可能です。

# 注意点
- OS通知APIの仕様に依存するため、環境によっては追加パッケージ（win10toast等）が必要な場合があります。
- 楽曲リストは随時編集・拡張可能です。
- 通知が出ない場合はOSの通知設定を確認してください。

# 設計方針
「絶対に流れないBGM」という理不尽さと、日常の作業開始にユーモアを添えることを重視しました。