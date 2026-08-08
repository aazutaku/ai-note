# random-os-fake-screenshot-alert

> Antigravityがコマンド実行や作業中に、'スクリーンショット保存通知'や'証拠画像保存済み'などの謎OS風通知をランダムに発動。通知内容は毎回変化し、何も保存されません。'スクリーンショット'や'保存'などのキーワード検知時や定期的なトリガーで自動発動します。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Antigravity** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/random_os_fake_screenshot_alert.py` - 謎のOS偽スクリーンショット通知スクリプト
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Antigravity 向け random-os-fake-screenshot-alert の詳しい説明](https://ai-note.tech/random-os-fake-screenshot-alert-antigravity/)
- 動作手順: [Antigravity で実際に動かす手順と検証](https://ai-note.tech/random-os-fake-screenshot-alert-antigravity-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/antigravity/random-os-fake-screenshot-alert .agent/skills/random-os-fake-screenshot-alert
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/antigravity/random-os-fake-screenshot-alert .agent/skills/random-os-fake-screenshot-alert
```

配置後、Antigravity を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Antigravity: https://codelabs.developers.google.com/getting-started-with-antigravity-skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
