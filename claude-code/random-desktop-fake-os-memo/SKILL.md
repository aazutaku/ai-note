---
name: random-desktop-fake-os-memo
description: 作業中やコーディング時に、完全ランダムな“謎のOSメモ”をデスクトップ通知として発動。通知・演出・OS連携のキーワードが含まれる状況や、/random-desktop-fake-os-memo コマンド実行時に自動で発動します。
---

# 機能概要
このSkillは、作業中のデスクトップに突然“謎のOSメモ”を通知として表示します。内容は完全にランダムで、例えば「冷蔵庫にプリンあり」「上司が見ている」「謎の引き出しを開けるな」など、実用性ゼロの怪文書が炸裂。集中している時ほど思わず二度見してしまう、シュールで遊び心あふれる演出を提供します。退屈なデスクトップにちょっとした混乱と笑いを呼び込み、気分転換や話題作りにも最適です。

# 使い方
- 明示的な呼び出し: `/random-desktop-fake-os-memo` コマンドを実行すると即座に通知が表示されます。
- 暗黙発動: 「通知」「演出」「OS連携」「デスクトップ」「遊び心」などのキーワードを含む会話やトリガー条件下で自動発動します。

# 出力例
```
[デスクトップ通知]
謎のOSメモ: 冷蔵庫にプリンあり

[デスクトップ通知]
謎のOSメモ: 上司が見ている

[デスクトップ通知]
謎のOSメモ: バグは空から降ってくる

[デスクトップ通知]
謎のOSメモ: 謎の引き出しを開けるな

[デスクトップ通知]
謎のOSメモ: システムはあなたを見ている
```

# 注意点
- 通知内容は毎回完全ランダムで再現性がありません。
- 実用性は一切なく、意味不明な内容が多く含まれます。
- 通知はローカル端末でのみ表示され、履歴やファイル保存は行いません。
- Linux/macOSでは`notify-send`/`osascript`、Windowsでは`win10toast`などの標準的な通知APIを利用します。

# 参考資料
- [Linux notify-send](https://specifications.freedesktop.org/notification-spec/latest/)
- [macOS AppleScript通知](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/introduction/ASLR_intro.html)
- [win10toast (PyPI)](https://pypi.org/project/win10toast/)