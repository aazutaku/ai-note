# random-os-fake-reboot-progressbar

> 作業に没頭しすぎている時や、冗談やリセット感を演出したいタイミングで発動。再起動・進捗・リセット・OS・プロセス・バー・冗談・混乱 などのキーワードが会話やコマンドに含まれる場合に適切。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Codex** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/fake_reboot_progressbar.py` - 謎のOS再起動進捗バーをランダムに表示するスクリプト (冗談用)
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Codex 向け random-os-fake-reboot-progressbar の詳しい説明](https://ai-note.tech/random-os-fake-reboot-progressbar-codex/)
- 動作手順: [Codex で実際に動かす手順と検証](https://ai-note.tech/random-os-fake-reboot-progressbar-codex-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/codex/random-os-fake-reboot-progressbar .agents/skills/random-os-fake-reboot-progressbar
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/codex/random-os-fake-reboot-progressbar .agents/skills/random-os-fake-reboot-progressbar
```

配置後、Codex を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Codex: https://developers.openai.com/codex/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
