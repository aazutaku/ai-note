# commit-diff-quick-summary

> コミット前の git diff や staged changes を自動要約したいとき、または "差分要約" や "変更点確認" などのキーワードがプロンプトや指示に含まれる場合に発動します。変更点の見落とし防止やレビュー効率化が求められる場面で有効です。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Antigravity** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/diff_quick_summary.py` - 実行スクリプト
- `references/design_notes.md` - 参考資料

## 関連記事

- スキル詳細説明: [Antigravity 向け commit-diff-quick-summary の詳しい説明](https://ai-note.tech/commit-diff-quick-summary-antigravity/)
- 動作手順: [Antigravity で実際に動かす手順と検証](https://ai-note.tech/commit-diff-quick-summary-antigravity-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/antigravity/commit-diff-quick-summary .agent/skills/commit-diff-quick-summary
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/antigravity/commit-diff-quick-summary .agent/skills/commit-diff-quick-summary
```

配置後、Antigravity を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Antigravity: https://codelabs.developers.google.com/getting-started-with-antigravity-skills

## 注意

このSkillは ai-note.tech が AI で設計したサンプルです。動作保証はありません。各自の環境で検証の上、ご利用ください。
