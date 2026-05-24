# context-switch-logbook

> 作業エージェントやタスクの切り替え時（例: agent switch, branch change, context shift, task jump）に発動し、切り替え元・先・理由を記録するSkillです。明示的な呼び出しや、切り替え関連のキーワード検出時に自動発動します。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Codex** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/context_switch_logbook.py` - 実行スクリプト
- `references/design_notes.md` - 参考資料

## 関連記事

- スキル詳細説明: [Codex 向け context-switch-logbook の詳しい説明](https://ai-note.tech/context-switch-logbook-codex/)
- 動作手順: [Codex で実際に動かす手順と検証](https://ai-note.tech/context-switch-logbook-codex-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/codex/context-switch-logbook .agents/skills/context-switch-logbook
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/codex/context-switch-logbook .agents/skills/context-switch-logbook
```

配置後、Codex を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Codex: https://developers.openai.com/codex/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
