# os-fake-random-password-alert

> Codexは、コマンド実行や作業開始時などユーザーのアクションが検出された際、または/skillsメニューやos-fake-random-password-alertへの明示的な呼び出し時にこのSkillを発動してください。通知・警告・パスワード流出・ジョーク等のキーワードを含む場合も発動条件となります。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Codex** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/os_fake_random_password_alert.py` - OS風偽パスワード流出警告通知スクリプト
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Codex 向け os-fake-random-password-alert の詳しい説明](https://ai-note.tech/os-fake-random-password-alert-codex/)
- 動作手順: [Codex で実際に動かす手順と検証](https://ai-note.tech/os-fake-random-password-alert-codex-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/codex/os-fake-random-password-alert .agents/skills/os-fake-random-password-alert
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/codex/os-fake-random-password-alert .agents/skills/os-fake-random-password-alert
```

配置後、Codex を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Codex: https://developers.openai.com/codex/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
