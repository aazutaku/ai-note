# os-fake-bug-bounty-alert

> 作業中やコマンド実行時、または/skillsメニューやos-fake-bug-bounty-alertの明示呼び出し時に、完全ランダムな“偽バグバウンティ通知”を発動。通知・演出・OS連携カテゴリで、緊張緩和や場の和ませ効果を狙います。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Codex** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/os_fake_bug_bounty_alert.py` - os-fake-bug-bounty-alert: ランダムな偽バグバウンティ通知を生成します。
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Codex 向け os-fake-bug-bounty-alert の詳しい説明](https://ai-note.tech/os-fake-bug-bounty-alert-codex/)
- 動作手順: [Codex で実際に動かす手順と検証](https://ai-note.tech/os-fake-bug-bounty-alert-codex-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/codex/os-fake-bug-bounty-alert .agents/skills/os-fake-bug-bounty-alert
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/codex/os-fake-bug-bounty-alert .agents/skills/os-fake-bug-bounty-alert
```

配置後、Codex を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Codex: https://developers.openai.com/codex/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
