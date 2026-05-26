# terminal-weather-mood-bar

> ターミナルやプロンプト上で開発者の気分やテンションを、気温や天気に見立てて表示したい場合に発動します。commit頻度や作業状況の変化、/skills menuやterminal-weather-mood-barの明示呼び出し時に適用されます。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Codex** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/weather_mood_bar.py` - terminal-weather-mood-bar: 気分やテンションを天気・気温風に表示するツール
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Codex 向け terminal-weather-mood-bar の詳しい説明](https://ai-note.tech/terminal-weather-mood-bar-codex/)
- 動作手順: [Codex で実際に動かす手順と検証](https://ai-note.tech/terminal-weather-mood-bar-codex-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/codex/terminal-weather-mood-bar .agents/skills/terminal-weather-mood-bar
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/codex/terminal-weather-mood-bar .agents/skills/terminal-weather-mood-bar
```

配置後、Codex を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Codex: https://developers.openai.com/codex/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
