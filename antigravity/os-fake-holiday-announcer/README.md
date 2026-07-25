# os-fake-holiday-announcer

> 開発者が作業中に「休み」「休日」「バグ記念日」「OS都合」などのキーワードを含む状況や、長時間の連続作業・作業のマンネリ感が検出された場合に発動。ユーザーの集中力維持や気分転換を目的とし、実害のない“架空のOS休日通知”をランダムに表示します。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Antigravity** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/os_fake_holiday_announcer.py` - OS Fake Holiday Announcer
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Antigravity 向け os-fake-holiday-announcer の詳しい説明](https://ai-note.tech/os-fake-holiday-announcer-antigravity/)
- 動作手順: [Antigravity で実際に動かす手順と検証](https://ai-note.tech/os-fake-holiday-announcer-antigravity-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/antigravity/os-fake-holiday-announcer .agent/skills/os-fake-holiday-announcer
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/antigravity/os-fake-holiday-announcer .agent/skills/os-fake-holiday-announcer
```

配置後、Antigravity を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Antigravity: https://codelabs.developers.google.com/getting-started-with-antigravity-skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
