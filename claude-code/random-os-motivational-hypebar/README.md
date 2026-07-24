# random-os-motivational-hypebar

> コマンド実行時やエディタ操作時など、ユーザーの作業アクションに反応し、毎回ランダムな“自己肯定感ハイプバー”を画面端やメニューバーに表示します。パラメータ名・数値は完全にランダムかつ意味不明で、進捗や成果には一切関係ありません。明示呼び出しは /random-os-motivational-hypebar で可能です。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Claude Code** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/hypebar.py` - OS自己肯定感ハイプバー
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Claude Code 向け random-os-motivational-hypebar の詳しい説明](https://ai-note.tech/random-os-motivational-hypebar-claude-code/)
- 動作手順: [Claude Code で実際に動かす手順と検証](https://ai-note.tech/random-os-motivational-hypebar-claude-code-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/claude-code/random-os-motivational-hypebar .claude/skills/random-os-motivational-hypebar
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/claude-code/random-os-motivational-hypebar .claude/skills/random-os-motivational-hypebar
```

配置後、Claude Code を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Claude Code: https://code.claude.com/docs/ja/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
