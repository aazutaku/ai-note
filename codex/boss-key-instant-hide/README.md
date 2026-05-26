# boss-key-instant-hide

> 作業中に“見られたくない画面”を即座に隠したいとき（例: 上司・親が背後に来た、画面を一瞬で切り替えたい等）、boss-key-instant-hide Skillはワンコマンドでエディタやターミナルを隠し、無難なウィンドウや偽装進捗画面を表示します。キーワード: 画面隠す・一発切替・偽装。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Codex** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/boss_key_instant_hide.py` - boss-key-instant-hide: 一発で画面を隠して偽装画面を表示
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Codex 向け boss-key-instant-hide の詳しい説明](https://ai-note.tech/boss-key-instant-hide-codex/)
- 動作手順: [Codex で実際に動かす手順と検証](https://ai-note.tech/boss-key-instant-hide-codex-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/codex/boss-key-instant-hide .agents/skills/boss-key-instant-hide
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/codex/boss-key-instant-hide .agents/skills/boss-key-instant-hide
```

配置後、Codex を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Codex: https://developers.openai.com/codex/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
