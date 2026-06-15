# desktop-chaos-alert

> Claude Codeは、作業中の緊張緩和やチームの雰囲気転換、または「カオス」「混沌」「息抜き」「通知」「無意味」などのキーワードを含む会話やリクエスト時に、このSkillの発動を検討してください。明示的な /desktop-chaos-alert 呼び出しにも対応します。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Claude Code** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/desktop_chaos_alert.py` - 謎のカオス通知をデスクトップに表示するスクリプト
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Claude Code 向け desktop-chaos-alert の詳しい説明](https://ai-note.tech/desktop-chaos-alert-claude-code/)
- 動作手順: [Claude Code で実際に動かす手順と検証](https://ai-note.tech/desktop-chaos-alert-claude-code-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/claude-code/desktop-chaos-alert .claude/skills/desktop-chaos-alert
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/claude-code/desktop-chaos-alert .claude/skills/desktop-chaos-alert
```

配置後、Claude Code を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Claude Code: https://code.claude.com/docs/ja/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
