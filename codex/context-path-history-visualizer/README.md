# context-path-history-visualizer

> Codexが複数のプロンプトやファイル間での作業経路や履歴を可視化したい場合、または「履歴」「経路」「分岐」「ツリー」「作業フロー」などのキーワードを含むリクエスト時に発動。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Codex** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/context_path_history_visualizer.py` - context_path_history_visualizer.py (Pythonスクリプト)
- `references/design_notes.md` - 概要 - このSkillは、Codexにおける作業履歴や思考経路をツリー構造で記録・可視化し、分岐や合流、編集の流れを直感的に把握できるよう設計されています。履歴はセッションごとに自動抽出され、ユーザーの明示操

## 関連記事

- スキル詳細説明: [Codex 向け context-path-history-visualizer の詳しい説明](https://ai-note.tech/context-path-history-visualizer-codex/)
- 動作手順: [Codex で実際に動かす手順と検証](https://ai-note.tech/context-path-history-visualizer-codex-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/codex/context-path-history-visualizer .agents/skills/context-path-history-visualizer
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/codex/context-path-history-visualizer .agents/skills/context-path-history-visualizer
```

配置後、Codex を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Codex: https://developers.openai.com/codex/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
