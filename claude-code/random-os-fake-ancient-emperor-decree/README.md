# random-os-fake-ancient-emperor-decree

> このSkillは、ターミナル操作や作業の合間に“OS公式・古代皇帝の勅令通知”をランダムな文面で表示します。通知・演出・OS連携カテゴリで、作業中やコマンド実行時、または明示的な呼び出し(/random-os-fake-ancient-emperor-decree)で発動します。通知内容は毎回異なり、威厳と理不尽さを兼ね備えた文体で、作業環境に一切影響を与えません。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Claude Code** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/emperor_decree_notifier.py` - 古代皇帝の勅令通知スクリプト
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Claude Code 向け random-os-fake-ancient-emperor-decree の詳しい説明](https://ai-note.tech/random-os-fake-ancient-emperor-decree-claude-code/)
- 動作手順: [Claude Code で実際に動かす手順と検証](https://ai-note.tech/random-os-fake-ancient-emperor-decree-claude-code-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/claude-code/random-os-fake-ancient-emperor-decree .claude/skills/random-os-fake-ancient-emperor-decree
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/claude-code/random-os-fake-ancient-emperor-decree .claude/skills/random-os-fake-ancient-emperor-decree
```

配置後、Claude Code を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Claude Code: https://code.claude.com/docs/ja/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
