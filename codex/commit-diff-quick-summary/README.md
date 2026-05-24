# commit-diff-quick-summary

> コミット直前やコードレビュー時に、'git diff'や'コミット差分'などのキーワードを検出した際、または明示的なSkill呼び出し時に発動。差分内容をAIで要約し、主要な変更点や影響範囲を端的に提示します。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Codex** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/commit_diff_quick_summary.py` - 実行スクリプト
- `references/design_notes.md` - 参考資料

## 関連記事

- スキル詳細説明: [Codex 向け commit-diff-quick-summary の詳しい説明](https://ai-note.tech/commit-diff-quick-summary-codex/)
- 動作手順: [Codex で実際に動かす手順と検証](https://ai-note.tech/commit-diff-quick-summary-codex-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/codex/commit-diff-quick-summary .agents/skills/commit-diff-quick-summary
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/codex/commit-diff-quick-summary .agents/skills/commit-diff-quick-summary
```

配置後、Codex を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Codex: https://developers.openai.com/codex/skills

## 注意

このSkillは ai-note.tech が AI で設計したサンプルです。動作保証はありません。各自の環境で検証の上、ご利用ください。
