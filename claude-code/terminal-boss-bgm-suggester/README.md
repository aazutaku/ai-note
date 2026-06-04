# terminal-boss-bgm-suggester

> 最初のターミナルコマンド実行時に、完全ランダムで“本日のあなたのテーマソング”をテキスト通知として提案します。発動条件は「その日最初のコマンド」または明示呼び出し（/terminal-boss-bgm-suggester）です。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Claude Code** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/bgm_suggester.py` - Terminal Boss BGM Suggester
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Claude Code 向け terminal-boss-bgm-suggester の詳しい説明](https://ai-note.tech/terminal-boss-bgm-suggester-claude-code/)
- 動作手順: [Claude Code で実際に動かす手順と検証](https://ai-note.tech/terminal-boss-bgm-suggester-claude-code-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/claude-code/terminal-boss-bgm-suggester .claude/skills/terminal-boss-bgm-suggester
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/claude-code/terminal-boss-bgm-suggester .claude/skills/terminal-boss-bgm-suggester
```

配置後、Claude Code を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Claude Code: https://code.claude.com/docs/ja/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
