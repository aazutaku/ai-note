# random-os-panic-alert

> 作業やコーディング中に『panic』『OSエラー』『クラッシュ』『アラート』などのキーワード検出時、または明示的なSkill呼び出し時に発動。現実には起こり得ない、ユーモラスなOSパニック通知をデスクトップに表示します。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Codex** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/random_os_panic_alert.py` - Random OS Panic Alert - 珍妙なOSパニック通知を表示します
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Codex 向け random-os-panic-alert の詳しい説明](https://ai-note.tech/random-os-panic-alert-codex/)
- 動作手順: [Codex で実際に動かす手順と検証](https://ai-note.tech/random-os-panic-alert-codex-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/codex/random-os-panic-alert .agents/skills/random-os-panic-alert
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/codex/random-os-panic-alert .agents/skills/random-os-panic-alert
```

配置後、Codex を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Codex: https://developers.openai.com/codex/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
