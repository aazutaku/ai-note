# random-os-error-poetry

> Antigravity でコマンド実行やファイル操作時に 'Permission denied' や 'File not found' などの典型的なOSエラーが発生した際、自動で詩的なメッセージに変換して表示するSkillです。エラー内容のキーワード検出時に発動します。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Antigravity** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/os_error_poetry.py` - OSエラーを詩的に変換するCLIツール
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Antigravity 向け random-os-error-poetry の詳しい説明](https://ai-note.tech/random-os-error-poetry-antigravity/)
- 動作手順: [Antigravity で実際に動かす手順と検証](https://ai-note.tech/random-os-error-poetry-antigravity-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/antigravity/random-os-error-poetry .agent/skills/random-os-error-poetry
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/antigravity/random-os-error-poetry .agent/skills/random-os-error-poetry
```

配置後、Antigravity を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Antigravity: https://codelabs.developers.google.com/getting-started-with-antigravity-skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
