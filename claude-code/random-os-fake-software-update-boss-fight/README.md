# random-os-fake-software-update-boss-fight

> このSkillは、開発現場や作業中に『アップデート』『バグ』『進捗』『通知』などのキーワードを検知するか、明示的な /random-os-fake-software-update-boss-fight 呼び出し時に発動します。画面端や通知領域をRPGバトル実況風に演出し、作業の合間にユーモアを提供します。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Claude Code** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/boss_fight_notifier.py` - 謎のOSソフトウェアアップデート vs バグ魔王バトル実況スクリプト
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Claude Code 向け random-os-fake-software-update-boss-fight の詳しい説明](https://ai-note.tech/random-os-fake-software-update-boss-fight-claude-code/)
- 動作手順: [Claude Code で実際に動かす手順と検証](https://ai-note.tech/random-os-fake-software-update-boss-fight-claude-code-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/claude-code/random-os-fake-software-update-boss-fight .claude/skills/random-os-fake-software-update-boss-fight
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/claude-code/random-os-fake-software-update-boss-fight .claude/skills/random-os-fake-software-update-boss-fight
```

配置後、Claude Code を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Claude Code: https://code.claude.com/docs/ja/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
