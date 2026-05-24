# stack-trace-context-highlighter

> エラー発生時にスタックトレースやTracebackが出力された場合、またはユーザーがデバッグ目的で明示的に呼び出した場合に発動。キーワード例: Traceback, Exception, stack trace, error, debug。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Codex** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/stack_trace_context_highlighter.py` - 実行スクリプト
- `references/design_notes.md` - 参考資料

## 関連記事

- スキル詳細説明: [Codex 向け stack-trace-context-highlighter の詳しい説明](https://ai-note.tech/stack-trace-context-highlighter-codex/)
- 動作手順: [Codex で実際に動かす手順と検証](https://ai-note.tech/stack-trace-context-highlighter-codex-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/codex/stack-trace-context-highlighter .agents/skills/stack-trace-context-highlighter
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/codex/stack-trace-context-highlighter .agents/skills/stack-trace-context-highlighter
```

配置後、Codex を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Codex: https://developers.openai.com/codex/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
