# random-os-fake-telepathic-command-alert

> このSkillは、ユーザーがコマンド入力や作業中に“念波”や“心の声”をOSが検出したかのようなフェイク通知をランダムに表示します。明示的な呼び出し（/skills menuやskill名メンション）や、作業進行・コマンド実行などのsemantic trigger時に発動します。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Codex** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/telepathic_alert.py` - OS読心術フェイク通知スキル
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Codex 向け random-os-fake-telepathic-command-alert の詳しい説明](https://ai-note.tech/random-os-fake-telepathic-command-alert-codex/)
- 動作手順: [Codex で実際に動かす手順と検証](https://ai-note.tech/random-os-fake-telepathic-command-alert-codex-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/codex/random-os-fake-telepathic-command-alert .agents/skills/random-os-fake-telepathic-command-alert
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/codex/random-os-fake-telepathic-command-alert .agents/skills/random-os-fake-telepathic-command-alert
```

配置後、Codex を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Codex: https://developers.openai.com/codex/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
