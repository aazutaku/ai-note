# os-fake-coffee-break-sound-effect

> このSkillは、Antigravityがコマンド実行や作業中に“コーヒーブレイク”を演出したい場合に発動します。トリガー条件は「休憩」「集中」「疲労」「カフェイン」「リフレッシュ」などのキーワードや、連続作業・長時間稼働時です。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Antigravity** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/coffee_break_notifier.py` - Fake Coffee Break Notifier
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Antigravity 向け os-fake-coffee-break-sound-effect の詳しい説明](https://ai-note.tech/os-fake-coffee-break-sound-effect-antigravity/)
- 動作手順: [Antigravity で実際に動かす手順と検証](https://ai-note.tech/os-fake-coffee-break-sound-effect-antigravity-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/antigravity/os-fake-coffee-break-sound-effect .agent/skills/os-fake-coffee-break-sound-effect
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/antigravity/os-fake-coffee-break-sound-effect .agent/skills/os-fake-coffee-break-sound-effect
```

配置後、Antigravity を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Antigravity: https://codelabs.developers.google.com/getting-started-with-antigravity-skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
