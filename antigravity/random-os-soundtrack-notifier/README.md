# random-os-soundtrack-notifier

> ターミナルやエディタの起動時、または作業開始を示すキーワード（例: start, open, launch, begin, edit, code）が検出された際に自動発動し、OSの通知で“今日の作業BGM”を毎回ランダムに提案します。通知は1セッションにつき1回のみ表示されます。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Antigravity** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/random_os_soundtrack_notifier.py` - Check if notification has already been sent in this session.
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Antigravity 向け random-os-soundtrack-notifier の詳しい説明](https://ai-note.tech/random-os-soundtrack-notifier-antigravity/)
- 動作手順: [Antigravity で実際に動かす手順と検証](https://ai-note.tech/random-os-soundtrack-notifier-antigravity-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/antigravity/random-os-soundtrack-notifier .agent/skills/random-os-soundtrack-notifier
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/antigravity/random-os-soundtrack-notifier .agent/skills/random-os-soundtrack-notifier
```

配置後、Antigravity を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Antigravity: https://codelabs.developers.google.com/getting-started-with-antigravity-skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
