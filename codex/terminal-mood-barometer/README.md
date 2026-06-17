# terminal-mood-barometer

> コマンド実行やターミナル操作時に、必ず“気分指数”とランダムな小ネタコメントを表示し、作業気分を演出します。コマンド発行・/skills menu・skill名明示時に発動。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Codex** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/mood_barometer.py` - terminal-mood-barometer: ターミナル作業に気分指数を演出表示
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Codex 向け terminal-mood-barometer の詳しい説明](https://ai-note.tech/terminal-mood-barometer-codex/)
- 動作手順: [Codex で実際に動かす手順と検証](https://ai-note.tech/terminal-mood-barometer-codex-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/codex/terminal-mood-barometer .agents/skills/terminal-mood-barometer
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/codex/terminal-mood-barometer .agents/skills/terminal-mood-barometer
```

配置後、Codex を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Codex: https://developers.openai.com/codex/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
