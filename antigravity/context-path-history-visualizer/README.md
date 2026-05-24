# context-path-history-visualizer

> 作業履歴やコンテキストパスの可視化が必要な際、または過去の分岐点・編集経路を把握したい時に発動。履歴抽出・ツリー表示・分岐検出などのキーワードが含まれる場合に適用。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Antigravity** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/context_path_history_visualizer.py` - context_path_history_visualizer.py (Pythonスクリプト)
- `references/design_notes.md` - 概要 - context-path-history-visualizerは、作業中のファイルやプロンプトの履歴を自動記録し、分岐や合流を含めてツリー表示するSkillです。履歴の可視化により、思考経路の把握や再

## 関連記事

- スキル詳細説明: [Antigravity 向け context-path-history-visualizer の詳しい説明](https://ai-note.tech/context-path-history-visualizer-antigravity/)
- 動作手順: [Antigravity で実際に動かす手順と検証](https://ai-note.tech/context-path-history-visualizer-antigravity-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/antigravity/context-path-history-visualizer .agent/skills/context-path-history-visualizer
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/antigravity/context-path-history-visualizer .agent/skills/context-path-history-visualizer
```

配置後、Antigravity を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Antigravity: https://codelabs.developers.google.com/getting-started-with-antigravity-skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
