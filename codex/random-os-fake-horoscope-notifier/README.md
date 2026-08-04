# random-os-fake-horoscope-notifier

> 作業開始や/skills menuコマンド、random-os-fake-horoscope-notifierへの明示呼び出し時など、セッション開始・ターミナル起動・新規作業開始などのキーワードを検知した際に発動します。1日1回、ランダムな“OS風星占い”通知を表示します。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Codex** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/os_horoscope_notifier.py` - OS Horoscope Notifier - ランダムなOS星占い通知をお届けします
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Codex 向け random-os-fake-horoscope-notifier の詳しい説明](https://ai-note.tech/random-os-fake-horoscope-notifier-codex/)
- 動作手順: [Codex で実際に動かす手順と検証](https://ai-note.tech/random-os-fake-horoscope-notifier-codex-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/codex/random-os-fake-horoscope-notifier .agents/skills/random-os-fake-horoscope-notifier
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/codex/random-os-fake-horoscope-notifier .agents/skills/random-os-fake-horoscope-notifier
```

配置後、Codex を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Codex: https://developers.openai.com/codex/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
