# random-os-nap-detection-alert

> ユーザーが30秒以上無操作状態になった場合に、ランダムな“お昼寝検出”メッセージをデスクトップ通知やターミナルに表示するSkillです。『うたた寝モード突入』などのツッコミ系通知で集中力低下やサボりを検出し、職場や作業現場で気まずい笑いを誘発します。コマンド入力やエディタ操作の監視がトリガー条件です。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Codex** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/random_os_nap_detection_alert.py` - random-os-nap-detection-alert: 30秒以上無操作でお昼寝アラートを通知
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Codex 向け random-os-nap-detection-alert の詳しい説明](https://ai-note.tech/random-os-nap-detection-alert-codex/)
- 動作手順: [Codex で実際に動かす手順と検証](https://ai-note.tech/random-os-nap-detection-alert-codex-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/codex/random-os-nap-detection-alert .agents/skills/random-os-nap-detection-alert
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/codex/random-os-nap-detection-alert .agents/skills/random-os-nap-detection-alert
```

配置後、Codex を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Codex: https://developers.openai.com/codex/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
