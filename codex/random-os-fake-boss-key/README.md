# random-os-fake-boss-key

> 作業中に“ボスが来た”風の緊急演出を即座に起動したい場合や、上司接近・監督キーワード（例:『上司』『監督』『見られる』）を検知した際に、偽の業務画面をランダム生成して切り替える必要がある場合に発動します。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Codex** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/fake_boss_key.py` - random-os-fake-boss-key: ダミー業務画面を即座に表示
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Codex 向け random-os-fake-boss-key の詳しい説明](https://ai-note.tech/random-os-fake-boss-key-codex/)
- 動作手順: [Codex で実際に動かす手順と検証](https://ai-note.tech/random-os-fake-boss-key-codex-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/codex/random-os-fake-boss-key .agents/skills/random-os-fake-boss-key
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/codex/random-os-fake-boss-key .agents/skills/random-os-fake-boss-key
```

配置後、Codex を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Codex: https://developers.openai.com/codex/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
