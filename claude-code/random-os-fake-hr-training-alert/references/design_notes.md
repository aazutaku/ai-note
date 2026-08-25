# 概要
このSkillは、現実には絶対に体験したくない“謎の人事研修”イベントを、OSやターミナル上にランダム通知として演出することを目的としています。実データには一切影響せず、完全にジョーク用途です。

# 公式ドキュメント抜粋
- [Python subprocess](https://docs.python.org/ja/3/library/subprocess.html)
- [plyer通知API](https://plyer.readthedocs.io/en/latest/)
- [win10toast](https://pypi.org/project/win10toast/)

# 利用例
- `/random-os-fake-hr-training-alert alert --count 3` で3回連続通知
- `/random-os-fake-hr-training-alert demo --interval 1.5 --times 5` で1.5秒間隔で5回通知
- 任意コマンドに「研修」「通知」など含む場合、自動でランダム通知

# 注意点
- 通知内容は完全に架空です。現実の人事制度・研修とは一切関係ありません。
- OS通知APIの制約により、通知が表示されない場合はターミナル上に演出されます。
- 履歴やログは一切保存されません。

# 設計方針
- OS依存を最小限にしつつ、`plyer`や`notify-send`、`osascript`など実在APIのみ利用
- ユーザーの実データやファイルには絶対に影響を与えない安全設計
- 通知バリエーションを増やし、毎回違う“カオスな人事研修”体験を提供