# random-os-mystery-boss-pop

> 作業中の集中やリマインダー、息抜きが必要なタイミング（例: 長時間作業・休憩忘れ・集中力低下など）に、ランダム生成の“謎OSボスキャラ”が画面端やデスクトップに突如現れ、ユニークな命令や警告を通知します。発動キーワード: ボス, 急襲, 休憩, ストレッチ, 魔王, 集中, OS演出。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Claude Code** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/random_os_mystery_boss_pop.py` - random-os-mystery-boss-pop: 謎のOSボスがランダムに出現し、命令や警告を通知します。
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Claude Code 向け random-os-mystery-boss-pop の詳しい説明](https://ai-note.tech/random-os-mystery-boss-pop-claude-code/)
- 動作手順: [Claude Code で実際に動かす手順と検証](https://ai-note.tech/random-os-mystery-boss-pop-claude-code-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/claude-code/random-os-mystery-boss-pop .claude/skills/random-os-mystery-boss-pop
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/claude-code/random-os-mystery-boss-pop .claude/skills/random-os-mystery-boss-pop
```

配置後、Claude Code を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Claude Code: https://code.claude.com/docs/ja/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
