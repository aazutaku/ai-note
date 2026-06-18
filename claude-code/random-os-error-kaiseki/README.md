# random-os-error-kaiseki

> コマンド実行時にエラーが発生した場合、このSkillは自動的に“OS風カタカナ専門用語”による意味不明なエラー解説をデスクトップ通知で強制表示します。trigger: error, exception, コマンド失敗, /random-os-error-kaiseki。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Claude Code** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/random_os_error_kaiseki.py` - random-os-error-kaiseki: OS風カタカナエラー通知
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Claude Code 向け random-os-error-kaiseki の詳しい説明](https://ai-note.tech/random-os-error-kaiseki-claude-code/)
- 動作手順: [Claude Code で実際に動かす手順と検証](https://ai-note.tech/random-os-error-kaiseki-claude-code-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/claude-code/random-os-error-kaiseki .claude/skills/random-os-error-kaiseki
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/claude-code/random-os-error-kaiseki .claude/skills/random-os-error-kaiseki
```

配置後、Claude Code を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Claude Code: https://code.claude.com/docs/ja/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
