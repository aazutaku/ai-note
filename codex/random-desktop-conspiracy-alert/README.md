# random-desktop-conspiracy-alert

> 作業やコーディング中、または /skills メニューや skill名への明示的な呼び出し時に、意味不明で根拠のない陰謀論アラートをデスクトップ通知で発生させます。trigger キーワード: 通知、アラート、陰謀論、気分転換。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Codex** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/conspiracy_alert.py` - Random Desktop Conspiracy Alert
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Codex 向け random-desktop-conspiracy-alert の詳しい説明](https://ai-note.tech/random-desktop-conspiracy-alert-codex/)
- 動作手順: [Codex で実際に動かす手順と検証](https://ai-note.tech/random-desktop-conspiracy-alert-codex-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/codex/random-desktop-conspiracy-alert .agents/skills/random-desktop-conspiracy-alert
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/codex/random-desktop-conspiracy-alert .agents/skills/random-desktop-conspiracy-alert
```

配置後、Codex を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Codex: https://developers.openai.com/codex/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
