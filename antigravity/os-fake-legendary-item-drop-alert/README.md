# os-fake-legendary-item-drop-alert

> ユーザーが集中して作業している際や長時間コーディング中など、Antigravityが『気分転換』『リフレッシュ』『集中力維持』などのキーワードや状況を検知した場合に発動。作業の合間や区切りに遊び心ある通知を表示します。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Antigravity** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/legendary_item_drop_alert.py` - 伝説アイテムドロップ通知スクリプト
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Antigravity 向け os-fake-legendary-item-drop-alert の詳しい説明](https://ai-note.tech/os-fake-legendary-item-drop-alert-antigravity/)
- 動作手順: [Antigravity で実際に動かす手順と検証](https://ai-note.tech/os-fake-legendary-item-drop-alert-antigravity-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/antigravity/os-fake-legendary-item-drop-alert .agent/skills/os-fake-legendary-item-drop-alert
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/antigravity/os-fake-legendary-item-drop-alert .agent/skills/os-fake-legendary-item-drop-alert
```

配置後、Antigravity を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Antigravity: https://codelabs.developers.google.com/getting-started-with-antigravity-skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
