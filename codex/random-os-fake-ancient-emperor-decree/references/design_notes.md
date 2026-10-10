# 概要
本Skillは、作業中に突然“OS公式・古代皇帝の勅令”を通知することで、ユーザー体験にユーモアとカオスを加える演出型スキルです。通知内容は完全なフィクションで、実際の作業やシステムに影響を与えません。

# 公式ドキュメント抜粋
- Python subprocess: https://docs.python.org/ja/3/library/subprocess.html
- Linux notify-send: https://specifications.freedesktop.org/notification-spec/latest/
- macOS osascript: https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/introduction/ASLR_intro.html

# 利用例
- チームのアイスブレイクや休憩時間の話題作り
- 長時間作業の合間にランダムな息抜き通知
- ターミナルやデスクトップでの演出イベント

# 注意点
- 通知はOSごとに異なるAPIを利用するため、環境によっては追加パッケージが必要
- 通知内容はジョークであり、実際の操作や権限には一切影響しません

# 設計方針
- シンプルな構成で、どのOSでも動作しやすいよう分岐実装
- 通知内容は威厳と理不尽さを重視したワンライナー形式
- 追加の履歴保存や実害ある処理は一切行わない