# random-os-fake-update-progrebar

> ターミナルやエディタでコマンド実行時や明示的な /random-os-fake-update-progrebar 呼び出し時に、毎回異なる“謎のOSアップデート進捗バー”を画面端にランダム表示します。進捗内容は完全無意味で、100%到達時も何も起きません。作業の合間に緊張感を和らげたい時に有効です。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Claude Code** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/random_os_fake_update_progrebar.py` - 謎のOSアップデート進捗バーをランダム表示する無駄スキル
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Claude Code 向け random-os-fake-update-progrebar の詳しい説明](https://ai-note.tech/random-os-fake-update-progrebar-claude-code/)
- 動作手順: [Claude Code で実際に動かす手順と検証](https://ai-note.tech/random-os-fake-update-progrebar-claude-code-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/claude-code/random-os-fake-update-progrebar .claude/skills/random-os-fake-update-progrebar
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/claude-code/random-os-fake-update-progrebar .claude/skills/random-os-fake-update-progrebar
```

配置後、Claude Code を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Claude Code: https://code.claude.com/docs/ja/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
