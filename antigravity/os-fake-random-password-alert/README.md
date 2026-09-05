# os-fake-random-password-alert

> このSkillは、コマンド実行や作業時などの『通知』『警告』『パスワード』『流出』『セキュリティ』『alert』『警告メッセージ』などのキーワードや状況を検知した際、ランダムな偽パスワード流出警告をデスクトップ通知で発動します。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Antigravity** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/os_fake_random_password_alert.py` - OS Fake Random Password Alert Skill
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Antigravity 向け os-fake-random-password-alert の詳しい説明](https://ai-note.tech/os-fake-random-password-alert-antigravity/)
- 動作手順: [Antigravity で実際に動かす手順と検証](https://ai-note.tech/os-fake-random-password-alert-antigravity-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/antigravity/os-fake-random-password-alert .agent/skills/os-fake-random-password-alert
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/antigravity/os-fake-random-password-alert .agent/skills/os-fake-random-password-alert
```

配置後、Antigravity を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Antigravity: https://codelabs.developers.google.com/getting-started-with-antigravity-skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
