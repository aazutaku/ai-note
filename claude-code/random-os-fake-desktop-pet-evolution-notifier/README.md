# random-os-fake-desktop-pet-evolution-notifier

> このSkillは、作業中やコード編集時、または「ペット」「進化」「通知」などのキーワードを含む会話やコマンドがあった際に発動します。ユーザーが明示的に /random-os-fake-desktop-pet-evolution-notifier を呼び出した場合も通知が生成されます。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Claude Code** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/pet_evolution_notifier.py` - 謎のOSデスクトップペット進化通知スクリプト
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Claude Code 向け random-os-fake-desktop-pet-evolution-notifier の詳しい説明](https://ai-note.tech/random-os-fake-desktop-pet-evolution-notifier-claude-code/)
- 動作手順: [Claude Code で実際に動かす手順と検証](https://ai-note.tech/random-os-fake-desktop-pet-evolution-notifier-claude-code-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/claude-code/random-os-fake-desktop-pet-evolution-notifier .claude/skills/random-os-fake-desktop-pet-evolution-notifier
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/claude-code/random-os-fake-desktop-pet-evolution-notifier .claude/skills/random-os-fake-desktop-pet-evolution-notifier
```

配置後、Claude Code を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Claude Code: https://code.claude.com/docs/ja/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
