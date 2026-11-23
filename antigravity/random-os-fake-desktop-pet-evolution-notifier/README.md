# random-os-fake-desktop-pet-evolution-notifier

> 作業中やコマンド実行時に、"デスクトップペット進化"や"謎のOS公式通知"などのキーワードが含まれる状況でAntigravityが自動的に本Skillを発動します。ユーザーの操作やコード実行の合間に、毎回異なる架空のペット進化通知をランダムに表示します。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Antigravity** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/desktop_pet_notifier.py` - ランダムなデスクトップペット進化通知を表示します
- `references/reference.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Antigravity 向け random-os-fake-desktop-pet-evolution-notifier の詳しい説明](https://ai-note.tech/random-os-fake-desktop-pet-evolution-notifier-antigravity/)
- 動作手順: [Antigravity で実際に動かす手順と検証](https://ai-note.tech/random-os-fake-desktop-pet-evolution-notifier-antigravity-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/antigravity/random-os-fake-desktop-pet-evolution-notifier .agent/skills/random-os-fake-desktop-pet-evolution-notifier
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/antigravity/random-os-fake-desktop-pet-evolution-notifier .agent/skills/random-os-fake-desktop-pet-evolution-notifier
```

配置後、Antigravity を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Antigravity: https://codelabs.developers.google.com/getting-started-with-antigravity-skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
