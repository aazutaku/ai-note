---
name: random-os-fake-ancient-emoji-scroll-notifier
description: このSkillは、Antigravityがユーザーの作業中やコマンド実行の合間に、"古文調＋現代顔文字や記号"のシュールな巻物風通知をターミナルやデスクトップに自動挿入したい場合に発動します。通知・演出・余白・気分転換・謎演出などのキーワードや、セマンティックマッチで適用されます。
---

# 機能概要
`random-os-fake-ancient-emoji-scroll-notifier`は、作業の合間やコマンド実行後に、突如として“謎のOS古代絵文字巻物通知”をターミナルやデスクトップに出現させるエンタメ系Skillです。東洋古文調と現代顔文字・記号が混在する意味不明なメッセージを、毎回ランダムに生成・表示。真面目な作業空間に一瞬でシュールな違和感をもたらし、脳をリフレッシュさせます。通知・演出・気分転換・余白の演出に最適です。

# 使い方
本Skillは明示的な呼び出しは不要です。Antigravityが「通知」「演出」「気分転換」「OS連携」「余白」などのキーワードや、作業の合間を検知した際に自動発動します。設定によりターミナル出力・デスクトップ通知（macOS/Linuxの`notify-send`/`osascript`）を選択可能。

# 出力例
```
┏━━━━━━━━━━━━━━━━━━━━━━━┓
┃ 東のコード谷にバグの風が吹く…… (´・ω・`)
┃ されど、printfの術は未だ極まらず。
┃ 西の彼方より、警告の鐘が鳴り響く。
┃ ── 2024年 水無月の刻
┗━━━━━━━━━━━━━━━━━━━━━━━┛

┏━━━━━━━━━━━━━━━━━━━━━━━┓
┃ いにしえのcommit、今も尚リベースされず。
┃ (ノ∀`) 　バグは静かに忍び寄る。
┃ #TODO: 夢の如し。
┗━━━━━━━━━━━━━━━━━━━━━━━┛
```

# 注意点
- 本Skillはエンタメ目的です。業務用途や重要な通知には使用しないでください。
- ローカル通知は`notify-send`(Linux)や`osascript`(macOS)に依存します。未対応環境ではターミナル出力のみ。
- 通知内容は完全ランダム生成のため意味不明な場合があります。

# 参考資料
- [notify-send(1) - Linux manual page](https://man7.org/linux/man-pages/man1/notify-send.1.html)
- [osascript - macOS Scriptable Notifications](https://ss64.com/osx/osascript.html)
- references/design_notes.md 参照