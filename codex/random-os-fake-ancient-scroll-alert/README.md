# random-os-fake-ancient-scroll-alert

> このSkillは、コマンド実行や作業の合間（例: build, test, push, review, idle, waiting, menu表示）に、巻物風UIで無意味な“謎のOS古文書通知”をランダム生成・表示します。集中力ブレイカーやエンタメ演出を求める場面で発動してください。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Codex** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/random_scroll_alert.py` - ランダムで古文書風の通知文を3行生成
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Codex 向け random-os-fake-ancient-scroll-alert の詳しい説明](https://ai-note.tech/random-os-fake-ancient-scroll-alert-codex/)
- 動作手順: [Codex で実際に動かす手順と検証](https://ai-note.tech/random-os-fake-ancient-scroll-alert-codex-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/codex/random-os-fake-ancient-scroll-alert .agents/skills/random-os-fake-ancient-scroll-alert
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/codex/random-os-fake-ancient-scroll-alert .agents/skills/random-os-fake-ancient-scroll-alert
```

配置後、Codex を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Codex: https://developers.openai.com/codex/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
