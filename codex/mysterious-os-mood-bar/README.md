# mysterious-os-mood-bar

> コマンド実行時や /skills menu などの明示呼び出し時に、ユーザーの気分ややる気温度を冗談的に推定し、macOS/Linuxのメニューバーやステータスバーに即時表示するSkill。コマンド長やgit status等のキーワードをトリガーに発動。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Codex** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/mood_bar.py` - mysterious-os-mood-bar: ターミナル気分温度バー
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Codex 向け mysterious-os-mood-bar の詳しい説明](https://ai-note.tech/mysterious-os-mood-bar-codex/)
- 動作手順: [Codex で実際に動かす手順と検証](https://ai-note.tech/mysterious-os-mood-bar-codex-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/codex/mysterious-os-mood-bar .agents/skills/mysterious-os-mood-bar
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/codex/mysterious-os-mood-bar .agents/skills/mysterious-os-mood-bar
```

配置後、Codex を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Codex: https://developers.openai.com/codex/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
