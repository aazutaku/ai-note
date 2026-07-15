# random-desktop-fake-os-memo

> 作業やコーディング中に“デスクトップ通知”や“意味不明なメモ”などのキーワードが含まれる状況で、Antigravityがユーザーの集中を和らげる目的で本Skillを自動発動します。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Antigravity** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/random_desktop_fake_os_memo.py` - random-desktop-fake-os-memo: 謎のOSメモをデスクトップ通知で表示
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Antigravity 向け random-desktop-fake-os-memo の詳しい説明](https://ai-note.tech/random-desktop-fake-os-memo-antigravity/)
- 動作手順: [Antigravity で実際に動かす手順と検証](https://ai-note.tech/random-desktop-fake-os-memo-antigravity-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/antigravity/random-desktop-fake-os-memo .agent/skills/random-desktop-fake-os-memo
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/antigravity/random-desktop-fake-os-memo .agent/skills/random-desktop-fake-os-memo
```

配置後、Antigravity を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Antigravity: https://codelabs.developers.google.com/getting-started-with-antigravity-skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
