# os-random-fake-password-policy-alert

> 作業中やコマンド実行時に、パスワードや認証、セキュリティ、ログイン、OS設定などに関連するキーワードが出現した場合、もしくは/skill-nameで明示的に呼び出された場合に発動します。現場の緊張感を和らげたいときに最適です。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Claude Code** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/fake_password_policy_alert.py` - osascript -e 'display notification "{message}" with title "[{level}] パスワードポリシー通知"'
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Claude Code 向け os-random-fake-password-policy-alert の詳しい説明](https://ai-note.tech/os-random-fake-password-policy-alert-claude-code/)
- 動作手順: [Claude Code で実際に動かす手順と検証](https://ai-note.tech/os-random-fake-password-policy-alert-claude-code-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/claude-code/os-random-fake-password-policy-alert .claude/skills/os-random-fake-password-policy-alert
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/claude-code/os-random-fake-password-policy-alert .claude/skills/os-random-fake-password-policy-alert
```

配置後、Claude Code を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Claude Code: https://code.claude.com/docs/ja/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
