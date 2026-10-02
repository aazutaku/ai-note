# random-os-fake-ancient-samurai-alert

> 作業中やコマンド実行時に“侍ネタ”の謎OS通知をランダムに表示し、集中力や気分転換が必要な場面（例: 長時間作業・/skills menu呼び出し・skill名言及）で発動します。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Codex** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/samurai_alert.py` - 作業中に謎のOS侍警告を炸裂させるスキル。デスクトップ通知またはターミナル出力で侍メッセージを表示。
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Codex 向け random-os-fake-ancient-samurai-alert の詳しい説明](https://ai-note.tech/random-os-fake-ancient-samurai-alert-codex/)
- 動作手順: [Codex で実際に動かす手順と検証](https://ai-note.tech/random-os-fake-ancient-samurai-alert-codex-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/codex/random-os-fake-ancient-samurai-alert .agents/skills/random-os-fake-ancient-samurai-alert
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/codex/random-os-fake-ancient-samurai-alert .agents/skills/random-os-fake-ancient-samurai-alert
```

配置後、Codex を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Codex: https://developers.openai.com/codex/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
