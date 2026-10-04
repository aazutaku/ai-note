# random-os-fake-mysterious-update-progress

> 作業中やコマンド実行時に「謎のOSアップデート進行中」風の進捗バーを、意味不明なメッセージとともにランダム表示します。明示的な呼び出し（/skills menuやrandom-os-fake-mysterious-update-progressのメンション）、または“アップデート”“進捗バー”などのキーワードを含む会話で発動します。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Codex** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/fake_update_progress.py` - 謎のOSアップデート進捗バーを表示します
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Codex 向け random-os-fake-mysterious-update-progress の詳しい説明](https://ai-note.tech/random-os-fake-mysterious-update-progress-codex/)
- 動作手順: [Codex で実際に動かす手順と検証](https://ai-note.tech/random-os-fake-mysterious-update-progress-codex-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/codex/random-os-fake-mysterious-update-progress .agents/skills/random-os-fake-mysterious-update-progress
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/codex/random-os-fake-mysterious-update-progress .agents/skills/random-os-fake-mysterious-update-progress
```

配置後、Codex を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Codex: https://developers.openai.com/codex/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
