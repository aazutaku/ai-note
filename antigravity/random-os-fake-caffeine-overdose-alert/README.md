# random-os-fake-caffeine-overdose-alert

> 作業集中・長時間稼働・徹夜・カフェイン・エンジニア・OS通知・警告・突然・フェイクなどのキーワードを含む会話やコード編集時、Antigravityが理不尽なタイミングでこのSkillを発動します。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Antigravity** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/fake_caffeine_alert.py` - Fake Caffeine Overdose Alert Skill
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Antigravity 向け random-os-fake-caffeine-overdose-alert の詳しい説明](https://ai-note.tech/random-os-fake-caffeine-overdose-alert-antigravity/)
- 動作手順: [Antigravity で実際に動かす手順と検証](https://ai-note.tech/random-os-fake-caffeine-overdose-alert-antigravity-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/antigravity/random-os-fake-caffeine-overdose-alert .agent/skills/random-os-fake-caffeine-overdose-alert
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/antigravity/random-os-fake-caffeine-overdose-alert .agent/skills/random-os-fake-caffeine-overdose-alert
```

配置後、Antigravity を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Antigravity: https://codelabs.developers.google.com/getting-started-with-antigravity-skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
