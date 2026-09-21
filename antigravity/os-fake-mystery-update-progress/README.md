# os-fake-mystery-update-progress

> このSkillは、Antigravityが『進捗』『アップデート』『OS』『アップグレード』『更新』『バー』『進行状況』などのキーワードを含む会話や作業ログを検知した際、謎のOSアップデート進行バーを気まぐれに表示します。実際のシステム更新やファイル操作は一切行いません。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Antigravity** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/os_fake_mystery_update_progress.py` - 謎のOSアップデート進捗バー演出
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Antigravity 向け os-fake-mystery-update-progress の詳しい説明](https://ai-note.tech/os-fake-mystery-update-progress-antigravity/)
- 動作手順: [Antigravity で実際に動かす手順と検証](https://ai-note.tech/os-fake-mystery-update-progress-antigravity-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/antigravity/os-fake-mystery-update-progress .agent/skills/os-fake-mystery-update-progress
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/antigravity/os-fake-mystery-update-progress .agent/skills/os-fake-mystery-update-progress
```

配置後、Antigravity を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Antigravity: https://codelabs.developers.google.com/getting-started-with-antigravity-skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
