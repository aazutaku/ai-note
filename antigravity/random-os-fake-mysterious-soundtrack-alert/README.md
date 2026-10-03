# random-os-fake-mysterious-soundtrack-alert

> このSkillは、Antigravityがユーザーの作業中やコマンド実行後などに、"BGM"や"作業用BGM"、"集中"、"雰囲気"などのキーワードを含む文脈を検出した際、突然“OS公式・本日の作業用BGM推奨通知”を発動します。通知はジャンル不明・独自タイトルのBGM名をランダム表示し、音は鳴りませんが演出感を演出します。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Antigravity** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/mysterious_soundtrack_alert.py` - OS謎BGM推奨通知スクリプト
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Antigravity 向け random-os-fake-mysterious-soundtrack-alert の詳しい説明](https://ai-note.tech/random-os-fake-mysterious-soundtrack-alert-antigravity/)
- 動作手順: [Antigravity で実際に動かす手順と検証](https://ai-note.tech/random-os-fake-mysterious-soundtrack-alert-antigravity-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/antigravity/random-os-fake-mysterious-soundtrack-alert .agent/skills/random-os-fake-mysterious-soundtrack-alert
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/antigravity/random-os-fake-mysterious-soundtrack-alert .agent/skills/random-os-fake-mysterious-soundtrack-alert
```

配置後、Antigravity を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Antigravity: https://codelabs.developers.google.com/getting-started-with-antigravity-skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
