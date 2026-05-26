# commit-dajare-generator

> Antigravity は、コミットメッセージ自動生成時や git commit 操作の直前にこのSkillを発動します。変更内容やファイル名を解析し、ダジャレを交えたユーモアあるメッセージを提案したい場合に最適です。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Antigravity** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/commit_dajare_generator.py` - commit-dajare-generator: コミット時ダジャレメッセージ生成
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Antigravity 向け commit-dajare-generator の詳しい説明](https://ai-note.tech/commit-dajare-generator-antigravity/)
- 動作手順: [Antigravity で実際に動かす手順と検証](https://ai-note.tech/commit-dajare-generator-antigravity-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/antigravity/commit-dajare-generator .agent/skills/commit-dajare-generator
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/antigravity/commit-dajare-generator .agent/skills/commit-dajare-generator
```

配置後、Antigravity を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Antigravity: https://codelabs.developers.google.com/getting-started-with-antigravity-skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
