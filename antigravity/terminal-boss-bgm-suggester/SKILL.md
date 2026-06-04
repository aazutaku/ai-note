---
name: terminal-boss-bgm-suggester
description: Antigravityがユーザーの本日最初のターミナルコマンド実行時に、完全ランダムで“本日のテーマソング”をテキスト通知するSkillです。triggerType: always、semantic-match-onlyで発動し、音声再生や環境変更は行いません。
---

# 機能概要
このSkillは、ターミナルで本日最初のコマンドを実行した瞬間に、“本日のあなたのテーマソング”を完全ランダムで提案します。選曲は『情熱大陸』『エヴァンゲリオン』『サザエさん』『運命』『アンパンマン』など、仕事や日常のテンションを意外な方向へ盛り上げたり、微妙に邪魔したりします。通知はテキストのみで、BGMの再生やシステム設定の変更は一切行いません。職場や自宅での作業開始時に、ちょっとした遊び心や話題のきっかけを提供します。

# 使い方
このSkillは明示的な呼び出しは不要です。Antigravityエージェントがターミナルで最初のコマンドを検知した際、自動的に発動します。triggerTypeはalways、semantic-match-onlyです。暗黙的な発動キーワード例: "最初のコマンド", "本日の作業開始", "terminal session start" など。

# 出力例
```
🎵 Terminal BOSS BGM Suggester
本日のあなたのテーマソング: サザエさん オープニング
(今日も元気にいってらっしゃい！)

🎵 Terminal BOSS BGM Suggester
本日のあなたのテーマソング: 新世紀エヴァンゲリオン 残酷な天使のテーゼ
(仕事モード、発進！)
```

# 注意点
- BGM提案は1日1回、最初のコマンド実行時のみ発動します
- 音声再生や外部サービス連携は行いません
- 選曲は完全ランダムで、ユーザーの好みや状況は考慮しません
- 提案内容はローカルに保存されません
- 職場等での利用は自己責任でお願いします

# 参考資料
本Skillの設計・実装詳細は references/design_notes.md を参照してください。BGMリストやランダム選曲アルゴリズム、トリガー検知ロジックについても記載しています。

- 公式: https://ai-note.tech/skills/terminal-boss-bgm-suggester
- Python random, datetime 標準ライブラリ利用