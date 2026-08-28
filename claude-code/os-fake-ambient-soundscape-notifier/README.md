# os-fake-ambient-soundscape-notifier

> 作業やコーディング中に“環境音通知”を演出したい場面や、集中力・気分転換を促す擬似OS通知を体験したい時に発動。キーワード例: 環境音, BGM, 集中, 通知, フェイク, OS演出, 休憩, クリエイティブ。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Claude Code** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/fake_ambient_soundscape_notifier.py` - OSフェイク環境音通知スキル
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Claude Code 向け os-fake-ambient-soundscape-notifier の詳しい説明](https://ai-note.tech/os-fake-ambient-soundscape-notifier-claude-code/)
- 動作手順: [Claude Code で実際に動かす手順と検証](https://ai-note.tech/os-fake-ambient-soundscape-notifier-claude-code-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/claude-code/os-fake-ambient-soundscape-notifier .claude/skills/os-fake-ambient-soundscape-notifier
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/claude-code/os-fake-ambient-soundscape-notifier .claude/skills/os-fake-ambient-soundscape-notifier
```

配置後、Claude Code を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Claude Code: https://code.claude.com/docs/ja/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
