# 概要
本Skillは、開発現場の緊張緩和やアイスブレイクを目的に、完全に架空のバグバウンティ通知をランダム生成・表示します。実際のバグ検出やセキュリティ報告とは無関係で、作業中の気分転換・笑いの提供が主眼です。

# 公式ドキュメント抜粋
- Linux: [notify-send](https://specifications.freedesktop.org/notification-spec/latest/)
- macOS: [osascript display notification](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/reference/ASLR_display.html)

# 利用例
- 長時間の開発作業や集中タイム中に、突如“謎のバグバウンティ”が通知され、チーム内で笑いが生まれる
- コミットやレビュー後の気分転換に明示呼び出し

# 注意点
- 通知内容・報酬は完全ランダムで、実害やデータ損失はありません
- 通知履歴はローカル保存しません
- Windowsではデスクトップ通知は未サポートですが、ターミナル出力は可能です

# 設計方針
- 実在APIのみ利用し、外部サービスやネットワーク通信は行いません
- バグ・報酬リストは拡張容易な構造とし、今後のネタ追加にも柔軟に対応します