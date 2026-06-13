---
name: random-os-soundtrack-notifier
description: ターミナルやエディタの起動時、または /skills コマンドや skill名で明示的に呼び出された際に、完全ランダムな“今日の作業BGM”をOS通知で1回だけ表示します。通知内容やタイミングが毎回異なることが特徴です。
---

# 機能概要
random-os-soundtrack-notifier は、あなたがターミナルやエディタを起動した瞬間や、/skills menu などで明示的に呼び出した時に、“今日の作業BGM”を完全ランダムでOS通知として提案します。BGMは「なつかしのファミコン効果音」「宇宙戦艦発進テーマ」「朝礼のチャイム」など、作業に全く関係ないタイトルばかり。開発現場に無駄な演出を加え、集中力をかき乱すための本気のジョークSkillです。実際のBGM再生や外部API呼び出しは一切行わず、通知のみで完結します。

# 使い方
- 明示的呼び出し例: `/skills random-os-soundtrack-notifier` または `$ random-os-soundtrack-notifier`
- 暗黙発動: 「ターミナル起動」「エディタ起動」「/skills menu」などのイベント時に自動で1回だけ発動
- 通知は1回のみ表示され、連続発動はしません

# 出力例
```terminal
[OS通知] あなたの今日の作業BGM: 宇宙戦艦発進テーマ
[OS通知] あなたの今日の作業BGM: なつかしのファミコン効果音
[OS通知] あなたの今日の作業BGM: 朝礼のチャイム
[OS通知] あなたの今日の作業BGM: 伝説のRPGセーブポイント
[OS通知] あなたの今日の作業BGM: 早朝の商店街BGM
```

# 注意点
- BGMはタイトルのみで、実際の音楽再生やファイル保存はありません
- 毎回ランダムなタイトルが選ばれますが、同じセッション内で重複する可能性もあります
- OS通知機能は Linux (notify-send), macOS (osascript), Windows (win10toast) に対応

# 参考資料
- references/design_notes.md 参照
- OS通知API: https://docs.python.org/ja/3/library/subprocess.html, https://github.com/jithurjacob/Windows-10-Toast-Notifications
- Skill設計方針や通知実装の詳細は references/design_notes.md を参照してください