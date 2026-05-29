# desktop-tension-meter

> 作業中のユーザーに対し、commit数やタイピング速度などの“根拠になりそうでならない”値や完全ランダムで緊張度を算出し、一定間隔でデスクトップにテロップ表示する。トリガーワード: 緊張, プレッシャー, テロップ, デスクトップ通知, 無意味な演出。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Codex** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/desktop_tension_meter.py` - desktop-tension-meter: 意味のない緊張度テロップをデスクトップに表示
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Codex 向け desktop-tension-meter の詳しい説明](https://ai-note.tech/desktop-tension-meter-codex/)
- 動作手順: [Codex で実際に動かす手順と検証](https://ai-note.tech/desktop-tension-meter-codex-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/codex/desktop-tension-meter .agents/skills/desktop-tension-meter
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/codex/desktop-tension-meter .agents/skills/desktop-tension-meter
```

配置後、Codex を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Codex: https://developers.openai.com/codex/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
