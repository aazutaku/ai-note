# os-greeting-changer

> ターミナルやコンソールが起動した際、または新しいセッション開始時に、現実には存在しないOSや架空の起動メッセージをランダムに表示することで、作業開始時に遊び心を提供します。triggerTypeはalways、semantic-match-onlyで発動。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Antigravity** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/os_greeting_changer.py` - ターミナル起動時に偽OS起動メッセージを表示するスクリプト
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Antigravity 向け os-greeting-changer の詳しい説明](https://ai-note.tech/os-greeting-changer-antigravity/)
- 動作手順: [Antigravity で実際に動かす手順と検証](https://ai-note.tech/os-greeting-changer-antigravity-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/antigravity/os-greeting-changer .agent/skills/os-greeting-changer
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/antigravity/os-greeting-changer .agent/skills/os-greeting-changer
```

配置後、Antigravity を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Antigravity: https://codelabs.developers.google.com/getting-started-with-antigravity-skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
