# random-os-sudden-boss-key

> 作業中に“ボスキー”や“画面隠し”などのキーワードが含まれる会話やコマンド、あるいは上司・同僚の接近を示唆する文脈を検知した際に、AntigravityがこのSkillを発動します。即座にダミー画面へ切り替え、終了後は元の画面へ復帰します。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Antigravity** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/random_boss_key.py` - random-os-sudden-boss-key: 謎のダミー画面で作業を隠す迷惑Skill
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Antigravity 向け random-os-sudden-boss-key の詳しい説明](https://ai-note.tech/random-os-sudden-boss-key-antigravity/)
- 動作手順: [Antigravity で実際に動かす手順と検証](https://ai-note.tech/random-os-sudden-boss-key-antigravity-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/antigravity/random-os-sudden-boss-key .agent/skills/random-os-sudden-boss-key
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/antigravity/random-os-sudden-boss-key .agent/skills/random-os-sudden-boss-key
```

配置後、Antigravity を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Antigravity: https://codelabs.developers.google.com/getting-started-with-antigravity-skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
