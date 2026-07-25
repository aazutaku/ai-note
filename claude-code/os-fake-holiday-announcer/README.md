# os-fake-holiday-announcer

> 長時間のコーディングや単調作業、集中力が切れがちなタイミングで突如“OS公式の架空休日”をデスクトップ通知で演出します。trigger: always/semantic。明示呼び出しは /os-fake-holiday-announcer。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Claude Code** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/os_fake_holiday_announcer.py` - OS Fake Holiday Announcer
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Claude Code 向け os-fake-holiday-announcer の詳しい説明](https://ai-note.tech/os-fake-holiday-announcer-claude-code/)
- 動作手順: [Claude Code で実際に動かす手順と検証](https://ai-note.tech/os-fake-holiday-announcer-claude-code-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/claude-code/os-fake-holiday-announcer .claude/skills/os-fake-holiday-announcer
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/claude-code/os-fake-holiday-announcer .claude/skills/os-fake-holiday-announcer
```

配置後、Claude Code を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Claude Code: https://code.claude.com/docs/ja/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
