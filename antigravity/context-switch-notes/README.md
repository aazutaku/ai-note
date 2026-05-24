# context-switch-notes

> タスクやプロンプト、作業対象の切り替えが発生した際に自動で発動。直前の作業内容や思考メモを保存・要約し、次回同じコンテキストに戻った際に自動表示。trigger: semantic-match-only, context, switch, prompt, project, task, note, resume, save, restore。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Antigravity** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/context_switch_notes.py` - 実行スクリプト
- `references/design_notes.md` - 参考資料

## 関連記事

- スキル詳細説明: [Antigravity 向け context-switch-notes の詳しい説明](https://ai-note.tech/context-switch-notes-antigravity/)
- 動作手順: [Antigravity で実際に動かす手順と検証](https://ai-note.tech/context-switch-notes-antigravity-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/antigravity/context-switch-notes .agent/skills/context-switch-notes
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/antigravity/context-switch-notes .agent/skills/context-switch-notes
```

配置後、Antigravity を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Antigravity: https://codelabs.developers.google.com/getting-started-with-antigravity-skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
