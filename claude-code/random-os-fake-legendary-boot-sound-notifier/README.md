# random-os-fake-legendary-boot-sound-notifier

> 作業開始・新規セッション・/random-os-fake-legendary-boot-sound-notifierコマンド実行時など、ユーザーのアクションを検知した際に発動。通知内容は毎回異なる“実在しない伝説のOS起動音”名で、実際の音は鳴らさずテキスト表示のみ。集中力のリセットやユーモア演出に最適。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Claude Code** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/random_os_fake_legendary_boot_sound_notifier.py` - === OS起動音通知 ===
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Claude Code 向け random-os-fake-legendary-boot-sound-notifier の詳しい説明](https://ai-note.tech/random-os-fake-legendary-boot-sound-notifier-claude-code/)
- 動作手順: [Claude Code で実際に動かす手順と検証](https://ai-note.tech/random-os-fake-legendary-boot-sound-notifier-claude-code-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/claude-code/random-os-fake-legendary-boot-sound-notifier .claude/skills/random-os-fake-legendary-boot-sound-notifier
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/claude-code/random-os-fake-legendary-boot-sound-notifier .claude/skills/random-os-fake-legendary-boot-sound-notifier
```

配置後、Claude Code を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Claude Code: https://code.claude.com/docs/ja/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
