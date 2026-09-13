# random-os-fake-caffeine-overdose-alert

> このSkillは、ユーザーが長時間作業や集中状態にあると推定される時、または明示的なコマンド実行時に、完全に架空のカフェイン過剰摂取警告をOS通知やターミナルに突然表示します。trigger: always, semantic, /random-os-fake-caffeine-overdose-alert。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Claude Code** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/caffeine_overdose_alert.py` - 謎のOSカフェイン過剰摂取フェイク警告を炸裂させるSkill
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Claude Code 向け random-os-fake-caffeine-overdose-alert の詳しい説明](https://ai-note.tech/random-os-fake-caffeine-overdose-alert-claude-code/)
- 動作手順: [Claude Code で実際に動かす手順と検証](https://ai-note.tech/random-os-fake-caffeine-overdose-alert-claude-code-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/claude-code/random-os-fake-caffeine-overdose-alert .claude/skills/random-os-fake-caffeine-overdose-alert
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/claude-code/random-os-fake-caffeine-overdose-alert .claude/skills/random-os-fake-caffeine-overdose-alert
```

配置後、Claude Code を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Claude Code: https://code.claude.com/docs/ja/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
