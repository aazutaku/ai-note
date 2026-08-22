# random-os-fake-system-pet-interruption

> ユーザーが作業やコーディングに集中している際、“ペット”に関する語や長時間の無操作・集中状態を検知した場合に、完全ランダムなOS風ペット乱入イベントを自動で発生させます。癒しや混乱を演出し、集中リセットを促します。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Antigravity** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/pet_interruption.py` - 監視対象のログファイルからキーワードを検出
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Antigravity 向け random-os-fake-system-pet-interruption の詳しい説明](https://ai-note.tech/random-os-fake-system-pet-interruption-antigravity/)
- 動作手順: [Antigravity で実際に動かす手順と検証](https://ai-note.tech/random-os-fake-system-pet-interruption-antigravity-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/antigravity/random-os-fake-system-pet-interruption .agent/skills/random-os-fake-system-pet-interruption
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/antigravity/random-os-fake-system-pet-interruption .agent/skills/random-os-fake-system-pet-interruption
```

配置後、Antigravity を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Antigravity: https://codelabs.developers.google.com/getting-started-with-antigravity-skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
