# random-os-fake-morning-radio

> 作業開始直後や『おはよう』『start work』などのキーワード、または明示的なSkill呼び出し時に、OS風ラジオDJトークや意味不明なOSニュースを通知・ターミナル出力します。日替わりで無駄な実況やゴシップが流れ、開発現場に笑いと活気を注入します。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Codex** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/os_fake_morning_radio.py` - 謎のOSモーニングラジオ風メッセージを出力します。
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Codex 向け random-os-fake-morning-radio の詳しい説明](https://ai-note.tech/random-os-fake-morning-radio-codex/)
- 動作手順: [Codex で実際に動かす手順と検証](https://ai-note.tech/random-os-fake-morning-radio-codex-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/codex/random-os-fake-morning-radio .agents/skills/random-os-fake-morning-radio
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/codex/random-os-fake-morning-radio .agents/skills/random-os-fake-morning-radio
```

配置後、Codex を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Codex: https://developers.openai.com/codex/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
