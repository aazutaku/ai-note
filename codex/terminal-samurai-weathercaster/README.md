# terminal-samurai-weathercaster

> ターミナル起動時や /skills menu、terminal-samurai-weathercaster の明示呼び出し時に発動。天気APIや現実の天候参照は一切せず、毎回異なる侍風コメントをランダム生成し、作業開始気分を演出する際に利用。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Codex** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/samurai_weathercaster.py` - Terminal Samurai Weathercaster: 侍が気分で天気予報を斬り捨てる演出スクリプト
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Codex 向け terminal-samurai-weathercaster の詳しい説明](https://ai-note.tech/terminal-samurai-weathercaster-codex/)
- 動作手順: [Codex で実際に動かす手順と検証](https://ai-note.tech/terminal-samurai-weathercaster-codex-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/codex/terminal-samurai-weathercaster .agents/skills/terminal-samurai-weathercaster
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/codex/terminal-samurai-weathercaster .agents/skills/terminal-samurai-weathercaster
```

配置後、Codex を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Codex: https://developers.openai.com/codex/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
