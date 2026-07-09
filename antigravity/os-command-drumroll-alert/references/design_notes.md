# 概要
os-command-drumroll-alertは、エンジニアが重大なコマンド（git push, rm, npm publish等）を実行する直前に、ドラムロール音とOS通知で演出を加えるSkillです。操作ミスや事故を抑止しつつ、日常作業に遊び心を提供します。

# 公式ドキュメント抜粋
- [Python subprocess](https://docs.python.org/3/library/subprocess.html)
- [plyer notification](https://plyer.readthedocs.io/en/latest/)
- [notify-send (Linux)](https://specifications.freedesktop.org/notification-spec/)
- [osascript (macOS)](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/introduction/ASLR_intro.html)

# 利用例
- git pushやrm -rfなどの前に、緊張感を演出し注意喚起
- チーム内での運用で、誤操作防止やジョークとして活用

# 注意点
- サウンド再生や通知表示はOS依存。Linuxはmpg123/notify-send、macOSはafplay/osascript、Windowsはpowershellに依存
- サウンドファイルは一時保存されますが、定期的なクリーニングを推奨
- 重大コマンド検出は単純なキーワード一致のため、カスタマイズが必要な場合はTRIGGER_KEYWORDSを編集してください

# 設計方針
- コマンド実行の邪魔になりすぎないよう、演出は5秒以内に収める
- サウンド・通知パターンはランダム化し、繰り返しの作業でも飽きない工夫
- CLIラッパー形式で、既存のワークフローに容易に組み込める設計