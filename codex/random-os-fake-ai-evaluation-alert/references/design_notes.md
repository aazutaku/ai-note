# 概要
本Skillは、作業中に理不尽かつユーモラスな“AI評価通知”をランダムに生成し、デスクトップやターミナルへ表示することで、作業空間に遊び心を提供します。実用性よりも演出・風刺が主目的です。

# 公式ドキュメント抜粋
- [Python subprocess](https://docs.python.org/3/library/subprocess.html): OSコマンド呼び出しに使用
- [notify-send](https://manpages.ubuntu.com/manpages/latest/man1/notify-send.1.html): Linuxのデスクトップ通知
- [osascript](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/introduction/ASLR_intro.html): macOSの通知
- [win10toast](https://pypi.org/project/win10toast/): Windows 10通知

# 利用例
- `/skills random-os-fake-ai-evaluation-alert alert --terminal` で即時通知
- `/skills random-os-fake-ai-evaluation-alert stream --count 5 --interval 120` で2分ごとに5回通知

# 注意点
- 実際の評価や監視は一切行いません
- 通知頻度は最低60秒間隔に制限し、ウザすぎない設計
- ログ保存は任意で明示指定時のみ

# 設計方針
- 完全に無害であることを最優先
- OSごとの通知APIを実装し、クロスプラットフォーム対応
- メッセージは現実のAI社会の風刺・ユーモアを意識して多数用意
