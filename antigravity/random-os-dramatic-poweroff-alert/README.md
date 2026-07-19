# random-os-dramatic-poweroff-alert

> 作業やコーディング中に“シャットダウン予告”や“電源オフ警告”などのキーワードが含まれるコンテキストを検知した際、AntigravityがこのSkillを発動し、壮大かつカオスな電源オフ通知をデスクトップに表示します。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Antigravity** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/dramatic_poweroff_alert.py` - Dramatic Poweroff Alert - OS電源オフの壮大な予告を通知で爆誕させる
- `references/reference.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Antigravity 向け random-os-dramatic-poweroff-alert の詳しい説明](https://ai-note.tech/random-os-dramatic-poweroff-alert-antigravity/)
- 動作手順: [Antigravity で実際に動かす手順と検証](https://ai-note.tech/random-os-dramatic-poweroff-alert-antigravity-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/antigravity/random-os-dramatic-poweroff-alert .agent/skills/random-os-dramatic-poweroff-alert
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/antigravity/random-os-dramatic-poweroff-alert .agent/skills/random-os-dramatic-poweroff-alert
```

配置後、Antigravity を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Antigravity: https://codelabs.developers.google.com/getting-started-with-antigravity-skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
