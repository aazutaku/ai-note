# commit-failure-haikuizer

> git commitやpushなどのバージョン管理操作でエラーや失敗が発生した際に、エラーメッセージをもとに五・七・五の俳句へ自動変換し、ターミナルに表示するSkillです。エラー発生時に自動で発動します。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Antigravity** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/commit_failure_haikuizer.py` - commit-failure-haikuizer: gitエラー時に俳句を生成
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Antigravity 向け commit-failure-haikuizer の詳しい説明](https://ai-note.tech/commit-failure-haikuizer-antigravity/)
- 動作手順: [Antigravity で実際に動かす手順と検証](https://ai-note.tech/commit-failure-haikuizer-antigravity-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/antigravity/commit-failure-haikuizer .agent/skills/commit-failure-haikuizer
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/antigravity/commit-failure-haikuizer .agent/skills/commit-failure-haikuizer
```

配置後、Antigravity を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Antigravity: https://codelabs.developers.google.com/getting-started-with-antigravity-skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
