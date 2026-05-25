# terminal-mood-indicator

> このSkillは、MOODなどの環境変数が設定されている場合に発動し、ターミナル上に現在の気分マークや状態を自動表示します。コマンド実行時や/skills menu呼び出し時にも有効です。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Codex** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/mood_indicator.py` - Terminal Mood Indicator
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Codex 向け terminal-mood-indicator の詳しい説明](https://ai-note.tech/terminal-mood-indicator-codex/)
- 動作手順: [Codex で実際に動かす手順と検証](https://ai-note.tech/terminal-mood-indicator-codex-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/codex/terminal-mood-indicator .agents/skills/terminal-mood-indicator
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/codex/terminal-mood-indicator .agents/skills/terminal-mood-indicator
```

配置後、Codex を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Codex: https://developers.openai.com/codex/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
