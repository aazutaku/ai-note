# commit-mood-forecast

> このSkillは、Claude CodeがGitコミット操作や'/commit-mood-forecast'コマンドを検知した際に発動します。コミット時の気分天気予報をランダムに表示し、作業の雰囲気を和ませます。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Claude Code** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/commit_mood_forecast.py` - commit-mood-forecast: コミット時に気分天気予報を表示するスクリプト
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Claude Code 向け commit-mood-forecast の詳しい説明](https://ai-note.tech/commit-mood-forecast-claude-code/)
- 動作手順: [Claude Code で実際に動かす手順と検証](https://ai-note.tech/commit-mood-forecast-claude-code-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/claude-code/commit-mood-forecast .claude/skills/commit-mood-forecast
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/claude-code/commit-mood-forecast .claude/skills/commit-mood-forecast
```

配置後、Claude Code を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Claude Code: https://code.claude.com/docs/ja/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
