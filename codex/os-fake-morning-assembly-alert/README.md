# os-fake-morning-assembly-alert

> Codexがターミナルやエディタの初回起動時、または/skillsコマンドやos-fake-morning-assembly-alertの明示呼び出し時に発動。朝礼・点呼・スローガンなどの“謎通知”を毎回異なる内容で表示し、作業開始を演出します。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Codex** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/os_fake_morning_assembly_alert.py` - \nOS Fake Morning Assembly Alert\n\nコマンド例:\n  python os_fake_morning_assembly_alert.py aut
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Codex 向け os-fake-morning-assembly-alert の詳しい説明](https://ai-note.tech/os-fake-morning-assembly-alert-codex/)
- 動作手順: [Codex で実際に動かす手順と検証](https://ai-note.tech/os-fake-morning-assembly-alert-codex-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/codex/os-fake-morning-assembly-alert .agents/skills/os-fake-morning-assembly-alert
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/codex/os-fake-morning-assembly-alert .agents/skills/os-fake-morning-assembly-alert
```

配置後、Codex を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Codex: https://developers.openai.com/codex/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
