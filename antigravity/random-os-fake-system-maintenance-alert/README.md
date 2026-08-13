# random-os-fake-system-maintenance-alert

> 作業やコーディング中、Antigravityが「メンテナンス」「保守」「システム通知」などの文脈を検知した際に、現実離れしたカオスなOSメンテナンス予告を自動でランダム表示します。集中力を和らげたい場面や、会議・ペアプロの雰囲気を変えたい時に最適です。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Antigravity** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/random_os_fake_system_maintenance_alert.py` - 謎のOSシステムメンテナンス予告通知をランダム表示するスクリプト
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Antigravity 向け random-os-fake-system-maintenance-alert の詳しい説明](https://ai-note.tech/random-os-fake-system-maintenance-alert-antigravity/)
- 動作手順: [Antigravity で実際に動かす手順と検証](https://ai-note.tech/random-os-fake-system-maintenance-alert-antigravity-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/antigravity/random-os-fake-system-maintenance-alert .agent/skills/random-os-fake-system-maintenance-alert
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/antigravity/random-os-fake-system-maintenance-alert .agent/skills/random-os-fake-system-maintenance-alert
```

配置後、Antigravity を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Antigravity: https://codelabs.developers.google.com/getting-started-with-antigravity-skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
