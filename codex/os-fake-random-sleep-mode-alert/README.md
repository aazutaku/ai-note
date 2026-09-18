# os-fake-random-sleep-mode-alert

> 作業中や集中力低下時など、ユーザーのアクティビティが停滞したタイミングや、/skills コマンド・スキル名の明示呼び出し時に発動。通知・警告・スリープ・昼寝・OS管理・強制・集中力などのキーワードを含む文脈で自動発動。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Codex** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/os_fake_random_sleep_mode_alert.py` - OS風スリープモード警告通知をランダムに表示するスキル (ネタ用途)
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Codex 向け os-fake-random-sleep-mode-alert の詳しい説明](https://ai-note.tech/os-fake-random-sleep-mode-alert-codex/)
- 動作手順: [Codex で実際に動かす手順と検証](https://ai-note.tech/os-fake-random-sleep-mode-alert-codex-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/codex/os-fake-random-sleep-mode-alert .agents/skills/os-fake-random-sleep-mode-alert
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/codex/os-fake-random-sleep-mode-alert .agents/skills/os-fake-random-sleep-mode-alert
```

配置後、Codex を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Codex: https://developers.openai.com/codex/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
