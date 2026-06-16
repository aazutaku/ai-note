# command-failure-excuse-notifier

> コマンド実行やスクリプト動作時にエラーや失敗メッセージが発生した場合、このSkillは自動的にOSの通知領域へ“言い訳”メッセージを表示します。失敗・エラー・例外・command not found・exit code!=0 などのキーワードが検知された際に発動します。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Antigravity** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/command_failure_excuse_notifier.py` - 指定コマンドを実行し、失敗時に言い訳通知を送る
- `references/reference.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Antigravity 向け command-failure-excuse-notifier の詳しい説明](https://ai-note.tech/command-failure-excuse-notifier-antigravity/)
- 動作手順: [Antigravity で実際に動かす手順と検証](https://ai-note.tech/command-failure-excuse-notifier-antigravity-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/antigravity/command-failure-excuse-notifier .agent/skills/command-failure-excuse-notifier
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/antigravity/command-failure-excuse-notifier .agent/skills/command-failure-excuse-notifier
```

配置後、Antigravity を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Antigravity: https://codelabs.developers.google.com/getting-started-with-antigravity-skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
