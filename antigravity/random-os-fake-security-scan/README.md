# random-os-fake-security-scan

> 作業中やターミナル操作時などに「セキュリティスキャン」や「警告」などのキーワードが含まれる状況で、AntigravityがフェイクなOSセキュリティ通知を自動表示し、進捗バー付きの演出でユーザーの集中を攪乱します。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Antigravity** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/fake_security_scan.py` - Fake OS Security Scan Notifier
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Antigravity 向け random-os-fake-security-scan の詳しい説明](https://ai-note.tech/random-os-fake-security-scan-antigravity/)
- 動作手順: [Antigravity で実際に動かす手順と検証](https://ai-note.tech/random-os-fake-security-scan-antigravity-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/antigravity/random-os-fake-security-scan .agent/skills/random-os-fake-security-scan
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/antigravity/random-os-fake-security-scan .agent/skills/random-os-fake-security-scan
```

配置後、Antigravity を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Antigravity: https://codelabs.developers.google.com/getting-started-with-antigravity-skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
