# random-os-error-poetry

> エラー発生時や例外メッセージ出力時、'Permission denied'や'File not found'などのキーワードを検知して、通常のエラーメッセージを詩的な文章に変換して表示します。コマンド失敗や例外時に自動発動。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Codex** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/poetry_wrapper.py` - random-os-error-poetry: OSエラーを即興詩に変換するラッパ
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Codex 向け random-os-error-poetry の詳しい説明](https://ai-note.tech/random-os-error-poetry-codex/)
- 動作手順: [Codex で実際に動かす手順と検証](https://ai-note.tech/random-os-error-poetry-codex-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/codex/random-os-error-poetry .agents/skills/random-os-error-poetry
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/codex/random-os-error-poetry .agents/skills/random-os-error-poetry
```

配置後、Codex を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Codex: https://developers.openai.com/codex/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
