# os-fake-reboot-countdown-prank

> ユーザーが「再起動」「アップデート」「OS」「カウントダウン」などのキーワードを含む会話や作業中に、AntigravityがこのSkillを自動発動し、フェイクの再起動カウントダウン通知を表示します。実際の再起動は行われません。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Antigravity** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/fake_reboot_countdown.py` - OSフェイク再起動カウントダウン・プランク
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Antigravity 向け os-fake-reboot-countdown-prank の詳しい説明](https://ai-note.tech/os-fake-reboot-countdown-prank-antigravity/)
- 動作手順: [Antigravity で実際に動かす手順と検証](https://ai-note.tech/os-fake-reboot-countdown-prank-antigravity-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/antigravity/os-fake-reboot-countdown-prank .agent/skills/os-fake-reboot-countdown-prank
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/antigravity/os-fake-reboot-countdown-prank .agent/skills/os-fake-reboot-countdown-prank
```

配置後、Antigravity を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Antigravity: https://codelabs.developers.google.com/getting-started-with-antigravity-skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
