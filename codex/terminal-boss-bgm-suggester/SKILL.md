---
name: terminal-boss-bgm-suggester
description: 最初のターミナルコマンド実行時、または /skills メニューや terminal-boss-bgm-suggester の明示呼び出し時に発動。選曲は完全ランダムで、BGM提案はテキスト通知のみ行います。
---

# 機能概要
terminal-boss-bgm-suggester は、今日最初のターミナルコマンドを実行した瞬間に、あなたの“本日のテーマソング”を完全ランダムで提案するスキルです。『情熱大陸』『エヴァンゲリオン』『サザエさん』など、仕事のテンションを一気に変えるBGMが、テキスト通知であなたを無言で盛り上げます。真面目な朝に『運命』、夜に『アンパンマン』など、意外性のある選曲が日々の作業を彩ります。

# 使い方
- 明示呼び出し: `/skills menu` から terminal-boss-bgm-suggester を選択、または `$terminal-boss-bgm-suggester` を入力
- 暗黙発動: ターミナルでその日最初のコマンドを実行した時に自動発動

# 出力例
```terminal
=== Terminal Boss BGM Suggester ===
本日のあなたのテーマソングは…
『サザエさんのテーマ』です！
今日も一日、波平のように落ち着いて頑張りましょう。
(参考: https://www.youtube.com/watch?v=xxxxxxx)
```

# 注意点
- BGMはテキスト通知のみで、音楽再生や端末の設定変更は行いません。
- 1日1回のみ発動。複数ターミナルを開いても同日は再通知しません。
- 選曲は完全ランダムで、選曲リストはスクリプト内で管理されています。
- 職場等での利用は周囲の雰囲気に配慮してください。

# 参考資料
- references/design_notes.md を参照
- 公式: https://ai-note.tech/skills/terminal-boss-bgm-suggester
