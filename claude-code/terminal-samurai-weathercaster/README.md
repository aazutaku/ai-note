# terminal-samurai-weathercaster

> ターミナル起動時や /terminal-samurai-weathercaster コマンド実行時に、毎回異なる“侍天気予報”コメントをランダム生成し表示します。現実の天気やAPI参照は一切せず、作業気分を演出する演出系スキルです。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Claude Code** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/samurai_weathercaster.py` - terminal-samurai-weathercaster: ターミナル侍天気予報スキル
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Claude Code 向け terminal-samurai-weathercaster の詳しい説明](https://ai-note.tech/terminal-samurai-weathercaster-claude-code/)
- 動作手順: [Claude Code で実際に動かす手順と検証](https://ai-note.tech/terminal-samurai-weathercaster-claude-code-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/claude-code/terminal-samurai-weathercaster .claude/skills/terminal-samurai-weathercaster
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/claude-code/terminal-samurai-weathercaster .claude/skills/terminal-samurai-weathercaster
```

配置後、Claude Code を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Claude Code: https://code.claude.com/docs/ja/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
