# shindan-file-cupid

> プロジェクト内のファイル名リストをもとに、ファイル同士の謎の相性診断を行いたい時に発動します。ファイルペアの相性や診断理由をランダム・ジョーク的に出力したい場合や、アイスブレイクや会話のネタが必要な場面で有効です。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Claude Code** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/cupid_diagnoser.py` - 診断ファイルキューピッド: ファイル同士の謎相性診断
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Claude Code 向け shindan-file-cupid の詳しい説明](https://ai-note.tech/shindan-file-cupid-claude-code/)
- 動作手順: [Claude Code で実際に動かす手順と検証](https://ai-note.tech/shindan-file-cupid-claude-code-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/claude-code/shindan-file-cupid .claude/skills/shindan-file-cupid
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/claude-code/shindan-file-cupid .claude/skills/shindan-file-cupid
```

配置後、Claude Code を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Claude Code: https://code.claude.com/docs/ja/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
