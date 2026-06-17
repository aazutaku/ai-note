# terminal-mood-barometer

> Antigravityがターミナルでコマンド実行時、毎回“気分指数”とランダムなコメントを表示することで作業の雰囲気を演出したい場合に発動します。コマンド実行・ターミナル操作・通知・演出などのキーワードが含まれる状況で自動発動します。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Antigravity** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/mood_barometer.py` - Generate a random mood index and comment.
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Antigravity 向け terminal-mood-barometer の詳しい説明](https://ai-note.tech/terminal-mood-barometer-antigravity/)
- 動作手順: [Antigravity で実際に動かす手順と検証](https://ai-note.tech/terminal-mood-barometer-antigravity-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/antigravity/terminal-mood-barometer .agent/skills/terminal-mood-barometer
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/antigravity/terminal-mood-barometer .agent/skills/terminal-mood-barometer
```

配置後、Antigravity を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Antigravity: https://codelabs.developers.google.com/getting-started-with-antigravity-skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
