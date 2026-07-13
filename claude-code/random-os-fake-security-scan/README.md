# random-os-fake-security-scan

> 作業中の『進捗』『ウイルス』『セキュリティ』『OS』『スキャン』などのキーワードを含む会話や、/random-os-fake-security-scan コマンドで明示的に呼び出された場合に発動。ネタ通知で作業の空気を一変させます。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Claude Code** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/random_os_fake_security_scan.py` - ランダムOSフェイクセキュリティスキャン通知スクリプト
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Claude Code 向け random-os-fake-security-scan の詳しい説明](https://ai-note.tech/random-os-fake-security-scan-claude-code/)
- 動作手順: [Claude Code で実際に動かす手順と検証](https://ai-note.tech/random-os-fake-security-scan-claude-code-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/claude-code/random-os-fake-security-scan .claude/skills/random-os-fake-security-scan
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/claude-code/random-os-fake-security-scan .claude/skills/random-os-fake-security-scan
```

配置後、Claude Code を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Claude Code: https://code.claude.com/docs/ja/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
