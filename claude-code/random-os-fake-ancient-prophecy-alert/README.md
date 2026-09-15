# random-os-fake-ancient-prophecy-alert

> 作業中やコマンド実行後に、キーワード（build, run, test, deploy, commit, push, install, update, error, warning, success）を検知した時、または明示的な呼び出し時に、古代OS風の予言通知をランダムに生成・表示します。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Claude Code** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/prophecy_alert.py` - 謎のOS古代予言通知をランダムに表示
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Claude Code 向け random-os-fake-ancient-prophecy-alert の詳しい説明](https://ai-note.tech/random-os-fake-ancient-prophecy-alert-claude-code/)
- 動作手順: [Claude Code で実際に動かす手順と検証](https://ai-note.tech/random-os-fake-ancient-prophecy-alert-claude-code-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/claude-code/random-os-fake-ancient-prophecy-alert .claude/skills/random-os-fake-ancient-prophecy-alert
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/claude-code/random-os-fake-ancient-prophecy-alert .claude/skills/random-os-fake-ancient-prophecy-alert
```

配置後、Claude Code を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Claude Code: https://code.claude.com/docs/ja/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
