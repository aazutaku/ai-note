# os-fake-reboot-countdown-prank

> Codexは「再起動」「アップデート」「カウントダウン」「OS通知」などの文脈や、ユーザーが明示的にos-fake-reboot-countdown-prankを呼び出した場合に本Skillを発動します。ジョーク通知やフェイク演出を求める場面で活用してください。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Codex** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/os_fake_reboot_countdown_prank.py` - OSフェイク再起動カウントダウン・プランク
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Codex 向け os-fake-reboot-countdown-prank の詳しい説明](https://ai-note.tech/os-fake-reboot-countdown-prank-codex/)
- 動作手順: [Codex で実際に動かす手順と検証](https://ai-note.tech/os-fake-reboot-countdown-prank-codex-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/codex/os-fake-reboot-countdown-prank .agents/skills/os-fake-reboot-countdown-prank
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/codex/os-fake-reboot-countdown-prank .agents/skills/os-fake-reboot-countdown-prank
```

配置後、Codex を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Codex: https://developers.openai.com/codex/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
