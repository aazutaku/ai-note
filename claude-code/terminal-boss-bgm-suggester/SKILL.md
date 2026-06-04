---
name: terminal-boss-bgm-suggester
description: 最初のターミナルコマンド実行時に、完全ランダムで“本日のあなたのテーマソング”をテキスト通知として提案します。発動条件は「その日最初のコマンド」または明示呼び出し（/terminal-boss-bgm-suggester）です。
---

# 機能概要
terminal-boss-bgm-suggesterは、ターミナルでその日最初のコマンドを実行した瞬間、あなたに“本日のテーマソング”を完全ランダムでテキスト通知します。『情熱大陸』『エヴァンゲリオン』『サザエさん』など、仕事や作業のテンションを盛り上げたり、逆に微妙に邪魔したりする選曲で、日々の開発にちょっとした演出を加えます。音は流さず、環境を壊すことなく、通知のみで気分転換や話題作りに役立ちます。

# 使い方
- 明示呼び出し: `/terminal-boss-bgm-suggester` を実行すると即座にテーマソングが提案されます。
- 暗黙発動: その日の最初のターミナルコマンド実行時に自動で発動します（内部でコマンド履歴・日付を判定）。

# 出力例
```
🎵 Terminal Boss BGM Suggestion 🎵
本日のあなたのテーマソングは…『情熱大陸』です！
（YouTube: https://www.youtube.com/watch?v=example1）
今日も一日、情熱的に頑張りましょう！
```
```
🎵 Terminal Boss BGM Suggestion 🎵
本日のあなたのテーマソングは…『サザエさん』です！
（YouTube: https://www.youtube.com/watch?v=example2）
肩の力を抜いて、楽しく作業しましょう。
```

# 注意点
- 選曲は完全ランダムで、同じ曲が続く場合もあります。
- 音は自動再生されません。YouTube等のリンクのみ通知されます。
- コマンド履歴はローカルのみに保存され、外部送信はありません。
- 職場や公共の場での利用は自己責任でお願いします。

# 参考資料
詳細な設計方針や参考情報は references/design_notes.md を参照してください。YouTube API 公式ドキュメント: https://developers.google.com/youtube/v3