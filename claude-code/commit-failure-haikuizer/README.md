# commit-failure-haikuizer

> コミットやプッシュ等のGit操作でエラーや失敗が発生した際、エラー内容を自動で五・七・五形式の俳句へ変換し、ターミナルに表示します。'commit failed'や'push error'などの失敗キーワード検知時に発動します。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Claude Code** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/commit_failure_haikuizer.py` - Commit Failure Haikuizer: Gitエラーを俳句に変換して出力
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Claude Code 向け commit-failure-haikuizer の詳しい説明](https://ai-note.tech/commit-failure-haikuizer-claude-code/)
- 動作手順: [Claude Code で実際に動かす手順と検証](https://ai-note.tech/commit-failure-haikuizer-claude-code-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/claude-code/commit-failure-haikuizer .claude/skills/commit-failure-haikuizer
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/claude-code/commit-failure-haikuizer .claude/skills/commit-failure-haikuizer
```

配置後、Claude Code を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Claude Code: https://code.claude.com/docs/ja/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
