# mysterious-os-mood-bar

> ユーザーがターミナルでコマンドを実行するたびに、コマンド内容や長さ、git statusの雰囲気などから気分温度ややる気指数を適当に判定し、OSのメニューバーやステータスバーにランダムな気分ワードや温度を表示するSkillです。"気分"や"やる気"などのキーワードや、コマンド実行時に自動発動します。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Antigravity** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/mood_bar.py` - Mysterious OS Mood Bar
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Antigravity 向け mysterious-os-mood-bar の詳しい説明](https://ai-note.tech/mysterious-os-mood-bar-antigravity/)
- 動作手順: [Antigravity で実際に動かす手順と検証](https://ai-note.tech/mysterious-os-mood-bar-antigravity-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/antigravity/mysterious-os-mood-bar .agent/skills/mysterious-os-mood-bar
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/antigravity/mysterious-os-mood-bar .agent/skills/mysterious-os-mood-bar
```

配置後、Antigravity を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Antigravity: https://codelabs.developers.google.com/getting-started-with-antigravity-skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
