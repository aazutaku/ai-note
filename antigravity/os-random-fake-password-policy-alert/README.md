# os-random-fake-password-policy-alert

> 開発現場や運用時に“パスワード”や“ポリシー”に関連する会話・コマンド・ドキュメント編集が認識された際、Antigravityが自動的に理不尽な偽パスワードポリシー通知を表示し、現場の緊張感を和ませます。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Antigravity** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/fake_password_policy_alert.py` - OSランダム偽パスワードポリシー通知スクリプト
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Antigravity 向け os-random-fake-password-policy-alert の詳しい説明](https://ai-note.tech/os-random-fake-password-policy-alert-antigravity/)
- 動作手順: [Antigravity で実際に動かす手順と検証](https://ai-note.tech/os-random-fake-password-policy-alert-antigravity-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/antigravity/os-random-fake-password-policy-alert .agent/skills/os-random-fake-password-policy-alert
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/antigravity/os-random-fake-password-policy-alert .agent/skills/os-random-fake-password-policy-alert
```

配置後、Antigravity を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Antigravity: https://codelabs.developers.google.com/getting-started-with-antigravity-skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
