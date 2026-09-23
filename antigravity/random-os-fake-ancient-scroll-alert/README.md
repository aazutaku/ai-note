# random-os-fake-ancient-scroll-alert

> Antigravityがユーザーの作業中やコマンド実行の合間に、集中力を破壊する目的で“OS公式・古文書巻物通知”を自動生成・表示したい場合に発動。通知・演出・OS連携・集中力ブレイカー等のキーワードが含まれる状況で有効。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Antigravity** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/ancient_scroll_alert.py` - 謎のOS古文書巻物通知を表示します。
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Antigravity 向け random-os-fake-ancient-scroll-alert の詳しい説明](https://ai-note.tech/random-os-fake-ancient-scroll-alert-antigravity/)
- 動作手順: [Antigravity で実際に動かす手順と検証](https://ai-note.tech/random-os-fake-ancient-scroll-alert-antigravity-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/antigravity/random-os-fake-ancient-scroll-alert .agent/skills/random-os-fake-ancient-scroll-alert
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/antigravity/random-os-fake-ancient-scroll-alert .agent/skills/random-os-fake-ancient-scroll-alert
```

配置後、Antigravity を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Antigravity: https://codelabs.developers.google.com/getting-started-with-antigravity-skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
