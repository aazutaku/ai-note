---
name: random-os-fake-ancient-poem-notifier
description: 作業中やコマンド入力時など、ユーザーの集中が続くタイミングで、完全ランダムな“古文調・詩体”の謎通知をOSの通知機能やターミナル上に表示します。通知内容は作業内容やエラーと無関係で、知的混乱や笑いを演出します。triggerType: semantic-or-explicit。
---

# 機能概要
このSkillは、現代の開発現場に“古代文学の風”を吹き込むための通知・演出ツールです。作業中やコマンド実行時など、集中が高まる瞬間に、完全ランダムな“OS古代詩通知”をデスクトップやターミナルに表示します。通知内容は「西のコードベースにバグの風そよぐ」「あなたのShiftキー、今宵は静かに眠るべし」など、万葉集や古典文学を模した謎ポエム。作業内容やエラー情報とは一切関係なく、ユーザーの集中力を絶妙にそらし、知的混乱と笑いをもたらします。

# 使い方
- 明示呼び出し例：`python random_poem_notifier.py notify` または Skillメニューから直接発動
- 暗黙発動キーワード例：`/skills menu` や `$random-os-fake-ancient-poem-notifier` へのメンション
- CLIサブコマンドで`list`（詩リスト表示）、`summary`（発動履歴要約）も利用可能

# 出力例
```
[OS Poem Notification]
東のメモリ、静かに溢れぬ
バグの風、夜半にささやく
あなたのShiftキー、今宵は眠るべし

[OS Poem Notification]
西のコードベースに、霧立ちこめる
エラーの影、そっと忍び寄る

[OS Poem Notification]
デバッグの灯、朝焼けに消えて
古の関数、夢に現る
```

# 注意点
- 通知内容は完全にランダム生成され、実際のシステム状況や作業内容とは無関係です。
- ローカルに通知履歴を保存しますが、個人情報やコード内容は記録しません。
- 通知はOSの標準通知API（Windows: Toast, macOS: AppleScript, Linux: notify-send）を利用します。
- 本Skillは実際のエラー通知やシステム警告とは無関係です。

# 参考資料
- references/design_notes.md
- [notify2公式ドキュメント](https://github.com/caronc/apprise)
- [AppleScript通知参考](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/introduction/ASLR_intro.html)
- [Pythonサブコマンド実装例](https://docs.python.org/ja/3/library/argparse.html)