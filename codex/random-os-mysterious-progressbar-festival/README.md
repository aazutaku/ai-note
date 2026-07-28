# random-os-mysterious-progressbar-festival

> Codexは、ユーザーがコマンド実行・ビルド・テスト・保存・実行などの操作を行った際、または「進捗」「バー」「謎」「祭り」などのキーワードを含む文脈で、このSkillを発動してください。複数の意味不明な進捗バーをランダムに描画し、通知・演出カテゴリの体験を提供します。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Codex** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/mysterious_progressbar_festival.py` - 謎のOS進捗バー祭りを発生させるCLIツール
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Codex 向け random-os-mysterious-progressbar-festival の詳しい説明](https://ai-note.tech/random-os-mysterious-progressbar-festival-codex/)
- 動作手順: [Codex で実際に動かす手順と検証](https://ai-note.tech/random-os-mysterious-progressbar-festival-codex-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/codex/random-os-mysterious-progressbar-festival .agents/skills/random-os-mysterious-progressbar-festival
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/codex/random-os-mysterious-progressbar-festival .agents/skills/random-os-mysterious-progressbar-festival
```

配置後、Codex を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Codex: https://developers.openai.com/codex/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
