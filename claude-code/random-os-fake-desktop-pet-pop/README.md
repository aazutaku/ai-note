# random-os-fake-desktop-pet-pop

> Claude Codeがユーザーの作業中や長時間無操作時、または明示的な /random-os-fake-desktop-pet-pop コマンド実行時に発動。通知・癒し・集中力リセットなどのキーワードや、作業の合間のリフレッシュ提案時に最適。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Claude Code** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/desktop_pet_pop.py` - random-os-fake-desktop-pet-pop: 謎のデスクトップペットが乱入するエンタメSkill
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Claude Code 向け random-os-fake-desktop-pet-pop の詳しい説明](https://ai-note.tech/random-os-fake-desktop-pet-pop-claude-code/)
- 動作手順: [Claude Code で実際に動かす手順と検証](https://ai-note.tech/random-os-fake-desktop-pet-pop-claude-code-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/claude-code/random-os-fake-desktop-pet-pop .claude/skills/random-os-fake-desktop-pet-pop
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/claude-code/random-os-fake-desktop-pet-pop .claude/skills/random-os-fake-desktop-pet-pop
```

配置後、Claude Code を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Claude Code: https://code.claude.com/docs/ja/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
