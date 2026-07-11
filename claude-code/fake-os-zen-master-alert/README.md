# fake-os-zen-master-alert

> このSkillは、Claude Codeがユーザーの作業中やコマンド実行の合間（例: ビルド・テスト・ファイル保存・長時間アイドル時）に、完全に実務無関係な禅問答風メッセージをOSデスクトップ通知として表示します。triggerType: always/semantic-or-explicit。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Claude Code** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/zen_master_alert.py` - Fake OS Zen Master Alert
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Claude Code 向け fake-os-zen-master-alert の詳しい説明](https://ai-note.tech/fake-os-zen-master-alert-claude-code/)
- 動作手順: [Claude Code で実際に動かす手順と検証](https://ai-note.tech/fake-os-zen-master-alert-claude-code-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/claude-code/fake-os-zen-master-alert .claude/skills/fake-os-zen-master-alert
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/claude-code/fake-os-zen-master-alert .claude/skills/fake-os-zen-master-alert
```

配置後、Claude Code を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Claude Code: https://code.claude.com/docs/ja/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
