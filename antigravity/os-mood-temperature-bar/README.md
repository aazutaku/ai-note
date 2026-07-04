# os-mood-temperature-bar

> ターミナルやエディタでコマンド実行時、作業テンションを“気分温度”としてOSのステータスバーやターミナルバー風にランダム表示したい時に発動。気分や作業状況を可視化したい、ちょっとした演出や息抜きが必要な場面で自動発動します。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Antigravity** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/os_mood_temperature_bar.py` - os-mood-temperature-bar: 気分温度をランダム表示＆ログ
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Antigravity 向け os-mood-temperature-bar の詳しい説明](https://ai-note.tech/os-mood-temperature-bar-antigravity/)
- 動作手順: [Antigravity で実際に動かす手順と検証](https://ai-note.tech/os-mood-temperature-bar-antigravity-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/antigravity/os-mood-temperature-bar .agent/skills/os-mood-temperature-bar
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/antigravity/os-mood-temperature-bar .agent/skills/os-mood-temperature-bar
```

配置後、Antigravity を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Antigravity: https://codelabs.developers.google.com/getting-started-with-antigravity-skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
