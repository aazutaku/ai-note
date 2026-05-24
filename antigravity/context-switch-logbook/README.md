# context-switch-logbook

> エージェントや作業ブランチの切り替え時、"切り替え元・切り替え先・理由"を自動ログするSkillです。"エージェント切り替え"や"タスク移動"などのキーワード検出時に発動します。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Antigravity** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/timeline_logger.py` - 実行スクリプト
- `references/design_notes.md` - 参考資料

## 関連記事

- スキル詳細説明: [Antigravity 向け context-switch-logbook の詳しい説明](https://ai-note.tech/context-switch-logbook-antigravity/)
- 動作手順: [Antigravity で実際に動かす手順と検証](https://ai-note.tech/context-switch-logbook-antigravity-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/antigravity/context-switch-logbook .agent/skills/context-switch-logbook
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/antigravity/context-switch-logbook .agent/skills/context-switch-logbook
```

配置後、Antigravity を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Antigravity: https://codelabs.developers.google.com/getting-started-with-antigravity-skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
