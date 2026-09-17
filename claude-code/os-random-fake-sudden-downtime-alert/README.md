# os-random-fake-sudden-downtime-alert

> 長時間の作業や集中状態、単調なコーディングセッション中に“緊急ダウンタイム通知”の演出で気分転換や遊び心を加えたい場合に発動。明示的な /os-random-fake-sudden-downtime-alert コマンドや「ダウンタイム」「メンテ」「OS異常」などのキーワードで自動発火します。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Claude Code** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/os_random_fake_sudden_downtime_alert.py` - os-random-fake-sudden-downtime-alert: フェイクOS緊急通知ジェネレータ
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Claude Code 向け os-random-fake-sudden-downtime-alert の詳しい説明](https://ai-note.tech/os-random-fake-sudden-downtime-alert-claude-code/)
- 動作手順: [Claude Code で実際に動かす手順と検証](https://ai-note.tech/os-random-fake-sudden-downtime-alert-claude-code-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/claude-code/os-random-fake-sudden-downtime-alert .claude/skills/os-random-fake-sudden-downtime-alert
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/claude-code/os-random-fake-sudden-downtime-alert .claude/skills/os-random-fake-sudden-downtime-alert
```

配置後、Claude Code を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Claude Code: https://code.claude.com/docs/ja/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
