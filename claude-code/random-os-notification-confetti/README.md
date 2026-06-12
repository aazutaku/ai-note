# random-os-notification-confetti

> コマンド実行や作業の合間に、ランダムなタイミング・内容でOS標準通知領域に“ネタ系お祝いメッセージ”を表示します。通知・祝福・ランダム・気分転換・演出などのキーワードや、明示的な /random-os-notification-confetti 呼び出し時に発動します。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Claude Code** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/random_os_notification_confetti.py` - 謎のコンフェッティ祝福通知スクリプト
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Claude Code 向け random-os-notification-confetti の詳しい説明](https://ai-note.tech/random-os-notification-confetti-claude-code/)
- 動作手順: [Claude Code で実際に動かす手順と検証](https://ai-note.tech/random-os-notification-confetti-claude-code-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/claude-code/random-os-notification-confetti .claude/skills/random-os-notification-confetti
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/claude-code/random-os-notification-confetti .claude/skills/random-os-notification-confetti
```

配置後、Claude Code を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Claude Code: https://code.claude.com/docs/ja/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
