# random-os-fake-ai-takeover-alert

> ターミナルやエディタで通常作業中、'AI takeover'や'AIによるOS制御'などのキーワードを含む文脈が検出された際、Antigravityが本Skillを自動発動し、ランダムなタイミングでデスクトップ通知を表示します。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Antigravity** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/random_os_fake_ai_takeover_alert.py` - AI takeover風のOS警告通知をランダムに表示するスクリプト
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Antigravity 向け random-os-fake-ai-takeover-alert の詳しい説明](https://ai-note.tech/random-os-fake-ai-takeover-alert-antigravity/)
- 動作手順: [Antigravity で実際に動かす手順と検証](https://ai-note.tech/random-os-fake-ai-takeover-alert-antigravity-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/antigravity/random-os-fake-ai-takeover-alert .agent/skills/random-os-fake-ai-takeover-alert
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/antigravity/random-os-fake-ai-takeover-alert .agent/skills/random-os-fake-ai-takeover-alert
```

配置後、Antigravity を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Antigravity: https://codelabs.developers.google.com/getting-started-with-antigravity-skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
