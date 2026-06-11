# random-os-startup-movie

> ターミナルやエディタの起動・再起動・新規ウィンドウ作成時など、セッションの開始を検知した際に発動します。キーワード: 起動, スタートアップ, セッション開始, ターミナル, エディタ。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Antigravity** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/random_os_startup_movie.py` - random-os-startup-movie: 毎回違う架空OS起動画面を演出
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Antigravity 向け random-os-startup-movie の詳しい説明](https://ai-note.tech/random-os-startup-movie-antigravity/)
- 動作手順: [Antigravity で実際に動かす手順と検証](https://ai-note.tech/random-os-startup-movie-antigravity-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/antigravity/random-os-startup-movie .agent/skills/random-os-startup-movie
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/antigravity/random-os-startup-movie .agent/skills/random-os-startup-movie
```

配置後、Antigravity を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Antigravity: https://codelabs.developers.google.com/getting-started-with-antigravity-skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
