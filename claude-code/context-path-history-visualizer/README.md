# context-path-history-visualizer

> Claude Code で複数のプロンプトやファイル間を移動した際、コンテキストのパス履歴や思考経路を自動で可視化したい場合に発動します。履歴の分岐・合流や出発点、編集フローの全体像を把握したいときに有効です。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Claude Code** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/context_path_history.py` - context_path_history.py (Pythonスクリプト)
- `references/design_notes.md` - 概要 - このスキルは、Claude Code のセッション内でのプロンプトやファイル編集の履歴を自動的に記録し、ツリー構造で可視化することを目的としています。履歴はローカルファイルに保存され、セッション全体の

## 関連記事

- スキル詳細説明: [Claude Code 向け context-path-history-visualizer の詳しい説明](https://ai-note.tech/context-path-history-visualizer-claude-code/)
- 動作手順: [Claude Code で実際に動かす手順と検証](https://ai-note.tech/context-path-history-visualizer-claude-code-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/claude-code/context-path-history-visualizer .claude/skills/context-path-history-visualizer
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/claude-code/context-path-history-visualizer .claude/skills/context-path-history-visualizer
```

配置後、Claude Code を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Claude Code: https://code.claude.com/docs/ja/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
