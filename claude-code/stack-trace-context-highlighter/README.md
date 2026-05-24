# stack-trace-context-highlighter

> Claude Codeがエラー発生時やスタックトレース出力を検知した際、関連する関数名・ファイル名を自動抽出し、現在開いているファイルや直近の編集箇所と突き合わせて注目箇所をハイライト表示する際に発動します。エラー解析やデバッグ時に有効です。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Claude Code** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/stack_trace_context_highlighter.py` - 実行スクリプト
- `references/design_notes.md` - 参考資料

## 関連記事

- スキル詳細説明: [Claude Code 向け stack-trace-context-highlighter の詳しい説明](https://ai-note.tech/stack-trace-context-highlighter-claude-code/)
- 動作手順: [Claude Code で実際に動かす手順と検証](https://ai-note.tech/stack-trace-context-highlighter-claude-code-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/claude-code/stack-trace-context-highlighter .claude/skills/stack-trace-context-highlighter
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/claude-code/stack-trace-context-highlighter .claude/skills/stack-trace-context-highlighter
```

配置後、Claude Code を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Claude Code: https://code.claude.com/docs/ja/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
