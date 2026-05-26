# terminal-weather-mood-bar

> ターミナルバーやプロンプトに「気分天気」を表示する必要がある場合に発動します。キーワード例: 気分, テンション, 天気, commit頻度, ステータスバー, 開発者の癒し, 自己分析。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Antigravity** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/terminal_weather_mood_bar.py` - terminal-weather-mood-bar: 気分天気をターミナルバーに表示
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Antigravity 向け terminal-weather-mood-bar の詳しい説明](https://ai-note.tech/terminal-weather-mood-bar-antigravity/)
- 動作手順: [Antigravity で実際に動かす手順と検証](https://ai-note.tech/terminal-weather-mood-bar-antigravity-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/antigravity/terminal-weather-mood-bar .agent/skills/terminal-weather-mood-bar
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/antigravity/terminal-weather-mood-bar .agent/skills/terminal-weather-mood-bar
```

配置後、Antigravity を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Antigravity: https://codelabs.developers.google.com/getting-started-with-antigravity-skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
