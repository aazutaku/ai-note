# os-fake-holiday-announcer

> 作業がマンネリ化・集中力が低下した際や、/skills menu から明示的に呼び出されたときに発動。通知・休暇・祝日・業務停止・休み・サボり等のキーワードを含む状況で、開発者の気分転換やリフレッシュを促すために利用されます。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Codex** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/os_fake_holiday_announcer.py` - os-fake-holiday-announcer: OSが謎の休日を勝手に宣言する通知演出ツール
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Codex 向け os-fake-holiday-announcer の詳しい説明](https://ai-note.tech/os-fake-holiday-announcer-codex/)
- 動作手順: [Codex で実際に動かす手順と検証](https://ai-note.tech/os-fake-holiday-announcer-codex-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/codex/os-fake-holiday-announcer .agents/skills/os-fake-holiday-announcer
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/codex/os-fake-holiday-announcer .agents/skills/os-fake-holiday-announcer
```

配置後、Codex を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Codex: https://developers.openai.com/codex/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
