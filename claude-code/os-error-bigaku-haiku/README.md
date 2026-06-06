# os-error-bigaku-haiku

> ターミナルやCLIでコマンド実行時にOSエラー（例: Permission denied, File not found, Segmentation fault等）が発生した際、そのエラー内容を和風俳句に変換し、元のエラーとともに表示するSkill。エラー発生時・明示コマンド呼び出し時に発動。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Claude Code** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/os_error_bigaku_haiku.py` - 標準入力からエラーらしき行を検出し、俳句化して表示
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Claude Code 向け os-error-bigaku-haiku の詳しい説明](https://ai-note.tech/os-error-bigaku-haiku-claude-code/)
- 動作手順: [Claude Code で実際に動かす手順と検証](https://ai-note.tech/os-error-bigaku-haiku-claude-code-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/claude-code/os-error-bigaku-haiku .claude/skills/os-error-bigaku-haiku
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/claude-code/os-error-bigaku-haiku .claude/skills/os-error-bigaku-haiku
```

配置後、Claude Code を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Claude Code: https://code.claude.com/docs/ja/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
