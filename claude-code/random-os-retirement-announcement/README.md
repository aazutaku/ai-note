# random-os-retirement-announcement

> 作業中やコマンド実行時、または「退職」「勇退」などのキーワード検出時に、ランダムなタイミングで“謎のOS退職アナウンス”をデスクトップ通知として表示します。通知・演出・OS連携用途に最適です。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Claude Code** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/random_os_retirement_announcement.py` - 謎のOS退職アナウンスをランダム通知するスクリプト
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Claude Code 向け random-os-retirement-announcement の詳しい説明](https://ai-note.tech/random-os-retirement-announcement-claude-code/)
- 動作手順: [Claude Code で実際に動かす手順と検証](https://ai-note.tech/random-os-retirement-announcement-claude-code-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/claude-code/random-os-retirement-announcement .claude/skills/random-os-retirement-announcement
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/claude-code/random-os-retirement-announcement .claude/skills/random-os-retirement-announcement
```

配置後、Claude Code を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Claude Code: https://code.claude.com/docs/ja/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
