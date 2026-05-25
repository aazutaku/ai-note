# terminal-mood-indicator

> ターミナルの環境変数（例: MOOD）が設定されている場合や、コマンドラインで明示的に呼び出された場合に発動します。"気分" "mood" "プロンプト" "環境変数" などのキーワードや、/terminal-mood-indicator コマンドがトリガーです。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Claude Code** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/terminal_mood_indicator.py` - ターミナル気分インジケータ
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Claude Code 向け terminal-mood-indicator の詳しい説明](https://ai-note.tech/terminal-mood-indicator-claude-code/)
- 動作手順: [Claude Code で実際に動かす手順と検証](https://ai-note.tech/terminal-mood-indicator-claude-code-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/claude-code/terminal-mood-indicator .claude/skills/terminal-mood-indicator
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/claude-code/terminal-mood-indicator .claude/skills/terminal-mood-indicator
```

配置後、Claude Code を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Claude Code: https://code.claude.com/docs/ja/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
