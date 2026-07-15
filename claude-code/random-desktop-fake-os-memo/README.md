# random-desktop-fake-os-memo

> 作業中やコーディング時に、完全ランダムな“謎のOSメモ”をデスクトップ通知として発動。通知・演出・OS連携のキーワードが含まれる状況や、/random-desktop-fake-os-memo コマンド実行時に自動で発動します。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Claude Code** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/random_desktop_fake_os_memo.py` - random-desktop-fake-os-memo: 謎のOSメモをランダム通知
- `references/reference.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Claude Code 向け random-desktop-fake-os-memo の詳しい説明](https://ai-note.tech/random-desktop-fake-os-memo-claude-code/)
- 動作手順: [Claude Code で実際に動かす手順と検証](https://ai-note.tech/random-desktop-fake-os-memo-claude-code-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/claude-code/random-desktop-fake-os-memo .claude/skills/random-desktop-fake-os-memo
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/claude-code/random-desktop-fake-os-memo .claude/skills/random-desktop-fake-os-memo
```

配置後、Claude Code を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Claude Code: https://code.claude.com/docs/ja/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
