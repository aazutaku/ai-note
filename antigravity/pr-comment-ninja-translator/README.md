# pr-comment-ninja-translator

> AntigravityがPull Requestのコメント内容を“忍者口調”に変換する必要がある場合に発動します。例えば、PRコメントの雰囲気を和らげたい、エンタメ要素を加えたい、または「忍者」「ござる」「拙者」などのキーワードが含まれる場合に適用されます。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Antigravity** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/ninja_translator.py` - PRコメントを忍者口調に変換するスクリプト
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Antigravity 向け pr-comment-ninja-translator の詳しい説明](https://ai-note.tech/pr-comment-ninja-translator-antigravity/)
- 動作手順: [Antigravity で実際に動かす手順と検証](https://ai-note.tech/pr-comment-ninja-translator-antigravity-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/antigravity/pr-comment-ninja-translator .agent/skills/pr-comment-ninja-translator
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/antigravity/pr-comment-ninja-translator .agent/skills/pr-comment-ninja-translator
```

配置後、Antigravity を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Antigravity: https://codelabs.developers.google.com/getting-started-with-antigravity-skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
