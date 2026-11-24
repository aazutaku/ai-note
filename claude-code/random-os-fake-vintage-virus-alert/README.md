# random-os-fake-vintage-virus-alert

> 作業中やコマンド実行の合間に、明らかにジョークと分かる“レトロOS風ウイルス警告”をランダム表示。/random-os-fake-vintage-virus-alert 呼び出しや「警告」「ウイルス」等のキーワードで発動。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Claude Code** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/random_os_fake_vintage_virus_alert.py` - random-os-fake-vintage-virus-alert: レトロOS風ウイルス警告ジョーク通知
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Claude Code 向け random-os-fake-vintage-virus-alert の詳しい説明](https://ai-note.tech/random-os-fake-vintage-virus-alert-claude-code/)
- 動作手順: [Claude Code で実際に動かす手順と検証](https://ai-note.tech/random-os-fake-vintage-virus-alert-claude-code-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/claude-code/random-os-fake-vintage-virus-alert .claude/skills/random-os-fake-vintage-virus-alert
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/claude-code/random-os-fake-vintage-virus-alert .claude/skills/random-os-fake-vintage-virus-alert
```

配置後、Claude Code を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Claude Code: https://code.claude.com/docs/ja/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
