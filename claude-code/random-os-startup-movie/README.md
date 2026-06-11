# random-os-startup-movie

> ターミナルやエディタの起動、または /random-os-startup-movie コマンド実行時に、毎回異なる“架空OSの起動画面”をテキストアニメーションとして表示します。発動条件は『起動』『open』『start』『launch』などのキーワード検知、または明示的なSkill呼び出しです。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Claude Code** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/random_os_startup_movie.py` - 毎回異なる架空OSの起動画面をテキストアニメーションで表示するスキル
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Claude Code 向け random-os-startup-movie の詳しい説明](https://ai-note.tech/random-os-startup-movie-claude-code/)
- 動作手順: [Claude Code で実際に動かす手順と検証](https://ai-note.tech/random-os-startup-movie-claude-code-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/claude-code/random-os-startup-movie .claude/skills/random-os-startup-movie
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/claude-code/random-os-startup-movie .claude/skills/random-os-startup-movie
```

配置後、Claude Code を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Claude Code: https://code.claude.com/docs/ja/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
