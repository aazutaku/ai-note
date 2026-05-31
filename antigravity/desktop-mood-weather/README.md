# desktop-mood-weather

> デスクトップ上に完全ランダムな天気アイコンを表示することで、作業気分や実際の天気とは無関係な“気分天気”を演出します。画面端での理不尽な天気変化を楽しみたい、または会議や作業中にちょっとしたカオスを加えたい場合に自動発動します。キーワード例: デスクトップ通知, 天気, 気分, ランダム, アイコン表示。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Antigravity** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/desktop_mood_weather.py` - 簡易的な天気アイコンをPillowで生成し保存
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Antigravity 向け desktop-mood-weather の詳しい説明](https://ai-note.tech/desktop-mood-weather-antigravity/)
- 動作手順: [Antigravity で実際に動かす手順と検証](https://ai-note.tech/desktop-mood-weather-antigravity-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/antigravity/desktop-mood-weather .agent/skills/desktop-mood-weather
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/antigravity/desktop-mood-weather .agent/skills/desktop-mood-weather
```

配置後、Antigravity を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Antigravity: https://codelabs.developers.google.com/getting-started-with-antigravity-skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
