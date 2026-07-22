# random-os-fake-power-saver-alert

> 作業中や集中タイムに“パワーセーバー警告”のような偽OS通知をランダムに炸裂させ、職場や自宅の雰囲気を一変させたいときに発動。『省エネ』『警告』『通知』『パワーセーブ』『休憩』などのキーワードや、/random-os-fake-power-saver-alert コマンドで明示的にも起動可能。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Claude Code** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/random_os_fake_power_saver_alert.py` - ランダムな偽OSパワーセーバー警告をデスクトップ通知で表示します。
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Claude Code 向け random-os-fake-power-saver-alert の詳しい説明](https://ai-note.tech/random-os-fake-power-saver-alert-claude-code/)
- 動作手順: [Claude Code で実際に動かす手順と検証](https://ai-note.tech/random-os-fake-power-saver-alert-claude-code-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/claude-code/random-os-fake-power-saver-alert .claude/skills/random-os-fake-power-saver-alert
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/claude-code/random-os-fake-power-saver-alert .claude/skills/random-os-fake-power-saver-alert
```

配置後、Claude Code を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Claude Code: https://code.claude.com/docs/ja/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
