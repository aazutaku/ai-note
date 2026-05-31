# desktop-mood-weather

> デスクトップの片隅に完全ランダムな“気分天気”アイコンを表示したいとき、または「天気」や「気分」「演出」などのキーワードを含む会話や明示呼び出し時に発動します。実際の天気や気分とは無関係な演出が必要な場合に適しています。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Codex** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/desktop_mood_weather.py` - desktop-mood-weather: デスクトップにランダム天気アイコンを表示
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Codex 向け desktop-mood-weather の詳しい説明](https://ai-note.tech/desktop-mood-weather-codex/)
- 動作手順: [Codex で実際に動かす手順と検証](https://ai-note.tech/desktop-mood-weather-codex-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/codex/desktop-mood-weather .agents/skills/desktop-mood-weather
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/codex/desktop-mood-weather .agents/skills/desktop-mood-weather
```

配置後、Codex を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Codex: https://developers.openai.com/codex/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
