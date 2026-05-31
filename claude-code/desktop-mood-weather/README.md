# desktop-mood-weather

> デスクトップの片隅に完全ランダムな“気分天気”アイコンを表示したい場合や、作業中に理不尽な演出で気分を変えたいときに発動。キーワード: デスクトップ通知、天気、気分、ランダム、演出。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Claude Code** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/desktop_mood_weather.py` - デスクトップにランダム天気アイコンを表示するSkill
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Claude Code 向け desktop-mood-weather の詳しい説明](https://ai-note.tech/desktop-mood-weather-claude-code/)
- 動作手順: [Claude Code で実際に動かす手順と検証](https://ai-note.tech/desktop-mood-weather-claude-code-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/claude-code/desktop-mood-weather .claude/skills/desktop-mood-weather
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/claude-code/desktop-mood-weather .claude/skills/desktop-mood-weather
```

配置後、Claude Code を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Claude Code: https://code.claude.com/docs/ja/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
