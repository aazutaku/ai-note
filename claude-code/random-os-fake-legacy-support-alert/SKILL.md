---
name: random-os-fake-legacy-support-alert
description: このSkillは、Claude Codeでコマンド実行やエディタ操作時など、セマンティックまたは明示的に発動条件（例: terminal, run, build, save, /random-os-fake-legacy-support-alert）に該当した際に、レガシーOSサポート終了のユーモラスな通知をランダムに表示します。
---

# 機能概要
random-os-fake-legacy-support-alertは、コマンド実行やファイル保存などの操作時に、現代では考えられないレガシーOSやAPIの“サポート終了通知”を完全ランダムでデスクトップに表示します。例えば「Windows 98互換モードのサポートが本日終了」「IE6向け最適化は永遠に封印されました」など、開発者の心に一瞬の懐かしさと無意味な焦燥をもたらします。実際の環境やデータには一切影響を与えず、遊び心ある通知演出を提供します。

# 使い方
- 明示呼び出し例: `/random-os-fake-legacy-support-alert` を実行
- 暗黙発動: ターミナルで`run`, `build`, `save`, `compile`, `test`等の操作時に自動発火
- 通知はOSの標準通知API（Windows: Toast, macOS: AppleScript, Linux: notify-send）を利用し、内容は毎回ランダム生成されます。

# 出力例
```
[通知] 98互換モードのサポートが本日終了しました。
[通知] IE6向け最適化は永遠に封印されました。
[通知] フロッピー対応APIが旅立ちました。
[通知] Windows MEのリモートデスクトップ機能は伝説となりました。
[通知] OS/2 Warp対応プリンタドライバの提供が終了しました。
[通知] Netscape Navigator 4用CSS互換レイヤーが削除されました。
```

# 注意点
- 実際のOSやシステム設定には一切影響を与えません。
- 通知内容は完全に架空であり、ジョーク用途です。
- 通知履歴はローカル保存されません。
- 一部Linux環境では`notify-send`コマンドが必要です。

# 参考資料
- references/design_notes.md を参照
- OS通知API公式: [Windows Toast](https://learn.microsoft.com/en-us/windows/uwp/design/shell/tiles-and-notifications/), [AppleScript通知](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/introduction/ASLR_intro.html), [notify-send](https://specifications.freedesktop.org/notification-spec/notification-spec-latest.html)