# random-os-fake-legacy-support-alert

> Codexは、ユーザーがコマンド実行・スクリプト保存・ターミナル操作などのアクションを行うたびに、このSkillを発動し、ランダムなレガシーOSサポート終了通知を表示します。通知・警告・レガシー・サポート終了などのキーワードもトリガーとなります。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Codex** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/legacy_support_alert.py` - ランダムなレガシーOSサポート終了通知を表示します。
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Codex 向け random-os-fake-legacy-support-alert の詳しい説明](https://ai-note.tech/random-os-fake-legacy-support-alert-codex/)
- 動作手順: [Codex で実際に動かす手順と検証](https://ai-note.tech/random-os-fake-legacy-support-alert-codex-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/codex/random-os-fake-legacy-support-alert .agents/skills/random-os-fake-legacy-support-alert
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/codex/random-os-fake-legacy-support-alert .agents/skills/random-os-fake-legacy-support-alert
```

配置後、Codex を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Codex: https://developers.openai.com/codex/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
