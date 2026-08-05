---
name: random-os-fake-ai-takeover-alert
description: ターミナルやエディタで作業中、または/skillsコマンド実行時に、AIによるOS制御ジャックを模した警告通知をOS標準のデスクトップ通知でランダムに表示します。発動条件は「AI」「OS」「警告」「制御」などのキーワード検出時、または明示的な呼び出し時です。
---

# 機能概要
このSkillは、普段の開発作業やコーディング中に、AIがOSを乗っ取ったかのようなフェイク警告を、OS標準のデスクトップ通知としてランダムなタイミング・内容で表示します。通知メッセージは毎回異なり、「AIがカーネル領域を再編成」「AI委員会による再起動審議」など、現実にはありえないユーモラスな内容です。作業現場に突然“AIによる人類ピンチ感”を演出し、チーム内の話題作りやリフレッシュ、ちょっとしたドッキリ用途にも最適です。

# 使い方
- 明示呼び出し: `/skills random-os-fake-ai-takeover-alert` またはメニューから選択
- 暗黙発動: 「AI」「OS」「警告」「制御」などのキーワードを含む会話やコマンド実行時に自動発動
- オプション: `--interval`で通知間隔を秒単位で指定可能 (例: `python fake_ai_alert.py --interval 300`)

# 出力例
```
[通知] 重要：AIがOS制御権を主張中
[通知] カーネル領域がAIにより再編成されました
[通知] AI委員会による再起動審議開始
[通知] AIプロトコルがシステム設定を上書きしました
[通知] 注意：AIが管理者権限を要求しています
```

# 注意点
- 本Skillは実際のシステム制御やファイル操作は一切行いません
- 通知はローカルPCの通知API (Windows: Toast, macOS: AppleScript, Linux: notify-send) を利用
- 作業妨害を避けるため、通知間隔や最大表示回数を調整可能
- ログや履歴はデフォルトで保存されません

# 参考資料
- [Python公式: plyer.notification](https://plyer.readthedocs.io/en/latest/#plyer.notification)
- references/design_notes.md 参照
