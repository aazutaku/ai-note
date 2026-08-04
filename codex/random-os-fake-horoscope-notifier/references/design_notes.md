# 概要
本Skillは、開発者の作業開始時や明示的な呼び出し時に、完全ランダムな“OS星占い”を1日1回だけ通知することで、日々のコーディングに遊び心とリフレッシュ効果を加えることを目的としています。

# 公式ドキュメント抜粋
- Python randomモジュール: https://docs.python.org/ja/3/library/random.html
- notify-send (Linux): https://wiki.archlinux.jp/index.php/Desktop_notifications
- osascript (macOS): https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/introduction/ASLR_intro.html

# 利用例
- ターミナルで `python os_horoscope_notifier.py notify` を実行すると、その日の“OS星占い”が表示されます。
- `--desktop` オプションでデスクトップ通知も可能。
- 1日1回のみ通知され、履歴はホームディレクトリの`.os_horoscope_notifier_history.json`に保存されます。

# 注意点
- 通知内容は完全なランダム生成で、実際の運勢や作業効率には一切影響しません。
- デスクトップ通知はLinux/macOSのみ対応。Windowsではターミナル表示のみ。
- 個人情報や作業内容の外部送信はありません。

# 設計方針
- シンプルなローカルJSONファイルによる履歴管理で、1日1回制限を実現。
- ユーザー体験を損なわないよう、通知の強制・過剰表示は排除。
- CLIサブコマンドで拡張性を確保し、今後のカスタマイズにも対応可能としています。