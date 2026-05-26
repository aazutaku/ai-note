# os-status-mood-light

> 環境変数MOODやOSステータスバー、シェルプロンプトの状態変化を検知し、ユーザーの気分をリアルタイムで可視化したい場合に発動。気分変更やSlack連携、日替わりネタ表示などのキーワードが含まれるときに推奨。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Claude Code** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/os_status_mood_light.py` - os-status-mood-light: 気分をOSやSlackに可視化
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Claude Code 向け os-status-mood-light の詳しい説明](https://ai-note.tech/os-status-mood-light-claude-code/)
- 動作手順: [Claude Code で実際に動かす手順と検証](https://ai-note.tech/os-status-mood-light-claude-code-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/claude-code/os-status-mood-light .claude/skills/os-status-mood-light
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/claude-code/os-status-mood-light .claude/skills/os-status-mood-light
```

配置後、Claude Code を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Claude Code: https://code.claude.com/docs/ja/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
