# random-os-sudden-boss-key

> 作業中に“ボスキー”を発動し、ターミナルやエディタ画面を即座に完全ランダムなダミー画面（謎グラフや警告）へ切り替えたい場合に利用。キーワード: ボスキー, 画面切替, ダミー, ランダム, 一時隠し。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Claude Code** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/random_boss_key.py` - Random OS Sudden Boss Key
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Claude Code 向け random-os-sudden-boss-key の詳しい説明](https://ai-note.tech/random-os-sudden-boss-key-claude-code/)
- 動作手順: [Claude Code で実際に動かす手順と検証](https://ai-note.tech/random-os-sudden-boss-key-claude-code-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/claude-code/random-os-sudden-boss-key .claude/skills/random-os-sudden-boss-key
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/claude-code/random-os-sudden-boss-key .claude/skills/random-os-sudden-boss-key
```

配置後、Claude Code を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Claude Code: https://code.claude.com/docs/ja/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
