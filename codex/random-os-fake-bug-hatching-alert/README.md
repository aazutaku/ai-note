# random-os-fake-bug-hatching-alert

> このSkillは、Codexがユーザーの作業中やコマンド実行の合間（例: 長時間のビルドやテスト、待機中のプロンプト）に、ランダムなタイミングで“OS公式のバグ孵化警告”を演出として表示します。発動トリガーは「通知」「バグ」「警告」「ランダム」「演出」などのキーワードや、明示的なSkill呼び出し時です。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Codex** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/bug_hatching_alert.py` - OS公式バグ孵化警告スキル (演出専用)
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Codex 向け random-os-fake-bug-hatching-alert の詳しい説明](https://ai-note.tech/random-os-fake-bug-hatching-alert-codex/)
- 動作手順: [Codex で実際に動かす手順と検証](https://ai-note.tech/random-os-fake-bug-hatching-alert-codex-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/codex/random-os-fake-bug-hatching-alert .agents/skills/random-os-fake-bug-hatching-alert
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/codex/random-os-fake-bug-hatching-alert .agents/skills/random-os-fake-bug-hatching-alert
```

配置後、Codex を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Codex: https://developers.openai.com/codex/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
