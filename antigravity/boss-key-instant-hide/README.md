# boss-key-instant-hide

> 作業中に“上司が来た”“親が部屋に入ってきた”などの状況で、Antigravityが『画面を即座に隠す』『無難なウィンドウに切り替える』などのキーワードを検知した際に発動します。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Antigravity** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/boss_key_instant_hide.py` - boss-key-instant-hide: 一発で画面を隠し偽装ウィンドウを表示
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Antigravity 向け boss-key-instant-hide の詳しい説明](https://ai-note.tech/boss-key-instant-hide-antigravity/)
- 動作手順: [Antigravity で実際に動かす手順と検証](https://ai-note.tech/boss-key-instant-hide-antigravity-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/antigravity/boss-key-instant-hide .agent/skills/boss-key-instant-hide
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/antigravity/boss-key-instant-hide .agent/skills/boss-key-instant-hide
```

配置後、Antigravity を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Antigravity: https://codelabs.developers.google.com/getting-started-with-antigravity-skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
