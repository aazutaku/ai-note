# random-os-fake-ancient-poem-notifier

> このSkillは、作業中やコマンド実行時など任意タイミングで“古文調の謎ポエム通知”をデスクトップやターミナルにランダム表示します。通知内容は完全ランダム生成で、作業内容やエラー情報とは無関係です。trigger: always, semantic, /random-os-fake-ancient-poem-notifier。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Claude Code** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/ancient_poem_notifier.py` - 謎のOS古代詩通知をデスクトップ/ターミナルにランダム表示するSkill
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Claude Code 向け random-os-fake-ancient-poem-notifier の詳しい説明](https://ai-note.tech/random-os-fake-ancient-poem-notifier-claude-code/)
- 動作手順: [Claude Code で実際に動かす手順と検証](https://ai-note.tech/random-os-fake-ancient-poem-notifier-claude-code-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/claude-code/random-os-fake-ancient-poem-notifier .claude/skills/random-os-fake-ancient-poem-notifier
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/claude-code/random-os-fake-ancient-poem-notifier .claude/skills/random-os-fake-ancient-poem-notifier
```

配置後、Claude Code を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Claude Code: https://code.claude.com/docs/ja/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
