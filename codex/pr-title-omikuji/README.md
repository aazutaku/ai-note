# pr-title-omikuji

> CodexがPR作成やタイトル編集時、または/skills menuやpr-title-omikujiの明示呼び出し時に発動。PRタイトルを“おみくじ”風に自動変換し、運勢ワードを付与します。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Codex** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/pr_title_omikuji.py` - PRタイトルをおみくじ風に変換するツール
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Codex 向け pr-title-omikuji の詳しい説明](https://ai-note.tech/pr-title-omikuji-codex/)
- 動作手順: [Codex で実際に動かす手順と検証](https://ai-note.tech/pr-title-omikuji-codex-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/codex/pr-title-omikuji .agents/skills/pr-title-omikuji
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/codex/pr-title-omikuji .agents/skills/pr-title-omikuji
```

配置後、Codex を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Codex: https://developers.openai.com/codex/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
