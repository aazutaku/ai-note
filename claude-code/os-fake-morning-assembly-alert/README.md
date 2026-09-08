# os-fake-morning-assembly-alert

> ターミナルやエディタの初回起動時、または「朝礼」や「スローガン」などのキーワード検知時に、謎の“OS朝礼通知”を画面に表示する演出スキルです。通知内容は毎回ランダムで変化し、日々の開発作業にユーモアを提供します。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Claude Code** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/morning_assembly_alert.py` - OS Fake Morning Assembly Alert
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Claude Code 向け os-fake-morning-assembly-alert の詳しい説明](https://ai-note.tech/os-fake-morning-assembly-alert-claude-code/)
- 動作手順: [Claude Code で実際に動かす手順と検証](https://ai-note.tech/os-fake-morning-assembly-alert-claude-code-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/claude-code/os-fake-morning-assembly-alert .claude/skills/os-fake-morning-assembly-alert
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/claude-code/os-fake-morning-assembly-alert .claude/skills/os-fake-morning-assembly-alert
```

配置後、Claude Code を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Claude Code: https://code.claude.com/docs/ja/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
