# shindan-file-cupid

> Codexがプロジェクト内のファイル名リストから、ファイル同士の『相性診断』や『おすすめペア』を求められた際、または「ファイルの相性」「おすすめペア」などのキーワードが会話に含まれる場合に発動します。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Codex** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/file_cupid.py` - プロジェクト内のファイル相性診断 (shindan-file-cupid)
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Codex 向け shindan-file-cupid の詳しい説明](https://ai-note.tech/shindan-file-cupid-codex/)
- 動作手順: [Codex で実際に動かす手順と検証](https://ai-note.tech/shindan-file-cupid-codex-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/codex/shindan-file-cupid .agents/skills/shindan-file-cupid
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/codex/shindan-file-cupid .agents/skills/shindan-file-cupid
```

配置後、Codex を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Codex: https://developers.openai.com/codex/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
