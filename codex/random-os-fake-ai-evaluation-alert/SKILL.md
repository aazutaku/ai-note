---
name: random-os-fake-ai-evaluation-alert
description: 作業中やコマンド実行時、または/skillsやrandom-os-fake-ai-evaluation-alertへの明示呼び出し時に発動。通知・評価・AI・集中・警告などのキーワードや、ユーザーのアクションが検知された場合に適用。
---

# 機能概要
このSkillは、あなたの作業空間に突然「AIによるOS公式評価通知」を送りつけます。評価内容は完全ランダムで、真面目な体裁ながら理不尽・無意味なコメントが特徴です。例えば「AI判定: たぶん寝てる」「コーヒー摂取量が基準値超過」など、現実のAI社会を風刺した演出を提供します。実用的な効果はありませんが、作業の合間にクスッと笑える通知で空間にスパイスを加えます。

# 使い方
- 明示呼び出し: `/skills random-os-fake-ai-evaluation-alert` または `random-os-fake-ai-evaluation-alert` へのmentionで即時発動。
- 暗黙発動: 「通知」「評価」「AI」「集中」「警告」などのキーワードを含む会話やコマンド実行時に自動発動。頻度は内部で調整され、ウザすぎない程度に1時間数回程度。

# 出力例
```
[AI評価通知] 本日のあなたの集中度: AI判定「たぶん寝てる」
[AI評価通知] 自動分析: コーヒー摂取量が基準値超過
[AI評価通知] タイピング速度: AI基準「なぜか逆走中」
[AI評価通知] 作業効率: AI判定「謎の停滞モード」
[AI評価通知] 画面注視率: AI推測「たぶんYouTube」
[AI評価通知] AIによる自動評価: 今日のやる気指数「未検出」
```

# 注意点
- 本Skillは完全に無害で、システムやファイルに一切影響を与えません。
- 通知内容はすべてランダム生成され、実際の評価や監視は行いません。
- ローカル環境に履歴を保存しません。
- 頻度は過度にならないよう自動調整。

# 参考資料
- [references/design_notes.md](references/design_notes.md) に設計方針や利用例を記載
- OS通知: `notify-send` (Linux), `osascript` (macOS), `win10toast` (Windows)
- [Python subprocess公式](https://docs.python.org/3/library/subprocess.html)
