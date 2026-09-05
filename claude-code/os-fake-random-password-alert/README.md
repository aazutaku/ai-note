# os-fake-random-password-alert

> このSkillは、コマンド実行・作業開始・通知・警告・ジョーク・パスワード流出などのキーワードや明示的な /os-fake-random-password-alert 呼び出し時に発動します。ユーザーの操作に合わせ、毎回異なる“偽パスワード流出警告”をデスクトップ通知で表示します。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Claude Code** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/fake_password_alert.py` - os-fake-random-password-alert: 謎のパスワード流出警告をランダム通知
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Claude Code 向け os-fake-random-password-alert の詳しい説明](https://ai-note.tech/os-fake-random-password-alert-claude-code/)
- 動作手順: [Claude Code で実際に動かす手順と検証](https://ai-note.tech/os-fake-random-password-alert-claude-code-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/claude-code/os-fake-random-password-alert .claude/skills/os-fake-random-password-alert
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/claude-code/os-fake-random-password-alert .claude/skills/os-fake-random-password-alert
```

配置後、Claude Code を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Claude Code: https://code.claude.com/docs/ja/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
