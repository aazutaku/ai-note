# random-os-fake-it-hero-summon-notifier

> このSkillは、作業中やコマンド実行時などに「英雄召喚」風のランダム通知を発動します。通知・演出・孤独感緩和・OS連携を求める場面や、/skills メニューや skill名を明示的に呼び出した時に発動します。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Codex** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/hero_summon_notifier.py` - random-os-fake-it-hero-summon-notifier
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Codex 向け random-os-fake-it-hero-summon-notifier の詳しい説明](https://ai-note.tech/random-os-fake-it-hero-summon-notifier-codex/)
- 動作手順: [Codex で実際に動かす手順と検証](https://ai-note.tech/random-os-fake-it-hero-summon-notifier-codex-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/codex/random-os-fake-it-hero-summon-notifier .agents/skills/random-os-fake-it-hero-summon-notifier
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/codex/random-os-fake-it-hero-summon-notifier .agents/skills/random-os-fake-it-hero-summon-notifier
```

配置後、Codex を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Codex: https://developers.openai.com/codex/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
