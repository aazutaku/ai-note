# random-os-fake-legendary-quest-notification

> 作業中やキーワード検知時に、ランダムな“伝説のOSクエスト通知”を生成し、ユーザーの集中や気分転換をサポート。通知・演出・OS連携系のキーワードや明示呼び出しで発動。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Claude Code** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/legendary_quest_notifier.py` - 伝説のOSクエスト通知スクリプト
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Claude Code 向け random-os-fake-legendary-quest-notification の詳しい説明](https://ai-note.tech/random-os-fake-legendary-quest-notification-claude-code/)
- 動作手順: [Claude Code で実際に動かす手順と検証](https://ai-note.tech/random-os-fake-legendary-quest-notification-claude-code-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/claude-code/random-os-fake-legendary-quest-notification .claude/skills/random-os-fake-legendary-quest-notification
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/claude-code/random-os-fake-legendary-quest-notification .claude/skills/random-os-fake-legendary-quest-notification
```

配置後、Claude Code を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Claude Code: https://code.claude.com/docs/ja/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
