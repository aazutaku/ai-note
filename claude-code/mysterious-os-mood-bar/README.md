# mysterious-os-mood-bar

> ターミナルでコマンド実行時や /mysterious-os-mood-bar 呼び出し時、コマンド内容やgit statusの雰囲気から“気分温度”や“やる気指数”を適当に算出し、OSのメニューバーやステータスバーへ冗談的に表示します。明示コマンドや on-demand キーワードで発動。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Claude Code** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/mood_bar.py` - mysterious-os-mood-bar: 気分温度ややる気指数を冗談的に表示するスキル
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Claude Code 向け mysterious-os-mood-bar の詳しい説明](https://ai-note.tech/mysterious-os-mood-bar-claude-code/)
- 動作手順: [Claude Code で実際に動かす手順と検証](https://ai-note.tech/mysterious-os-mood-bar-claude-code-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/claude-code/mysterious-os-mood-bar .claude/skills/mysterious-os-mood-bar
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/claude-code/mysterious-os-mood-bar .claude/skills/mysterious-os-mood-bar
```

配置後、Claude Code を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Claude Code: https://code.claude.com/docs/ja/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
