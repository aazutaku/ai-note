# context-switch-notes

> タスクやプロジェクトの切り替え時（プロンプトや作業対象の変更、/skills menuやcontext-switch-notesの明示呼び出し時）に自動で直前のメモや要約を記録・復元する際に発動します。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Codex** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/context_switch_notes.py` - 実行スクリプト
- `references/design_notes.md` - 参考資料

## 関連記事

- スキル詳細説明: [Codex 向け context-switch-notes の詳しい説明](https://ai-note.tech/context-switch-notes-codex/)
- 動作手順: [Codex で実際に動かす手順と検証](https://ai-note.tech/context-switch-notes-codex-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/codex/context-switch-notes .agents/skills/context-switch-notes
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/codex/context-switch-notes .agents/skills/context-switch-notes
```

配置後、Codex を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Codex: https://developers.openai.com/codex/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
