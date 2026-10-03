# random-os-fake-mysterious-soundtrack-alert

> 作業中やコマンド実行時、もしくは/skillsメニュー呼び出し時に、Codexが“謎のOS公式BGM推奨通知”をランダムに発動します。通知はジャンル不明の独自BGMタイトルを生成し、音は鳴らず演出のみ。気分転換や小ネタ投入に最適です。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Codex** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/mysterious_soundtrack_alert.py` - 謎のOS公式BGM推奨通知スクリプト
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Codex 向け random-os-fake-mysterious-soundtrack-alert の詳しい説明](https://ai-note.tech/random-os-fake-mysterious-soundtrack-alert-codex/)
- 動作手順: [Codex で実際に動かす手順と検証](https://ai-note.tech/random-os-fake-mysterious-soundtrack-alert-codex-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/codex/random-os-fake-mysterious-soundtrack-alert .agents/skills/random-os-fake-mysterious-soundtrack-alert
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/codex/random-os-fake-mysterious-soundtrack-alert .agents/skills/random-os-fake-mysterious-soundtrack-alert
```

配置後、Codex を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Codex: https://developers.openai.com/codex/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
