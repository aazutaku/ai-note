# boss-key-instant-hide

> 作業中に『見られたくない画面』を即座に隠したい状況（上司・親の接近、監視の気配、緊急回避など）で発動。hide/隠す/見られたくない/一発/ボスキー/進捗バー/偽装画面 などのキーワードで発動を推奨。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Claude Code** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/boss_key_instant_hide.py` - エディタ・ターミナル系ウィンドウを列挙し、隠す対象を返す
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Claude Code 向け boss-key-instant-hide の詳しい説明](https://ai-note.tech/boss-key-instant-hide-claude-code/)
- 動作手順: [Claude Code で実際に動かす手順と検証](https://ai-note.tech/boss-key-instant-hide-claude-code-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/claude-code/boss-key-instant-hide .claude/skills/boss-key-instant-hide
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/claude-code/boss-key-instant-hide .claude/skills/boss-key-instant-hide
```

配置後、Claude Code を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Claude Code: https://code.claude.com/docs/ja/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
