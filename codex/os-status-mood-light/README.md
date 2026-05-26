# os-status-mood-light

> Codexがユーザーの作業中の気分や状態を可視化したい、または環境変数MOODの変化を検知してシェルやSlack等に通知・反映したい場合に発動します。キーワード例: 気分, MOOD, ステータスバー, シェルプロンプト, Slack連携。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Codex** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/mood_light.py` - os-status-mood-light: 気分可視化スキル
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Codex 向け os-status-mood-light の詳しい説明](https://ai-note.tech/os-status-mood-light-codex/)
- 動作手順: [Codex で実際に動かす手順と検証](https://ai-note.tech/os-status-mood-light-codex-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/codex/os-status-mood-light .agents/skills/os-status-mood-light
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/codex/os-status-mood-light .agents/skills/os-status-mood-light
```

配置後、Codex を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Codex: https://developers.openai.com/codex/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
