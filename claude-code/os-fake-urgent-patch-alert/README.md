# os-fake-urgent-patch-alert

> 作業中やコード編集時、"緊急"や"パッチ"、"バグ修正"などのキーワードを含む会話やコマンド実行時、もしくは明示的な /os-fake-urgent-patch-alert 呼び出し時に発動。ユーザーの集中を和らげる演出として利用。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Claude Code** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/fake_patch_alert.py` - OS緊急パッチアラート (フェイク通知)
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Claude Code 向け os-fake-urgent-patch-alert の詳しい説明](https://ai-note.tech/os-fake-urgent-patch-alert-claude-code/)
- 動作手順: [Claude Code で実際に動かす手順と検証](https://ai-note.tech/os-fake-urgent-patch-alert-claude-code-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/claude-code/os-fake-urgent-patch-alert .claude/skills/os-fake-urgent-patch-alert
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/claude-code/os-fake-urgent-patch-alert .claude/skills/os-fake-urgent-patch-alert
```

配置後、Claude Code を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Claude Code: https://code.claude.com/docs/ja/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
