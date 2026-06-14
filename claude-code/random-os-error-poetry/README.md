# random-os-error-poetry

> コマンド実行やファイル操作などで発生したOSエラー（例: PermissionError, FileNotFoundError, OSError）を検知した際、自動的に詩的なエラーメッセージへ変換して表示します。エラー発生時や'/random-os-error-poetry'明示呼び出しで発動します。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Claude Code** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/random_os_error_poetry.py` - エラーメッセージから例外名とパス（あれば）を抽出する
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Claude Code 向け random-os-error-poetry の詳しい説明](https://ai-note.tech/random-os-error-poetry-claude-code/)
- 動作手順: [Claude Code で実際に動かす手順と検証](https://ai-note.tech/random-os-error-poetry-claude-code-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/claude-code/random-os-error-poetry .claude/skills/random-os-error-poetry
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/claude-code/random-os-error-poetry .claude/skills/random-os-error-poetry
```

配置後、Claude Code を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Claude Code: https://code.claude.com/docs/ja/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
