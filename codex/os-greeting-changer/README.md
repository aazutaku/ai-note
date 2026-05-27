# os-greeting-changer

> ターミナルやコンソール起動時、または /skills menu などの明示呼び出し時に発動。現実には存在しないOSや珍しい起動演出をランダムに表示し、実作業やファイルには一切影響しない安全なSkillです。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Codex** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/os_greeting_changer.py` - ターミナル起動時に偽OSメッセージをランダム表示する遊び心Skill
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Codex 向け os-greeting-changer の詳しい説明](https://ai-note.tech/os-greeting-changer-codex/)
- 動作手順: [Codex で実際に動かす手順と検証](https://ai-note.tech/os-greeting-changer-codex-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/codex/os-greeting-changer .agents/skills/os-greeting-changer
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/codex/os-greeting-changer .agents/skills/os-greeting-changer
```

配置後、Codex を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Codex: https://developers.openai.com/codex/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
