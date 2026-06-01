# boss-key-fake-excel

> 作業中に“バレたくない”コードや画面を即座に隠したいとき、または『Excel作業中』を装いたい瞬間に発動。キーワード: 急な来客、画面切替、フェイク、隠す、ショートカット。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Codex** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/boss_key_fake_excel.py` - boss-key-fake-excel: 急な来客や上司対策に！Excel風フェイク画面表示ツール
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Codex 向け boss-key-fake-excel の詳しい説明](https://ai-note.tech/boss-key-fake-excel-codex/)
- 動作手順: [Codex で実際に動かす手順と検証](https://ai-note.tech/boss-key-fake-excel-codex-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/codex/boss-key-fake-excel .agents/skills/boss-key-fake-excel
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/codex/boss-key-fake-excel .agents/skills/boss-key-fake-excel
```

配置後、Codex を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Codex: https://developers.openai.com/codex/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
