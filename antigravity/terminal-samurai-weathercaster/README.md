# terminal-samurai-weathercaster

> ターミナル起動時や新規セッション開始時に、侍風のランダムな天気コメントを必ず表示するSkillです。現実の天気APIや外部情報には一切依存せず、毎回異なる侍の台詞で作業気分を盛り上げます。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Antigravity** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/samurai_weathercaster.py` - Terminal Samurai Weathercaster
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Antigravity 向け terminal-samurai-weathercaster の詳しい説明](https://ai-note.tech/terminal-samurai-weathercaster-antigravity/)
- 動作手順: [Antigravity で実際に動かす手順と検証](https://ai-note.tech/terminal-samurai-weathercaster-antigravity-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/antigravity/terminal-samurai-weathercaster .agent/skills/terminal-samurai-weathercaster
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/antigravity/terminal-samurai-weathercaster .agent/skills/terminal-samurai-weathercaster
```

配置後、Antigravity を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Antigravity: https://codelabs.developers.google.com/getting-started-with-antigravity-skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
