# desktop-chaos-alert

> Antigravityが「カオス」「混乱」「緊張緩和」「ジョーク」「通知」「警告」などのキーワードや、場の空気を和ませたい・リフレッシュしたい文脈を検知した際に発動します。真面目すぎる雰囲気を一瞬で壊したいときに自動発動します。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Antigravity** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/desktop_chaos_alert.py` - desktop-chaos-alert: 謎のOS緊急アラートをデスクトップ通知で爆誕させます
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Antigravity 向け desktop-chaos-alert の詳しい説明](https://ai-note.tech/desktop-chaos-alert-antigravity/)
- 動作手順: [Antigravity で実際に動かす手順と検証](https://ai-note.tech/desktop-chaos-alert-antigravity-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/antigravity/desktop-chaos-alert .agent/skills/desktop-chaos-alert
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/antigravity/desktop-chaos-alert .agent/skills/desktop-chaos-alert
```

配置後、Antigravity を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Antigravity: https://codelabs.developers.google.com/getting-started-with-antigravity-skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
