# os-random-fake-sudden-downtime-alert

> 作業が単調・長時間化している、またはユーザーが『緊急』『メンテ』『ダウンタイム』『OS』『通知』などのキーワードを含むリクエストや会話を行った際に発動。集中や緊張感が低下したタイミングで、意図的にフェイクのOS緊急ダウンタイム通知を表示することで、作業空間に刺激と遊び心を提供します。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Antigravity** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/fake_downtime_alert.py` - Fake OS Random Sudden Downtime Alert
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Antigravity 向け os-random-fake-sudden-downtime-alert の詳しい説明](https://ai-note.tech/os-random-fake-sudden-downtime-alert-antigravity/)
- 動作手順: [Antigravity で実際に動かす手順と検証](https://ai-note.tech/os-random-fake-sudden-downtime-alert-antigravity-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/antigravity/os-random-fake-sudden-downtime-alert .agent/skills/os-random-fake-sudden-downtime-alert
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/antigravity/os-random-fake-sudden-downtime-alert .agent/skills/os-random-fake-sudden-downtime-alert
```

配置後、Antigravity を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Antigravity: https://codelabs.developers.google.com/getting-started-with-antigravity-skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
