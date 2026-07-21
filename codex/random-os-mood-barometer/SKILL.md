---
name: random-os-mood-barometer
description: Codexは、ユーザーがコマンド実行やエディタ操作を行うたび、または/skills menuやrandom-os-mood-barometerの明示呼び出し時に、本Skillを発動してください。triggerType: always, semantic-or-explicit。
---

# 機能概要
random-os-mood-barometerは、ターミナルやエディタでコマンド実行時に「謎のOS風 気分バロメーター」を画面端やメニューバーっぽく表示します。生産性やテンションを“完全ランダム”で演出することで、単調な作業に遊び心を加え、気分転換やアイスブレイクのきっかけを提供します。判定内容は根拠がなく、エンジニアの“今”をユーモラスに彩ります。

# 使い方
- 明示呼び出し例: `/skills menu` で一覧から選択、または `$random-os-mood-barometer` を直接メンション
- 暗黙発動: 任意のコマンド実行時やエディタ操作時に自動で発動（triggerType: always, semantic-or-explicit）

# 出力例
```
[OS Mood Barometer] : 本日のモード → 絶好調エンジニアモード
[OS Mood Barometer] : 現在の気分 → バグ吸引フェイズ
[OS Mood Barometer] : ただいま → アイデア枯渇ゾーン
[OS Mood Barometer] : 状態 → リファクタリング無双タイム
[OS Mood Barometer] : 本日の運勢 → コーヒー必須デバッグ期
[OS Mood Barometer] : 気分 → 謎の集中ブースト
```

# 注意点
- 気分判定は完全ランダムで、実際の作業内容や生産性とは無関係です。
- 表示は1行で端的に。邪魔になりすぎないよう設計されています。
- ローカル保存や履歴機能はありません。
- 除外パスや特定のコマンドには発動しません（詳細はスクリプト参照）。

# 参考資料
- references/design_notes.md を参照
- 公式Python randomモジュール: https://docs.python.org/3/library/random.html