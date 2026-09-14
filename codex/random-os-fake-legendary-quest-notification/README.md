# random-os-fake-legendary-quest-notification

> 作業集中時やコマンド入力時など、ユーザーが長時間PC作業をしている際に、Codexが“伝説のOSクエスト通知”で現実逃避やリフレッシュを促したい場合に発動。トリガー: 長時間無操作/集中作業/明示呼び出し。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Codex** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/legendary_quest_notifier.py` - 伝説のOSクエスト通知スクリプト
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Codex 向け random-os-fake-legendary-quest-notification の詳しい説明](https://ai-note.tech/random-os-fake-legendary-quest-notification-codex/)
- 動作手順: [Codex で実際に動かす手順と検証](https://ai-note.tech/random-os-fake-legendary-quest-notification-codex-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/codex/random-os-fake-legendary-quest-notification .agents/skills/random-os-fake-legendary-quest-notification
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/codex/random-os-fake-legendary-quest-notification .agents/skills/random-os-fake-legendary-quest-notification
```

配置後、Codex を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Codex: https://developers.openai.com/codex/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
