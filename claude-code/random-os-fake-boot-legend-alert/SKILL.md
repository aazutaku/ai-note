---
name: random-os-fake-boot-legend-alert
description: 作業中やコマンド実行時など、ユーザーの集中が高まるタイミングや、/random-os-fake-boot-legend-alert 明示呼び出し時に発動。伝説級の謎OS起動通知を表示し、場を和ませたり意外性を演出します。
---

# 機能概要
このSkillは、作業中に「伝説のOS起動通知」を完全ランダムな内容で突如表示します。内容は“OS界の選ばれし者”や“謎BIOSの声”など、意味不明かつレジェンド感あふれるメッセージ。通知はデスクトップ(Windows/macOS/Linux)やターミナル上に現れ、実害は一切ありません。日常作業の合間に「何だこれ!?」と一瞬現実を疑わせ、笑いや驚きを提供します。退屈な作業や長時間のコーディングにちょっとした刺激を与え、チームや個人の雰囲気を和らげる小ネタ演出として最適です。

# 使い方
- 明示的な呼び出し: `/random-os-fake-boot-legend-alert` コマンドで即時発動
- 暗黙的な発動: 「起動」「伝説」「OS」「BIOS」「神話」「レジェンド」などのキーワードを含む作業や会話、または一定時間ごとに自動発動
- 設定ファイルで発動間隔や通知方法(デスクトップ/ターミナル)を調整可能

# 出力例
```
[伝説のOS起動通知]
本日、あなたは選ばれしOSユーザーです。
---
BIOS: “古の声が聞こえる...システムは覚醒した”
伝説のブートシーケンスが発動しました。
---
OS神話モード: 有効
```

# 注意点
- 完全なジョーク機能のため、実際のシステムやファイルには一切影響しません
- 通知はローカル環境のみ。リモートやサーバー用途には非推奨
- 長時間の連続発動や大量通知にはご注意ください
- 通知履歴はローカルに保存されません

# 参考資料
- [参考: references/design_notes.md](references/design_notes.md)
- [公式: Python標準通知API](https://docs.python.org/ja/3/library/subprocess.html)
- [notify2 (Linux)](https://pypi.org/project/notify2/), [osascript (macOS)](https://ss64.com/osx/osascript.html), [win10toast (Windows)](https://pypi.org/project/win10toast/)