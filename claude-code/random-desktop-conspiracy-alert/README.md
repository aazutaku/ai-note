# random-desktop-conspiracy-alert

> このSkillは、作業中や特定のキーワード（例: "集中力", "バグ", "監視"）が会話やコードに現れた際、または明示的に /random-desktop-conspiracy-alert を実行した際に、意味不明な陰謀論アラートをデスクトップ通知で表示します。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Claude Code** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/random_desktop_conspiracy_alert.py` - random-desktop-conspiracy-alert: 謎の陰謀論アラートをデスクトップ通知で爆誕させる
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Claude Code 向け random-desktop-conspiracy-alert の詳しい説明](https://ai-note.tech/random-desktop-conspiracy-alert-claude-code/)
- 動作手順: [Claude Code で実際に動かす手順と検証](https://ai-note.tech/random-desktop-conspiracy-alert-claude-code-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/claude-code/random-desktop-conspiracy-alert .claude/skills/random-desktop-conspiracy-alert
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/claude-code/random-desktop-conspiracy-alert .claude/skills/random-desktop-conspiracy-alert
```

配置後、Claude Code を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Claude Code: https://code.claude.com/docs/ja/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
