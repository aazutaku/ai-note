# random-os-fake-disk-space-crisis

> 作業やコーディング中に“ディスク残量危機”を装った現実離れしたジョーク通知をランダム表示します。『ディスク容量』『空き領域』『容量不足』などのキーワードや /random-os-fake-disk-space-crisis コマンドで発動します。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Claude Code** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/fake_disk_crisis.py` - 謎のOSディスク残量危機通知をランダムに生成して表示します。
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Claude Code 向け random-os-fake-disk-space-crisis の詳しい説明](https://ai-note.tech/random-os-fake-disk-space-crisis-claude-code/)
- 動作手順: [Claude Code で実際に動かす手順と検証](https://ai-note.tech/random-os-fake-disk-space-crisis-claude-code-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/claude-code/random-os-fake-disk-space-crisis .claude/skills/random-os-fake-disk-space-crisis
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/claude-code/random-os-fake-disk-space-crisis .claude/skills/random-os-fake-disk-space-crisis
```

配置後、Claude Code を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Claude Code: https://code.claude.com/docs/ja/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
