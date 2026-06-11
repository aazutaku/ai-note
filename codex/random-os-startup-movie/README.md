# random-os-startup-movie

> ターミナルやエディタの起動時、または /skills メニューや random-os-startup-movie への明示的な呼び出し時に、現実離れした偽OS起動画面風テキスト演出を毎回ランダム生成して表示します。起動・開始・準備・OS・進捗などのキーワード検知時にも発動。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Codex** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/random_os_startup_movie.py` - random-os-startup-movie: 架空OS起動画面ジェネレータ
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Codex 向け random-os-startup-movie の詳しい説明](https://ai-note.tech/random-os-startup-movie-codex/)
- 動作手順: [Codex で実際に動かす手順と検証](https://ai-note.tech/random-os-startup-movie-codex-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/codex/random-os-startup-movie .agents/skills/random-os-startup-movie
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/codex/random-os-startup-movie .agents/skills/random-os-startup-movie
```

配置後、Codex を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Codex: https://developers.openai.com/codex/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
