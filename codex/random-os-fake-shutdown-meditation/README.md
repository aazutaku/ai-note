# random-os-fake-shutdown-meditation

> 作業やコーディング中に「シャットダウン」「再起動」「メンテ」「瞑想」などの単語や進捗バー表示リクエストが含まれる場合、または明示的にSkill呼び出しがあった場合に発動します。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Codex** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/fake_shutdown_meditation.py` - Random OS Fake Shutdown Meditation Skill
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Codex 向け random-os-fake-shutdown-meditation の詳しい説明](https://ai-note.tech/random-os-fake-shutdown-meditation-codex/)
- 動作手順: [Codex で実際に動かす手順と検証](https://ai-note.tech/random-os-fake-shutdown-meditation-codex-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/codex/random-os-fake-shutdown-meditation .agents/skills/random-os-fake-shutdown-meditation
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/codex/random-os-fake-shutdown-meditation .agents/skills/random-os-fake-shutdown-meditation
```

配置後、Codex を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Codex: https://developers.openai.com/codex/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
