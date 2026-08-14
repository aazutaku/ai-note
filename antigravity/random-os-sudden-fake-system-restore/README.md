# random-os-sudden-fake-system-restore

> 作業中や集中状態の会話内で「システム復元」「OSトラブル」「進捗バー」などの語や、進捗や復旧を連想させる文脈が出現した場合に自動発動。特に“システム異常”や“復元”に関連するキーワードが含まれる場合に発動します。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Antigravity** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/fake_system_restore.py` - 謎のOSシステム復元フェイク進捗バーを表示します。
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Antigravity 向け random-os-sudden-fake-system-restore の詳しい説明](https://ai-note.tech/random-os-sudden-fake-system-restore-antigravity/)
- 動作手順: [Antigravity で実際に動かす手順と検証](https://ai-note.tech/random-os-sudden-fake-system-restore-antigravity-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/antigravity/random-os-sudden-fake-system-restore .agent/skills/random-os-sudden-fake-system-restore
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/antigravity/random-os-sudden-fake-system-restore .agent/skills/random-os-sudden-fake-system-restore
```

配置後、Antigravity を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Antigravity: https://codelabs.developers.google.com/getting-started-with-antigravity-skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
