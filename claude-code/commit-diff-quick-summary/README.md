# commit-diff-quick-summary

> コミット前の変更差分(git diff)が存在し、主要な変更点や影響範囲を素早く把握したい場合に発動します。キーワード: diff, 差分, 要約, 変更点, 影響範囲, commit, 変更確認。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Claude Code** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/commit_diff_quick_summary.py` - 実行スクリプト
- `references/design_notes.md` - 参考資料

## 関連記事

- スキル詳細説明: [Claude Code 向け commit-diff-quick-summary の詳しい説明](https://ai-note.tech/commit-diff-quick-summary-claude-code/)
- 動作手順: [Claude Code で実際に動かす手順と検証](https://ai-note.tech/commit-diff-quick-summary-claude-code-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/claude-code/commit-diff-quick-summary .claude/skills/commit-diff-quick-summary
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/claude-code/commit-diff-quick-summary .claude/skills/commit-diff-quick-summary
```

配置後、Claude Code を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Claude Code: https://code.claude.com/docs/ja/skills

## 注意

このSkillは ai-note.tech が AI で設計したサンプルです。動作保証はありません。各自の環境で検証の上、ご利用ください。
