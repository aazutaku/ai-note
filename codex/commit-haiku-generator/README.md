# commit-haiku-generator

> コミットメッセージ生成や git commit 操作時に、"haiku" "俳句" "五七五" "poem" などのキーワードや明示的なSkill呼び出しが検出された場合に発動します。コミット内容を和風の五・七・五俳句形式へ自動変換したい時に最適です。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Codex** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/commit_haiku_generator.py` - コミットメッセージを俳句（五・七・五）に変換します。
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Codex 向け commit-haiku-generator の詳しい説明](https://ai-note.tech/commit-haiku-generator-codex/)
- 動作手順: [Codex で実際に動かす手順と検証](https://ai-note.tech/commit-haiku-generator-codex-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/codex/commit-haiku-generator .agents/skills/commit-haiku-generator
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/codex/commit-haiku-generator .agents/skills/commit-haiku-generator
```

配置後、Codex を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Codex: https://developers.openai.com/codex/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
