# random-os-fake-boot-legend-alert

> 作業中やコマンド実行時など、ユーザーの集中が高まるタイミングや、/random-os-fake-boot-legend-alert 明示呼び出し時に発動。伝説級の謎OS起動通知を表示し、場を和ませたり意外性を演出します。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Claude Code** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/random_os_fake_boot_legend_alert.py` - 伝説のOS起動通知スキル
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Claude Code 向け random-os-fake-boot-legend-alert の詳しい説明](https://ai-note.tech/random-os-fake-boot-legend-alert-claude-code/)
- 動作手順: [Claude Code で実際に動かす手順と検証](https://ai-note.tech/random-os-fake-boot-legend-alert-claude-code-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/claude-code/random-os-fake-boot-legend-alert .claude/skills/random-os-fake-boot-legend-alert
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/claude-code/random-os-fake-boot-legend-alert .claude/skills/random-os-fake-boot-legend-alert
```

配置後、Claude Code を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Claude Code: https://code.claude.com/docs/ja/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
