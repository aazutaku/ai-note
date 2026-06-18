# 概要
random-os-error-kaisekiは、コマンド実行時のエラー発生時に、実際のエラー内容とは無関係な“OS風カタカナ造語”による謎解説をデスクトップ通知として表示するジョークSkillです。開発現場でのストレス解消や、エラー時の雰囲気緩和を目的としています。

# 公式ドキュメント抜粋
- [Python subprocess](https://docs.python.org/ja/3/library/subprocess.html)
- [notify-send (Linux)](https://specifications.freedesktop.org/notification-spec/latest/)
- [osascript (macOS)](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/introduction/ASLR_intro.html)

# 利用例
- バッチ処理やCI/CDパイプラインでエラー発生時に自動通知
- チームのペアプロやデバッグセッションでのリフレッシュ用

# 注意点
- 通知はローカルデスクトップでのみ表示され、SSHやヘッドレス環境では無効です。
- Windowsはwin10toastライブラリが必要です。

# 設計方針
- 技術的な意味を持たないカタカナ造語を毎回ランダム生成
- 本来のエラー内容は標準出力・標準エラーにそのまま出力
- 拡張性を考慮し、カタカナ語リストは編集可能