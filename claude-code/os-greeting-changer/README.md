# os-greeting-changer

> ターミナルやコンソールを開いた際、または「起動」「OS」「ログイン」などのキーワードを含むプロンプトや明示的な /os-greeting-changer 呼び出し時に、現実には存在しない“偽OS起動メッセージ”を毎回ランダムに表示します。作業開始時の気分転換や遊び心を演出したい場合に自動発動します。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Claude Code** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/os_greeting_changer.py` - ターミナル起動時に偽OS起動メッセージをランダム表示するスキル
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Claude Code 向け os-greeting-changer の詳しい説明](https://ai-note.tech/os-greeting-changer-claude-code/)
- 動作手順: [Claude Code で実際に動かす手順と検証](https://ai-note.tech/os-greeting-changer-claude-code-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/claude-code/os-greeting-changer .claude/skills/os-greeting-changer
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/claude-code/os-greeting-changer .claude/skills/os-greeting-changer
```

配置後、Claude Code を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Claude Code: https://code.claude.com/docs/ja/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
