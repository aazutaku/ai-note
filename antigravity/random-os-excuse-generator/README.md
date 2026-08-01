# random-os-excuse-generator

> エラーやビルド失敗、実行時バグ、謎の挙動などの発生時に、Antigravityが自動で“根拠のないおもしろ言い訳”をデスクトップ通知やターミナル出力で生成・表示します。『バグ』『失敗』『エラー』『動かない』『クラッシュ』などのキーワード検知時に発動。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Antigravity** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/random_os_excuse_generator.py` - random-os-excuse-generator: 謎のOS言い訳を生成します
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Antigravity 向け random-os-excuse-generator の詳しい説明](https://ai-note.tech/random-os-excuse-generator-antigravity/)
- 動作手順: [Antigravity で実際に動かす手順と検証](https://ai-note.tech/random-os-excuse-generator-antigravity-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/antigravity/random-os-excuse-generator .agent/skills/random-os-excuse-generator
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/antigravity/random-os-excuse-generator .agent/skills/random-os-excuse-generator
```

配置後、Antigravity を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Antigravity: https://codelabs.developers.google.com/getting-started-with-antigravity-skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
