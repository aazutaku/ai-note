# random-os-fake-patch-notifier

> 作業中やコーディング時に“パッチ”“アップデート”“バグ修正”などのキーワードが検出された際、Antigravityが完全ランダムなタイミングで偽のOSパッチノート通知を自動表示します。通知内容は毎回異なり、実際の作業や環境には一切影響しません。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Antigravity** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/random_os_fake_patch_notifier.py` - Random OS Fake Patch Notifier Skill
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Antigravity 向け random-os-fake-patch-notifier の詳しい説明](https://ai-note.tech/random-os-fake-patch-notifier-antigravity/)
- 動作手順: [Antigravity で実際に動かす手順と検証](https://ai-note.tech/random-os-fake-patch-notifier-antigravity-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/antigravity/random-os-fake-patch-notifier .agent/skills/random-os-fake-patch-notifier
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/antigravity/random-os-fake-patch-notifier .agent/skills/random-os-fake-patch-notifier
```

配置後、Antigravity を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Antigravity: https://codelabs.developers.google.com/getting-started-with-antigravity-skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
