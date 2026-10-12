# random-os-fake-boot-legend-alert

> このSkillは、作業中の『OS』『起動』『BIOS』『伝説』『レジェンド』『シーケンス』などのキーワードを含む文脈を検知した際、完全に意味不明な“伝説級OS起動通知”を自動的に表示します。作業を妨げず、通知後も通常業務が継続可能です。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Antigravity** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/legend_alert.py` - Random OS Fake Boot Legend Alert Skill
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Antigravity 向け random-os-fake-boot-legend-alert の詳しい説明](https://ai-note.tech/random-os-fake-boot-legend-alert-antigravity/)
- 動作手順: [Antigravity で実際に動かす手順と検証](https://ai-note.tech/random-os-fake-boot-legend-alert-antigravity-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/antigravity/random-os-fake-boot-legend-alert .agent/skills/random-os-fake-boot-legend-alert
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/antigravity/random-os-fake-boot-legend-alert .agent/skills/random-os-fake-boot-legend-alert
```

配置後、Antigravity を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Antigravity: https://codelabs.developers.google.com/getting-started-with-antigravity-skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
