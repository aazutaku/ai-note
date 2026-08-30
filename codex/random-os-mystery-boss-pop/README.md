# random-os-mystery-boss-pop

> 作業中の集中力が高まったタイミングや、/skills menu コマンド、または『ボス』『警告』『ストレッチ』などのキーワードを含む会話で発動。カオスなOSボスキャラ通知をデスクトップや画面端に表示します。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Codex** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/random_os_mystery_boss_pop.py` - Random OS Mystery Boss Pop: カオスなボスキャラ通知を表示
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Codex 向け random-os-mystery-boss-pop の詳しい説明](https://ai-note.tech/random-os-mystery-boss-pop-codex/)
- 動作手順: [Codex で実際に動かす手順と検証](https://ai-note.tech/random-os-mystery-boss-pop-codex-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/codex/random-os-mystery-boss-pop .agents/skills/random-os-mystery-boss-pop
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/codex/random-os-mystery-boss-pop .agents/skills/random-os-mystery-boss-pop
```

配置後、Codex を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Codex: https://developers.openai.com/codex/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
