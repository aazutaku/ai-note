# os-random-fake-motivational-speech-alert

> コマンド実行時や作業中に、毎回内容が異なる“公式風やる気爆上げスピーチ”通知を発動。通知内容は本気の激励風で、明示的な呼び出し（/os-random-fake-motivational-speech-alert）や任意の作業トリガーで発生します。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Claude Code** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/motivational_alert.py` - Cross-platform notification. Falls back to stdout if GUI notification fails.
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Claude Code 向け os-random-fake-motivational-speech-alert の詳しい説明](https://ai-note.tech/os-random-fake-motivational-speech-alert-claude-code/)
- 動作手順: [Claude Code で実際に動かす手順と検証](https://ai-note.tech/os-random-fake-motivational-speech-alert-claude-code-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/claude-code/os-random-fake-motivational-speech-alert .claude/skills/os-random-fake-motivational-speech-alert
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/claude-code/os-random-fake-motivational-speech-alert .claude/skills/os-random-fake-motivational-speech-alert
```

配置後、Claude Code を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Claude Code: https://code.claude.com/docs/ja/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
