# random-os-mystery-sound-effect

> コマンド実行やファイル操作、プロジェクトビルドなどのアクション時に、毎回ランダムな“謎のOS公式サウンドエフェクト”を鳴らすことで、開発現場にシュールな混乱や笑いを演出したい場合に発動します。triggerType: always/semantic。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Claude Code** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/random_os_mystery_sound_effect.py` - ランダムOS謎サウンドエフェクト Skill
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Claude Code 向け random-os-mystery-sound-effect の詳しい説明](https://ai-note.tech/random-os-mystery-sound-effect-claude-code/)
- 動作手順: [Claude Code で実際に動かす手順と検証](https://ai-note.tech/random-os-mystery-sound-effect-claude-code-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/claude-code/random-os-mystery-sound-effect .claude/skills/random-os-mystery-sound-effect
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/claude-code/random-os-mystery-sound-effect .claude/skills/random-os-mystery-sound-effect
```

配置後、Claude Code を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Claude Code: https://code.claude.com/docs/ja/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
