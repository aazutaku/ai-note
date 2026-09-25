# pr-comment-ninja-translator

> Pull Requestのコメントが投稿・編集される際や、/pr-comment-ninja-translator コマンドで明示的に呼び出された場合に発動。キーワード: PRコメント, 忍者口調, ジョーク, 変換, レビュー。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Claude Code** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/ninja_translator.py` - 1文を忍者口調へ変換する
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Claude Code 向け pr-comment-ninja-translator の詳しい説明](https://ai-note.tech/pr-comment-ninja-translator-claude-code/)
- 動作手順: [Claude Code で実際に動かす手順と検証](https://ai-note.tech/pr-comment-ninja-translator-claude-code-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/claude-code/pr-comment-ninja-translator .claude/skills/pr-comment-ninja-translator
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/claude-code/pr-comment-ninja-translator .claude/skills/pr-comment-ninja-translator
```

配置後、Claude Code を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Claude Code: https://code.claude.com/docs/ja/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
