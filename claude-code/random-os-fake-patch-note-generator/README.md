# random-os-fake-patch-note-generator

> このSkillは、Claude Codeでコマンド実行やファイル編集などのアクション時に自動発動し、または /random-os-fake-patch-note-generator で明示的にも呼び出せます。発動キーワード例: 実行、保存、ビルド、run、save、commit。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Claude Code** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/random_os_fake_patch_note_generator.py` - Random OS Fake Patch Note Generator
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Claude Code 向け random-os-fake-patch-note-generator の詳しい説明](https://ai-note.tech/random-os-fake-patch-note-generator-claude-code/)
- 動作手順: [Claude Code で実際に動かす手順と検証](https://ai-note.tech/random-os-fake-patch-note-generator-claude-code-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/claude-code/random-os-fake-patch-note-generator .claude/skills/random-os-fake-patch-note-generator
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/claude-code/random-os-fake-patch-note-generator .claude/skills/random-os-fake-patch-note-generator
```

配置後、Claude Code を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Claude Code: https://code.claude.com/docs/ja/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
