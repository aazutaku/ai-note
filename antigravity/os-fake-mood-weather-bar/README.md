# os-fake-mood-weather-bar

> Antigravityが「気分」「天気」「集中力」「やる気」などのワードや、作業進捗・休憩提案・気分転換に関する文脈を検知した際、自動的に“謎の気分天気バー”を画面端やメニューバーに表示します。通知・演出系Skillと重複しないよう注意しつつ、主に作業中やコード実行時に発動します。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Antigravity** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/os_fake_mood_weather_bar.py` - OS風・謎の気分天気バー
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Antigravity 向け os-fake-mood-weather-bar の詳しい説明](https://ai-note.tech/os-fake-mood-weather-bar-antigravity/)
- 動作手順: [Antigravity で実際に動かす手順と検証](https://ai-note.tech/os-fake-mood-weather-bar-antigravity-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/antigravity/os-fake-mood-weather-bar .agent/skills/os-fake-mood-weather-bar
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/antigravity/os-fake-mood-weather-bar .agent/skills/os-fake-mood-weather-bar
```

配置後、Antigravity を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Antigravity: https://codelabs.developers.google.com/getting-started-with-antigravity-skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
