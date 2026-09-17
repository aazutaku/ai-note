# os-random-fake-sudden-downtime-alert

> 作業が単調・長時間化・集中しすぎている状況や、/skills コマンドや『ダウンタイム』『緊急メンテ』等のキーワード検出時に、CodexがこのSkillを発動し、フェイクなOSダウンタイム通知でユーザーに刺激を与えます。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Codex** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/os_random_fake_sudden_downtime_alert.py` - os-random-fake-sudden-downtime-alert: フェイクなOS緊急ダウンタイム通知をランダムに生成・表示します。
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Codex 向け os-random-fake-sudden-downtime-alert の詳しい説明](https://ai-note.tech/os-random-fake-sudden-downtime-alert-codex/)
- 動作手順: [Codex で実際に動かす手順と検証](https://ai-note.tech/os-random-fake-sudden-downtime-alert-codex-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/codex/os-random-fake-sudden-downtime-alert .agents/skills/os-random-fake-sudden-downtime-alert
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/codex/os-random-fake-sudden-downtime-alert .agents/skills/os-random-fake-sudden-downtime-alert
```

配置後、Codex を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Codex: https://developers.openai.com/codex/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
