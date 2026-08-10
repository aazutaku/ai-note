# os-fake-coffee-break-sound-effect

> このSkillは、Claude Codeがコマンド実行や作業の節目（例: ビルド/テスト/デプロイ/長時間作業）を検知した際や、/os-fake-coffee-break-sound-effect の明示呼び出し時に発動します。通知・サウンド演出を通じて“強制コーヒーブレイク”を演出します。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Claude Code** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/coffee_break_sound_effect.py` - OS風フェイク・コーヒーブレイクサウンド&通知スキル
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Claude Code 向け os-fake-coffee-break-sound-effect の詳しい説明](https://ai-note.tech/os-fake-coffee-break-sound-effect-claude-code/)
- 動作手順: [Claude Code で実際に動かす手順と検証](https://ai-note.tech/os-fake-coffee-break-sound-effect-claude-code-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/claude-code/os-fake-coffee-break-sound-effect .claude/skills/os-fake-coffee-break-sound-effect
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/claude-code/os-fake-coffee-break-sound-effect .claude/skills/os-fake-coffee-break-sound-effect
```

配置後、Claude Code を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Claude Code: https://code.claude.com/docs/ja/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
