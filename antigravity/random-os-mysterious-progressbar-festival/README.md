# random-os-mysterious-progressbar-festival

> Antigravity がターミナル/エディタでコマンド実行やファイル保存などの操作を検知した際、「進捗」「バグ」「会議」などのキーワードを含む場合に自動発動。複数のランダムな進捗バーを画面端に表示し、作業中の緊張を和らげます。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Antigravity** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/mysterious_progressbar_festival.py` - 謎のOS進捗バー祭りスクリプト
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Antigravity 向け random-os-mysterious-progressbar-festival の詳しい説明](https://ai-note.tech/random-os-mysterious-progressbar-festival-antigravity/)
- 動作手順: [Antigravity で実際に動かす手順と検証](https://ai-note.tech/random-os-mysterious-progressbar-festival-antigravity-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/antigravity/random-os-mysterious-progressbar-festival .agent/skills/random-os-mysterious-progressbar-festival
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/antigravity/random-os-mysterious-progressbar-festival .agent/skills/random-os-mysterious-progressbar-festival
```

配置後、Antigravity を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Antigravity: https://codelabs.developers.google.com/getting-started-with-antigravity-skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
