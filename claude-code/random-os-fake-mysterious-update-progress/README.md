# random-os-fake-mysterious-update-progress

> 作業中に『謎のOSアップデート進行中』の進捗バーをランダム表示し、進捗内容や挙動が理不尽で意味不明な場合にこのSkillを発動します。キーワード: 進捗バー, OSアップデート, 謎, 演出, 非日常。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Claude Code** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/mysterious_update_progress.py` - 謎のOSアップデート進捗バー演出
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Claude Code 向け random-os-fake-mysterious-update-progress の詳しい説明](https://ai-note.tech/random-os-fake-mysterious-update-progress-claude-code/)
- 動作手順: [Claude Code で実際に動かす手順と検証](https://ai-note.tech/random-os-fake-mysterious-update-progress-claude-code-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/claude-code/random-os-fake-mysterious-update-progress .claude/skills/random-os-fake-mysterious-update-progress
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/claude-code/random-os-fake-mysterious-update-progress .claude/skills/random-os-fake-mysterious-update-progress
```

配置後、Claude Code を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Claude Code: https://code.claude.com/docs/ja/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
