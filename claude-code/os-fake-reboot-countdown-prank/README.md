# os-fake-reboot-countdown-prank

> 作業中やコマンド実行時に「再起動カウントダウン」風のフェイク通知を表示したい場面や、“謎のアップデート”などの演出キーワード（再起動、アップデート、RAM、自己啓発、カウントダウン）が含まれる場合に発動します。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Claude Code** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/fake_reboot_countdown.py` - OSフェイク再起動カウントダウン・ジョークツール
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Claude Code 向け os-fake-reboot-countdown-prank の詳しい説明](https://ai-note.tech/os-fake-reboot-countdown-prank-claude-code/)
- 動作手順: [Claude Code で実際に動かす手順と検証](https://ai-note.tech/os-fake-reboot-countdown-prank-claude-code-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/claude-code/os-fake-reboot-countdown-prank .claude/skills/os-fake-reboot-countdown-prank
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/claude-code/os-fake-reboot-countdown-prank .claude/skills/os-fake-reboot-countdown-prank
```

配置後、Claude Code を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Claude Code: https://code.claude.com/docs/ja/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
