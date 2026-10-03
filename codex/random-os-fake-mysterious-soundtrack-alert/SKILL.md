---
name: random-os-fake-mysterious-soundtrack-alert
description: 作業中やコマンド実行時、もしくは/skillsメニュー呼び出し時に、Codexが“謎のOS公式BGM推奨通知”をランダムに発動します。通知はジャンル不明の独自BGMタイトルを生成し、音は鳴らず演出のみ。気分転換や小ネタ投入に最適です。
---

# 機能概要
このSkillは、作業中やコマンド実行の合間に“謎のOS公式・本日の作業用BGM推奨通知”をランダムで表示します。通知内容は毎回異なり、ジャンル不明・独自のBGMタイトル（例：「Cドライブ幻想曲」「第3会議室の静寂」など）が生成されます。実際に音楽は流れませんが、作業空間に一瞬だけ“謎の演出感”を与え、気分転換や会話のネタとして活用できます。

# 使い方
- 明示的な呼び出し: `/skills random-os-fake-mysterious-soundtrack-alert` または `@codex random-os-fake-mysterious-soundtrack-alert`
- 暗黙トリガー: 「BGM」「作業用」「静寂」「集中」「OS通知」などのキーワードを含む発話や、コマンド実行の合間に自動発動

# 出力例
```
[OS公式通知] 本日の作業用BGM: 『未定義変数のバラード』
[OS公式通知] 本日の作業用BGM: 『第3会議室の静寂』
[OS公式通知] 本日の作業用BGM: 『Cドライブ幻想曲』
[OS公式通知] 本日の作業用BGM: 『再起動前夜のワルツ』
[OS公式通知] 本日の作業用BGM: 『メモリ不足の夜想曲』
```

# 注意点
- 実際に音楽は再生されません。通知・演出のみです。
- ローカルファイルや履歴には保存されません。
- 本Skillはジョーク・演出用途であり、業務システム通知とは無関係です。
- 通知タイミングや頻度は設定可能ですが、初期はコマンド実行の合間や明示呼び出し時のみ発動します。

# 参考資料
- references/design_notes.md に設計方針・利用例を記載
- 公式Python通知API: https://pypi.org/project/plyer/ など
- OS通知参考: https://docs.python.org/ja/3/library/subprocess.html