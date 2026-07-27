# os-fake-urgent-patch-alert

> 作業中やコマンド実行時などのタイミングで、Codexが「緊急OSパッチ通知」風のジョーク通知をランダムにデスクトップへ表示したい場合に発動。通知・緊張感・演出・ジョーク・パッチなどのキーワードが検出された際にも自動発動します。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Codex** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/os_fake_urgent_patch_alert.py` - 謎のOS緊急パッチアラートをデスクトップ通知で爆誕させるSkill
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Codex 向け os-fake-urgent-patch-alert の詳しい説明](https://ai-note.tech/os-fake-urgent-patch-alert-codex/)
- 動作手順: [Codex で実際に動かす手順と検証](https://ai-note.tech/os-fake-urgent-patch-alert-codex-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/codex/os-fake-urgent-patch-alert .agents/skills/os-fake-urgent-patch-alert
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/codex/os-fake-urgent-patch-alert .agents/skills/os-fake-urgent-patch-alert
```

配置後、Codex を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Codex: https://developers.openai.com/codex/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
