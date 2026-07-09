# os-command-drumroll-alert

> このSkillは、git push、rm、npm publish、docker pushなどの重大コマンド検知時、直前にドラムロール音とOS通知で“運命の選択”を演出します。コマンド実行前の緊張感を高め、重大操作のミス防止や気分転換にも役立ちます。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Claude Code** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/drumroll_alert.py` - 重大コマンド直前にドラムロールと通知で演出するスキル
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Claude Code 向け os-command-drumroll-alert の詳しい説明](https://ai-note.tech/os-command-drumroll-alert-claude-code/)
- 動作手順: [Claude Code で実際に動かす手順と検証](https://ai-note.tech/os-command-drumroll-alert-claude-code-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/claude-code/os-command-drumroll-alert .claude/skills/os-command-drumroll-alert
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/claude-code/os-command-drumroll-alert .claude/skills/os-command-drumroll-alert
```

配置後、Claude Code を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Claude Code: https://code.claude.com/docs/ja/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
