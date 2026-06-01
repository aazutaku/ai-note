# boss-key-fake-excel

> 作業中に“あっヤバい！”という瞬間や監督者の気配を感じた際、即座に本Skillを発動し、ターミナルやエディタ画面をExcel風フェイク画面に切り替えて視線を欺きます。boss、監査、急な来客などのキーワードで発動。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Claude Code** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/boss_key_fake_excel.py` - 瞬時にExcel風フェイク画面を表示するBossKeyスクリプト
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Claude Code 向け boss-key-fake-excel の詳しい説明](https://ai-note.tech/boss-key-fake-excel-claude-code/)
- 動作手順: [Claude Code で実際に動かす手順と検証](https://ai-note.tech/boss-key-fake-excel-claude-code-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/claude-code/boss-key-fake-excel .claude/skills/boss-key-fake-excel
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/claude-code/boss-key-fake-excel .claude/skills/boss-key-fake-excel
```

配置後、Claude Code を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Claude Code: https://code.claude.com/docs/ja/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
