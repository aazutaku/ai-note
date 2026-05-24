# context-branch-highlighter

> 複数の作業ブランチやタスクが混在し、どの流れに注力すべきか曖昧な場合に発動。"作業中のブランチ" "直近の編集" "分岐の可視化" などのキーワードや明示コマンドで実行。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Claude Code** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/context_branch_highlighter.py` - 実行スクリプト
- `references/design_notes.md` - 参考資料

## 関連記事

- スキル詳細説明: [Claude Code 向け context-branch-highlighter の詳しい説明](https://ai-note.tech/context-branch-highlighter-claude-code/)
- 動作手順: [Claude Code で実際に動かす手順と検証](https://ai-note.tech/context-branch-highlighter-claude-code-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/claude-code/context-branch-highlighter .claude/skills/context-branch-highlighter
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/claude-code/context-branch-highlighter .claude/skills/context-branch-highlighter
```

配置後、Claude Code を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Claude Code: https://code.claude.com/docs/ja/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
