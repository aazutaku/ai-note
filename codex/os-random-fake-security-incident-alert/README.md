# os-random-fake-security-incident-alert

> 作業中や会話中に「セキュリティ」「ウイルス」「インシデント」「OS」などのキーワードが出現した際、または/skillsメニューや明示的な呼び出しで、爆笑フェイクOSインシデント通知をランダムに生成・発火します。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Codex** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/fake_security_incident_alert.py` - 爆笑フェイクOSセキュリティインシデント通知スクリプト
- `references/reference.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Codex 向け os-random-fake-security-incident-alert の詳しい説明](https://ai-note.tech/os-random-fake-security-incident-alert-codex/)
- 動作手順: [Codex で実際に動かす手順と検証](https://ai-note.tech/os-random-fake-security-incident-alert-codex-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/codex/os-random-fake-security-incident-alert .agents/skills/os-random-fake-security-incident-alert
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/codex/os-random-fake-security-incident-alert .agents/skills/os-random-fake-security-incident-alert
```

配置後、Codex を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Codex: https://developers.openai.com/codex/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
