# random-os-dramatic-poweroff-alert

> 作業や開発に没頭している際、または『shutdown』『電源』『予告』『カオス』『通知』『ジョーク』などのキーワードを含む文脈で、突如として“壮大なOS電源オフ通知”をデスクトップに表示します。実際のシャットダウンは一切行われません。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Codex** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/dramatic_poweroff_alert.py` - 壮大なOS電源オフ予告通知をランダム表示するスクリプト
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Codex 向け random-os-dramatic-poweroff-alert の詳しい説明](https://ai-note.tech/random-os-dramatic-poweroff-alert-codex/)
- 動作手順: [Codex で実際に動かす手順と検証](https://ai-note.tech/random-os-dramatic-poweroff-alert-codex-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/codex/random-os-dramatic-poweroff-alert .agents/skills/random-os-dramatic-poweroff-alert
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/codex/random-os-dramatic-poweroff-alert .agents/skills/random-os-dramatic-poweroff-alert
```

配置後、Codex を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Codex: https://developers.openai.com/codex/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
