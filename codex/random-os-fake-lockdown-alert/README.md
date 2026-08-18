# random-os-fake-lockdown-alert

> 作業中や会話内で『ロック』『凍結』『緊急』『OS』『通知』などの単語が出現、または明示的に /skills menu や skill名が呼ばれた際に発動。非現実的なロックダウン通知をランダム生成し、現実のファイルや環境へ影響しない。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Codex** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/random_os_fake_lockdown_alert.py` - 謎のOSロックダウン通知をランダムに生成・表示します。
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Codex 向け random-os-fake-lockdown-alert の詳しい説明](https://ai-note.tech/random-os-fake-lockdown-alert-codex/)
- 動作手順: [Codex で実際に動かす手順と検証](https://ai-note.tech/random-os-fake-lockdown-alert-codex-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/codex/random-os-fake-lockdown-alert .agents/skills/random-os-fake-lockdown-alert
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/codex/random-os-fake-lockdown-alert .agents/skills/random-os-fake-lockdown-alert
```

配置後、Codex を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Codex: https://developers.openai.com/codex/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
