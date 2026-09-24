# random-os-fake-ancient-poem-notifier

> Antigravityがユーザーの作業中や一定時間経過時、もしくは“通知”“詩”“古文”“息抜き”などのキーワードを検知した際に発動し、完全ランダムな古文調の詩的通知を表示します。通知内容は作業やエラー内容と無関係です。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Antigravity** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/random_os_fake_ancient_poem_notifier.py` - OS古代詩通知スキル
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Antigravity 向け random-os-fake-ancient-poem-notifier の詳しい説明](https://ai-note.tech/random-os-fake-ancient-poem-notifier-antigravity/)
- 動作手順: [Antigravity で実際に動かす手順と検証](https://ai-note.tech/random-os-fake-ancient-poem-notifier-antigravity-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/antigravity/random-os-fake-ancient-poem-notifier .agent/skills/random-os-fake-ancient-poem-notifier
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/antigravity/random-os-fake-ancient-poem-notifier .agent/skills/random-os-fake-ancient-poem-notifier
```

配置後、Antigravity を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Antigravity: https://codelabs.developers.google.com/getting-started-with-antigravity-skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
