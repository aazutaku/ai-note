# random-os-fake-software-update-boss-fight

> このSkillは「アップデート」「バグ」「ソフトウェア更新」などの通知・進捗バー・OS演出に関する文脈や、/skills コマンドや random-os-fake-software-update-boss-fight の明示呼び出し時に発動します。開発現場での息抜きや、会話にRPG風の茶番を挟みたい場合に最適です。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Codex** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/os_update_boss_fight.py` - OSソフトウェアアップデート vs バグ魔王 RPGバトル実況スクリプト
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Codex 向け random-os-fake-software-update-boss-fight の詳しい説明](https://ai-note.tech/random-os-fake-software-update-boss-fight-codex/)
- 動作手順: [Codex で実際に動かす手順と検証](https://ai-note.tech/random-os-fake-software-update-boss-fight-codex-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/codex/random-os-fake-software-update-boss-fight .agents/skills/random-os-fake-software-update-boss-fight
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/codex/random-os-fake-software-update-boss-fight .agents/skills/random-os-fake-software-update-boss-fight
```

配置後、Codex を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Codex: https://developers.openai.com/codex/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
