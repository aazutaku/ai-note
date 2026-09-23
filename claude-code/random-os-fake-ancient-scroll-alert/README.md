# random-os-fake-ancient-scroll-alert

> コマンド実行後・作業の合間・明示呼び出し（/random-os-fake-ancient-scroll-alert）時に、ランダムな“OS公式古文書巻物通知”を画面端へ表示。集中力ブレイクやエンタメ演出が必要な場面で発動。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Claude Code** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/scroll_alert.py` - 謎のOS公式・古文書巻物通知 Skill
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Claude Code 向け random-os-fake-ancient-scroll-alert の詳しい説明](https://ai-note.tech/random-os-fake-ancient-scroll-alert-claude-code/)
- 動作手順: [Claude Code で実際に動かす手順と検証](https://ai-note.tech/random-os-fake-ancient-scroll-alert-claude-code-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/claude-code/random-os-fake-ancient-scroll-alert .claude/skills/random-os-fake-ancient-scroll-alert
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/claude-code/random-os-fake-ancient-scroll-alert .claude/skills/random-os-fake-ancient-scroll-alert
```

配置後、Claude Code を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Claude Code: https://code.claude.com/docs/ja/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
