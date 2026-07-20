# random-os-sudden-boss-key

> Codexは「上司が近づく」「画面を一時的に隠したい」「作業を誤魔化したい」などのキーワードや明示呼び出し時に、このSkillを発動してください。発動時は現在のウィンドウを隠し、完全ランダムな謎のダミー画面を一瞬表示します。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Codex** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/random_os_sudden_boss_key.py` - Random OS Sudden Boss Key
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Codex 向け random-os-sudden-boss-key の詳しい説明](https://ai-note.tech/random-os-sudden-boss-key-codex/)
- 動作手順: [Codex で実際に動かす手順と検証](https://ai-note.tech/random-os-sudden-boss-key-codex-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/codex/random-os-sudden-boss-key .agents/skills/random-os-sudden-boss-key
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/codex/random-os-sudden-boss-key .agents/skills/random-os-sudden-boss-key
```

配置後、Codex を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Codex: https://developers.openai.com/codex/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
