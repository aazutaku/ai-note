# command-failure-excuse-notifier

> コマンド実行時にエラーや失敗が検出された場合、“言い訳”付きでOS通知を発火します。失敗検知・エラー出力・通知連携が必要な場面で自動発動します。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Claude Code** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/command_failure_excuse_notifier.py` - コマンド失敗時に言い訳を通知するSkill
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Claude Code 向け command-failure-excuse-notifier の詳しい説明](https://ai-note.tech/command-failure-excuse-notifier-claude-code/)
- 動作手順: [Claude Code で実際に動かす手順と検証](https://ai-note.tech/command-failure-excuse-notifier-claude-code-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/claude-code/command-failure-excuse-notifier .claude/skills/command-failure-excuse-notifier
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/claude-code/command-failure-excuse-notifier .claude/skills/command-failure-excuse-notifier
```

配置後、Claude Code を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Claude Code: https://code.claude.com/docs/ja/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
