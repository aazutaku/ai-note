# random-os-fake-power-saving-mode

> 作業中やコーディング時に「省エネ」「パフォーマンス低下」「謎のOS通知」などのキーワードが含まれる会話やコマンド実行時、または明示的に /random-os-fake-power-saving-mode を呼び出した際に発動。完全なフェイク通知を生成し、実環境には影響しません。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Claude Code** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/fake_power_saving_mode.py` - 謎のOSフェイク省エネモード通知をランダム生成・履歴管理するスクリプト
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Claude Code 向け random-os-fake-power-saving-mode の詳しい説明](https://ai-note.tech/random-os-fake-power-saving-mode-claude-code/)
- 動作手順: [Claude Code で実際に動かす手順と検証](https://ai-note.tech/random-os-fake-power-saving-mode-claude-code-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/claude-code/random-os-fake-power-saving-mode .claude/skills/random-os-fake-power-saving-mode
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/claude-code/random-os-fake-power-saving-mode .claude/skills/random-os-fake-power-saving-mode
```

配置後、Claude Code を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Claude Code: https://code.claude.com/docs/ja/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
