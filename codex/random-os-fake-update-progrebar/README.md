# random-os-fake-update-progrebar

> このSkillは、コマンド実行やエディタ操作時など作業の合間に、ランダムな“謎のOSアップデート進捗バー”を端やメニューバー風に表示します。進捗内容は毎回異なり、進捗バーが100%になっても何も起きません。通知・演出・OS連携カテゴリで、脱力系の演出を自動または明示的に発動します。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Codex** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/random_os_fake_update_progrebar.py` - 謎のOSアップデート進捗バーをランダム表示する演出スクリプト
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Codex 向け random-os-fake-update-progrebar の詳しい説明](https://ai-note.tech/random-os-fake-update-progrebar-codex/)
- 動作手順: [Codex で実際に動かす手順と検証](https://ai-note.tech/random-os-fake-update-progrebar-codex-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/codex/random-os-fake-update-progrebar .agents/skills/random-os-fake-update-progrebar
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/codex/random-os-fake-update-progrebar .agents/skills/random-os-fake-update-progrebar
```

配置後、Codex を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Codex: https://developers.openai.com/codex/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
