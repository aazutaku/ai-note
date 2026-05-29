# desktop-tension-meter

> 作業中の緊張感や集中度を“根拠になりそうでならない”値から算出し、デスクトップ画面端に無意味な緊張度ラベルをランダムな間隔でテロップ表示します。キーワード: 通知, デスクトップ, 緊張度, 無意味, ランダム, テロップ, 作業中。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Claude Code** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/desktop_tension_meter.py` - desktop-tension-meter: デスクトップに無意味な緊張度をテロップ表示
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Claude Code 向け desktop-tension-meter の詳しい説明](https://ai-note.tech/desktop-tension-meter-claude-code/)
- 動作手順: [Claude Code で実際に動かす手順と検証](https://ai-note.tech/desktop-tension-meter-claude-code-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/claude-code/desktop-tension-meter .claude/skills/desktop-tension-meter
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/claude-code/desktop-tension-meter .claude/skills/desktop-tension-meter
```

配置後、Claude Code を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Claude Code: https://code.claude.com/docs/ja/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
