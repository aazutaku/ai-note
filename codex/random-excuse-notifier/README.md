# random-excuse-notifier

> Codexがターミナル操作やコマンド実行、/skills menuやrandom-excuse-notifierの明示呼び出し時に発動。通知・OS連携・演出系Skillとして、操作ごとにユーモラスな“言い訳”をOS通知領域へ表示します。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Codex** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/random_excuse_notifier.py` - random-excuse-notifier: ターミナル操作ごとに言い訳通知を表示
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Codex 向け random-excuse-notifier の詳しい説明](https://ai-note.tech/random-excuse-notifier-codex/)
- 動作手順: [Codex で実際に動かす手順と検証](https://ai-note.tech/random-excuse-notifier-codex-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/codex/random-excuse-notifier .agents/skills/random-excuse-notifier
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/codex/random-excuse-notifier .agents/skills/random-excuse-notifier
```

配置後、Codex を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Codex: https://developers.openai.com/codex/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
