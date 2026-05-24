# prompt-branch-suggester

> 作業ブランチ名、コミットメッセージ、直前のファイル差分などをもとに、Claude Code/Codex/Antigravity が適切なプロンプト分岐や一時的な指示セットを自動生成・提案するSkill。分岐提案や指示ファイル生成が必要な作業やイレギュラー対応時に発動。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Claude Code** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/prompt_branch_suggester.py` - 実行スクリプト
- `references/design_notes.md` - 参考資料

## 関連記事

- スキル詳細説明: [Claude Code 向け prompt-branch-suggester の詳しい説明](https://ai-note.tech/prompt-branch-suggester-claude-code/)
- 動作手順: [Claude Code で実際に動かす手順と検証](https://ai-note.tech/prompt-branch-suggester-claude-code-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/claude-code/prompt-branch-suggester .claude/skills/prompt-branch-suggester
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/claude-code/prompt-branch-suggester .claude/skills/prompt-branch-suggester
```

配置後、Claude Code を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Claude Code: https://code.claude.com/docs/ja/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
