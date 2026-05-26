# terminal-weather-mood-bar

> ターミナルやプロンプト上で開発者の気分やテンションを気象情報風に表示したいとき、またはcommit頻度や作業状況からランダムに気分予報を生成したいときに発動します。キーワード: 気分, 天気, ステータスバー, commit頻度, ターミナル演出。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Claude Code** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/weather_mood_bar.py` - 今日のコミット数を取得
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Claude Code 向け terminal-weather-mood-bar の詳しい説明](https://ai-note.tech/terminal-weather-mood-bar-claude-code/)
- 動作手順: [Claude Code で実際に動かす手順と検証](https://ai-note.tech/terminal-weather-mood-bar-claude-code-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/claude-code/terminal-weather-mood-bar .claude/skills/terminal-weather-mood-bar
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/claude-code/terminal-weather-mood-bar .claude/skills/terminal-weather-mood-bar
```

配置後、Claude Code を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Claude Code: https://code.claude.com/docs/ja/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
