# desktop-chaos-alert

> 作業中や会話の流れで「緊急」「アラート」「OS警告」「混乱」「カオス」「通知」などのキーワードが現れた際、または /skills menu や desktop-chaos-alert の明示呼び出し時に発動します。突然、意味不明なOS風アラートをデスクトップ通知で表示し、真面目な雰囲気を一瞬で壊します。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Codex** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/desktop_chaos_alert.py` - desktop-chaos-alert: 謎のOSアラートをデスクトップ通知で爆誕させるスキル
- `references/reference.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Codex 向け desktop-chaos-alert の詳しい説明](https://ai-note.tech/desktop-chaos-alert-codex/)
- 動作手順: [Codex で実際に動かす手順と検証](https://ai-note.tech/desktop-chaos-alert-codex-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/codex/desktop-chaos-alert .agents/skills/desktop-chaos-alert
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/codex/desktop-chaos-alert .agents/skills/desktop-chaos-alert
```

配置後、Codex を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Codex: https://developers.openai.com/codex/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
