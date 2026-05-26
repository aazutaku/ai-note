# commit-dajare-generator

> コミット時や /commit-dajare-generator 明示呼び出し時に、変更内容やファイル名をもとに理系ダジャレ満載のコミットメッセージを自動生成します。commit・変更・ファイル名・メッセージ生成などのキーワードで発動。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Claude Code** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/commit_dajare_generator.py` - コミット時に理系ダジャレメッセージを生成するスキル
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Claude Code 向け commit-dajare-generator の詳しい説明](https://ai-note.tech/commit-dajare-generator-claude-code/)
- 動作手順: [Claude Code で実際に動かす手順と検証](https://ai-note.tech/commit-dajare-generator-claude-code-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/claude-code/commit-dajare-generator .claude/skills/commit-dajare-generator
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/claude-code/commit-dajare-generator .claude/skills/commit-dajare-generator
```

配置後、Claude Code を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Claude Code: https://code.claude.com/docs/ja/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
