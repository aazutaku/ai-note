# command-failure-excuse-notifier

> コマンド実行時に失敗（例: exit code非ゼロや例外発生）が検出された場合に発動し、OSの通知領域へ“言い訳”を添えたエラーメッセージを表示します。失敗時の通知・演出・OS連携が必要な場面で自動/明示的に利用されます。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Codex** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/command_failure_excuse_notifier.py` - コマンド失敗時に言い訳通知を出すスキル
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Codex 向け command-failure-excuse-notifier の詳しい説明](https://ai-note.tech/command-failure-excuse-notifier-codex/)
- 動作手順: [Codex で実際に動かす手順と検証](https://ai-note.tech/command-failure-excuse-notifier-codex-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/codex/command-failure-excuse-notifier .agents/skills/command-failure-excuse-notifier
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/codex/command-failure-excuse-notifier .agents/skills/command-failure-excuse-notifier
```

配置後、Codex を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Codex: https://developers.openai.com/codex/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
