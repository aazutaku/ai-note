# os-fake-mystery-update-progress

> 作業やコマンド実行時、または『アップデート』『進捗』『インストール』『謎』『バグ』『最適化』などの語が会話やコードに現れた際に、理不尽な“謎のOSアップデート進行中”進捗バーを表示します。明示的な /os-fake-mystery-update-progress 呼び出しにも対応。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Claude Code** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/os_fake_mystery_update_progress.py` - 謎のOSアップデート進捗バー
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Claude Code 向け os-fake-mystery-update-progress の詳しい説明](https://ai-note.tech/os-fake-mystery-update-progress-claude-code/)
- 動作手順: [Claude Code で実際に動かす手順と検証](https://ai-note.tech/os-fake-mystery-update-progress-claude-code-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/claude-code/os-fake-mystery-update-progress .claude/skills/os-fake-mystery-update-progress
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/claude-code/os-fake-mystery-update-progress .claude/skills/os-fake-mystery-update-progress
```

配置後、Claude Code を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Claude Code: https://code.claude.com/docs/ja/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
