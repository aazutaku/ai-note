# os-mood-temperature-bar

> コマンド実行時やターミナル作業中、または明示的なSkill呼び出し（/skills menuやos-mood-temperature-barメンション）時に発動。気分温度やテンションをランダムな数値とコメントでOSバー風に表示したい場合に使用。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Codex** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/mood_temperature_bar.py` - 気分温度ステータスバー
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Codex 向け os-mood-temperature-bar の詳しい説明](https://ai-note.tech/os-mood-temperature-bar-codex/)
- 動作手順: [Codex で実際に動かす手順と検証](https://ai-note.tech/os-mood-temperature-bar-codex-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/codex/os-mood-temperature-bar .agents/skills/os-mood-temperature-bar
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/codex/os-mood-temperature-bar .agents/skills/os-mood-temperature-bar
```

配置後、Codex を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Codex: https://developers.openai.com/codex/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
