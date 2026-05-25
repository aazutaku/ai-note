# commit-haiku-generator

> コミットメッセージ生成や編集時、または "haiku" "五七五" "俳句" などのキーワードを含むリクエスト時に発動。コミット文を自動で五・七・五の俳句形式に変換したい場合に利用されます。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Antigravity** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/commit_haiku_generator.py` - コミットメッセージを俳句に変換
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Antigravity 向け commit-haiku-generator の詳しい説明](https://ai-note.tech/commit-haiku-generator-antigravity/)
- 動作手順: [Antigravity で実際に動かす手順と検証](https://ai-note.tech/commit-haiku-generator-antigravity-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/antigravity/commit-haiku-generator .agent/skills/commit-haiku-generator
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/antigravity/commit-haiku-generator .agent/skills/commit-haiku-generator
```

配置後、Antigravity を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Antigravity: https://codelabs.developers.google.com/getting-started-with-antigravity-skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
