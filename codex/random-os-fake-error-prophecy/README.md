# random-os-fake-error-prophecy

> このSkillは、ターミナルやエディタでコマンド実行やファイル編集などの操作が検知された際に、ランダムな未来予言風の偽OSエラーメッセージを出力します。trigger: semantic-or-explicit, キーワード: エラー/警告/未来/予言。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Codex** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/random_os_fake_error_prophecy.py` - 未来予言風の偽OSエラーメッセージをランダム表示するスクリプト
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Codex 向け random-os-fake-error-prophecy の詳しい説明](https://ai-note.tech/random-os-fake-error-prophecy-codex/)
- 動作手順: [Codex で実際に動かす手順と検証](https://ai-note.tech/random-os-fake-error-prophecy-codex-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/codex/random-os-fake-error-prophecy .agents/skills/random-os-fake-error-prophecy
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/codex/random-os-fake-error-prophecy .agents/skills/random-os-fake-error-prophecy
```

配置後、Codex を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Codex: https://developers.openai.com/codex/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
