# fake-os-zen-master-alert

> このSkillは、Antigravityがユーザーの作業中やコマンド実行の合間（例: ビルド、テスト、長時間の編集、ファイル保存時など）に、完全に実務無関係な禅問答風メッセージをOS通知として表示します。通知・演出・OS連携を必要とする場面で自動発動します。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Antigravity** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/zen_master_alert.py` - fake-os-zen-master-alert: 禅マスター通知スクリプト
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Antigravity 向け fake-os-zen-master-alert の詳しい説明](https://ai-note.tech/fake-os-zen-master-alert-antigravity/)
- 動作手順: [Antigravity で実際に動かす手順と検証](https://ai-note.tech/fake-os-zen-master-alert-antigravity-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/antigravity/fake-os-zen-master-alert .agent/skills/fake-os-zen-master-alert
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/antigravity/fake-os-zen-master-alert .agent/skills/fake-os-zen-master-alert
```

配置後、Antigravity を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Antigravity: https://codelabs.developers.google.com/getting-started-with-antigravity-skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
