# 概要
このSkillは、開発現場のコミット作業にユーモアと偶発性をもたらすために設計されました。commit時に毎回異なるタロット風メッセージを表示し、作業の合間にちょっとした話題や気分転換を提供します。

# 公式ドキュメント抜粋
- Git公式: https://git-scm.com/doc
- notify-send (Linux): https://specifications.freedesktop.org/notification-spec/latest/
- osascript (macOS): https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/

# 利用例
- チーム開発でcommit時の話題作りに
- 個人開発のモチベーション維持や気分転換に
- コミット履歴に沿った占いログの振り返り

# 注意点
- 通知内容は完全にランダムで、実際の運勢やコード内容には一切関係しません。
- デスクトップ通知はLinux/macOSのみ対応。Windowsではターミナル出力のみ。
- ログはホームディレクトリの .commit_fortune_tarot.log に保存されます。

# 設計方針
- シンプルな設計で、GitフックやCI/CDパイプラインにも容易に組み込める
- ローカル環境で完結し、外部通信や個人情報の送信は行わない
- ユーザーの作業を阻害しないよう、通知は短文・即時性重視