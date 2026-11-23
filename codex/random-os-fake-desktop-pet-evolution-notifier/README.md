# random-os-fake-desktop-pet-evolution-notifier

> 作業中に“デスクトップペット進化通知”でユーザーを驚かせたい場合や、ターミナル/デスクトップに遊び心ある通知をランダム表示したい時に発動。通知・演出・OS連携・ランダム・ペット・進化・ジョーク等のキーワード検知時に有効。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Codex** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/pet_evolution_notifier.py` - 謎のOS公式デスクトップペット進化通知をランダムで炸裂させるスクリプト
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Codex 向け random-os-fake-desktop-pet-evolution-notifier の詳しい説明](https://ai-note.tech/random-os-fake-desktop-pet-evolution-notifier-codex/)
- 動作手順: [Codex で実際に動かす手順と検証](https://ai-note.tech/random-os-fake-desktop-pet-evolution-notifier-codex-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/codex/random-os-fake-desktop-pet-evolution-notifier .agents/skills/random-os-fake-desktop-pet-evolution-notifier
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/codex/random-os-fake-desktop-pet-evolution-notifier .agents/skills/random-os-fake-desktop-pet-evolution-notifier
```

配置後、Codex を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Codex: https://developers.openai.com/codex/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
