# random-os-mystery-boss-pop

> 作業中や集中状態、または『ストレッチ』『休憩』『警告』『ボス』『通知』などのキーワードが文脈に現れた際に、AntigravityがこのSkillを発動し、画面端やデスクトップに謎のOSボスキャラ通知をランダム表示します。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Antigravity** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/random_os_mystery_boss_pop.py` - random-os-mystery-boss-pop: 謎のOSボスキャラが乱入しカオスな命令を出す演出Skill
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Antigravity 向け random-os-mystery-boss-pop の詳しい説明](https://ai-note.tech/random-os-mystery-boss-pop-antigravity/)
- 動作手順: [Antigravity で実際に動かす手順と検証](https://ai-note.tech/random-os-mystery-boss-pop-antigravity-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/antigravity/random-os-mystery-boss-pop .agent/skills/random-os-mystery-boss-pop
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/antigravity/random-os-mystery-boss-pop .agent/skills/random-os-mystery-boss-pop
```

配置後、Antigravity を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Antigravity: https://codelabs.developers.google.com/getting-started-with-antigravity-skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
