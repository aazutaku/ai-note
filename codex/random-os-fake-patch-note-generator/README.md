# random-os-fake-patch-note-generator

> Codexは、ユーザーがコマンド実行・ファイル保存・ビルド・テスト・/skillsメニュー呼び出し等のタイミングで本Skillを発動し、毎回異なる“偽OSパッチノート”を通知またはターミナル出力してください。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Codex** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/random_os_fake_patch_note_generator.py` - Random OS Fake Patch Note Generator
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Codex 向け random-os-fake-patch-note-generator の詳しい説明](https://ai-note.tech/random-os-fake-patch-note-generator-codex/)
- 動作手順: [Codex で実際に動かす手順と検証](https://ai-note.tech/random-os-fake-patch-note-generator-codex-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/codex/random-os-fake-patch-note-generator .agents/skills/random-os-fake-patch-note-generator
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/codex/random-os-fake-patch-note-generator .agents/skills/random-os-fake-patch-note-generator
```

配置後、Codex を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Codex: https://developers.openai.com/codex/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
