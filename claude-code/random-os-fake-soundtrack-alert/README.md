# random-os-fake-soundtrack-alert

> このSkillは、Claude Codeでコマンド実行や作業開始時などのタイミングで、毎回異なる“架空のOS公式サウンドトラック通知”をデスクトップに表示します。通知内容や曲名は完全オリジナルで、実際に音は流れません。作業の緊張感を和らげるジョーク演出や、沈黙を打ち破るユーモアな通知が欲しい場合に最適です。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Claude Code** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/random_os_fake_soundtrack_alert.py` - 謎のOS公式サウンドトラック通知を表示するジョークスクリプト。音は流れません。
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Claude Code 向け random-os-fake-soundtrack-alert の詳しい説明](https://ai-note.tech/random-os-fake-soundtrack-alert-claude-code/)
- 動作手順: [Claude Code で実際に動かす手順と検証](https://ai-note.tech/random-os-fake-soundtrack-alert-claude-code-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/claude-code/random-os-fake-soundtrack-alert .claude/skills/random-os-fake-soundtrack-alert
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/claude-code/random-os-fake-soundtrack-alert .claude/skills/random-os-fake-soundtrack-alert
```

配置後、Claude Code を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Claude Code: https://code.claude.com/docs/ja/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
