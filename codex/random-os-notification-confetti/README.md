# random-os-notification-confetti

> 作業中やコマンド実行時、または /skills メニューや skill名の明示呼び出し時に、完全ランダムな“祝福”通知をOSの通知領域へ表示します。出社やlsコマンドなど、脈絡のないネタ祝福が突然現れ、気分転換や非日常の演出を提供します。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Codex** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/random_os_notification_confetti.py` - 完全ランダムな祝福通知をOSの通知領域に表示します。
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Codex 向け random-os-notification-confetti の詳しい説明](https://ai-note.tech/random-os-notification-confetti-codex/)
- 動作手順: [Codex で実際に動かす手順と検証](https://ai-note.tech/random-os-notification-confetti-codex-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/codex/random-os-notification-confetti .agents/skills/random-os-notification-confetti
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/codex/random-os-notification-confetti .agents/skills/random-os-notification-confetti
```

配置後、Codex を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Codex: https://developers.openai.com/codex/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
