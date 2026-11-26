# random-os-fake-mysterious-background-process-alert

> ユーザーが『バックグラウンド』『通知』『プロセス』『怪しい』『OS警告』『進捗』『監視』『解析』『意味不明』などのキーワードを含む会話やコマンドを実行した際、または明示的にSkillを呼び出した際に発動します。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Codex** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/mysterious_process_alert.py` - 謎のOS風バックグラウンドプロセス通知をランダムに生成・表示します。
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Codex 向け random-os-fake-mysterious-background-process-alert の詳しい説明](https://ai-note.tech/random-os-fake-mysterious-background-process-alert-codex/)
- 動作手順: [Codex で実際に動かす手順と検証](https://ai-note.tech/random-os-fake-mysterious-background-process-alert-codex-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/codex/random-os-fake-mysterious-background-process-alert .agents/skills/random-os-fake-mysterious-background-process-alert
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/codex/random-os-fake-mysterious-background-process-alert .agents/skills/random-os-fake-mysterious-background-process-alert
```

配置後、Codex を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Codex: https://developers.openai.com/codex/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
