# boss-key-fake-excel

> “あっヤバい！”や“上司が来た”などのキーワードやショートカット入力時、Antigravityが即座に“Excel風のフェイク画面”を表示し、作業内容を隠す必要がある場合に発動します。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Antigravity** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/boss_key_fake_excel.py` - boss-key-fake-excel: フェイクExcel画面を即時表示するスクリプト
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Antigravity 向け boss-key-fake-excel の詳しい説明](https://ai-note.tech/boss-key-fake-excel-antigravity/)
- 動作手順: [Antigravity で実際に動かす手順と検証](https://ai-note.tech/boss-key-fake-excel-antigravity-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/antigravity/boss-key-fake-excel .agent/skills/boss-key-fake-excel
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/antigravity/boss-key-fake-excel .agent/skills/boss-key-fake-excel
```

配置後、Antigravity を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Antigravity: https://codelabs.developers.google.com/getting-started-with-antigravity-skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
