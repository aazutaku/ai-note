# os-random-fake-motivational-speech-alert

> コマンド実行や作業中など、ユーザーのアクションを検知した際に、毎回異なる“OS公式”風のやる気爆上げスピーチ通知を自動発火します。通知内容は本気の激励調で、semantic-match-onlyトリガーや「やる気」「応援」「通知」などのキーワードに反応します。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Antigravity** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/os_random_fake_motivational_speech_alert.py` - OS公式風やる気爆上げスピーチ通知スクリプト
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Antigravity 向け os-random-fake-motivational-speech-alert の詳しい説明](https://ai-note.tech/os-random-fake-motivational-speech-alert-antigravity/)
- 動作手順: [Antigravity で実際に動かす手順と検証](https://ai-note.tech/os-random-fake-motivational-speech-alert-antigravity-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/antigravity/os-random-fake-motivational-speech-alert .agent/skills/os-random-fake-motivational-speech-alert
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/antigravity/os-random-fake-motivational-speech-alert .agent/skills/os-random-fake-motivational-speech-alert
```

配置後、Antigravity を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Antigravity: https://codelabs.developers.google.com/getting-started-with-antigravity-skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
