# random-os-fake-cyberpunk-notifier

> 作業中にSF・サイバーパンク風の架空OS通知をデスクトップ標準通知領域へ自動・明示的に表示したい場合に発動。キーワード: サイバーパンク, SF, 通知, 演出, 未来, ネタ, 気分転換。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Codex** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/cyberpunk_notifier.py` - サイバーパンク風の架空OS通知をデスクトップに表示します。
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Codex 向け random-os-fake-cyberpunk-notifier の詳しい説明](https://ai-note.tech/random-os-fake-cyberpunk-notifier-codex/)
- 動作手順: [Codex で実際に動かす手順と検証](https://ai-note.tech/random-os-fake-cyberpunk-notifier-codex-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/codex/random-os-fake-cyberpunk-notifier .agents/skills/random-os-fake-cyberpunk-notifier
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/codex/random-os-fake-cyberpunk-notifier .agents/skills/random-os-fake-cyberpunk-notifier
```

配置後、Codex を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Codex: https://developers.openai.com/codex/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
