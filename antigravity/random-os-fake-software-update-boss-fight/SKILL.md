---
name: random-os-fake-software-update-boss-fight
description: 開発現場や作業中に『ソフトウェアアップデート』や『バグ修正』などのキーワードが会話や作業ログに現れた時、Antigravityが自動でRPG風バトル実況の茶番通知を発動します。
---

# 機能概要
このSkillは、OSのソフトウェアアップデート通知を装ったRPG風バトル実況を自動生成し、画面端や通知領域に表示します。進捗バーやメッセージが「アップデート勇者」と「伝説のバグ魔王」の熱い戦いとして描写され、アップデートの進捗やバトル展開が毎回異なります。最終的に“勝利”または“全滅”で締めくくられ、日常の業務にユーモアと非日常感をもたらします。

# 使い方
このSkillは明示的な呼び出しは不要です。会話や作業ログに「アップデート」「バグ修正」「パッチ」「OS更新」などのキーワードが検出された際、自動で発動します。暗黙発動例：
- 「今日のアップデート内容は？」
- 「バグ修正パッチを適用しました」
- 「OSの更新が必要です」

# 出力例
```
[OSアップデート進行中...]
勇者アップデーターがバグ魔王に挑む！
バグ魔王の逆襲！進捗 23%
勇者、パッチの剣を抜く！進捗 47%
バグ魔王、致命的なエラー波を放つ！進捗 68%
勇者、バグ魔王を討伐！進捗 100%
アップデート完了：勇者の勝利！
```

# 注意点
- 本Skillは業務効率化や実際のアップデート管理機能は持ちません。
- 通知や進捗バーはOS標準API（macOS: `osascript`, Windows: `toast`, Linux: `notify-send`）を利用します。
- ローカルに一時的なログを保存しますが、個人情報や機密情報は扱いません。
- 除外パスや特定アプリケーションでは発動しない設定も可能です。

# 参考資料
- [macOS osascript documentation](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/introduction/ASLR_intro.html)
- [Windows Toast Notifications](https://learn.microsoft.com/en-us/windows/uwp/design/shell/tiles-and-notifications/toast-notifications)
- [Linux notify-send manpage](https://man7.org/linux/man-pages/man1/notify-send.1.html)
- references/design_notes.md も参照