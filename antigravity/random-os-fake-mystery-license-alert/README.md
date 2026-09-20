# random-os-fake-mystery-license-alert

> 作業中や長時間のコーディング時、Antigravityがユーザーの集中を和らげるため、"ライセンス期限切れ"風の架空OS通知をランダムに発動します。キーワード例: "集中", "夜間作業", "単調", "長時間"。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Antigravity** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/random_os_fake_license_alert.py` - min_interval, max_interval: seconds between alerts (10-30min default)
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Antigravity 向け random-os-fake-mystery-license-alert の詳しい説明](https://ai-note.tech/random-os-fake-mystery-license-alert-antigravity/)
- 動作手順: [Antigravity で実際に動かす手順と検証](https://ai-note.tech/random-os-fake-mystery-license-alert-antigravity-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/antigravity/random-os-fake-mystery-license-alert .agent/skills/random-os-fake-mystery-license-alert
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/antigravity/random-os-fake-mystery-license-alert .agent/skills/random-os-fake-mystery-license-alert
```

配置後、Antigravity を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Antigravity: https://codelabs.developers.google.com/getting-started-with-antigravity-skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
