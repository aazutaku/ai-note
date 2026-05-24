---
name: stack-trace-context-highlighter
description: Claude Codeがエラー発生時やスタックトレース出力を検知した際、関連する関数名・ファイル名を自動抽出し、現在開いているファイルや直近の編集箇所と突き合わせて注目箇所をハイライト表示する際に発動します。エラー解析やデバッグ時に有効です。
---

# 機能概要
本Skillは、エラー発生時のスタックトレースから関数名やファイル名を自動で抽出し、現在の作業コンテキスト（例：エディタで開いているファイル、直近の編集箇所）と突き合わせて、注目すべき箇所をハイライト表示します。これにより、膨大なファイルや関数が存在するプロジェクトでも、エラー原因候補へ即座にナビゲートでき、デバッグ効率が大幅に向上します。特殊な依存や環境構築も不要で、エディタやターミナル上の情報のみを利用します。

# 使い方
- 明示呼び出し例：`/stack-trace-context-highlighter --trace-file error.log --open-files main.py utils.py --recent-edits main.py:42,utils.py:15`
- 暗黙発動キーワード例：「Traceback」、「スタックトレース」、「Exception」、「エラー発生」などの出力を検知した際に自動発動します。

# 出力例
```
[stack-trace-context-highlighter] ハイライト候補:
- main.py:42 (open, recent edit)
- utils.py:15 (open, recent edit)
- config.py:88 (not open)

注目: main.py:42, utils.py:15
```

# 注意点
- スタックトレースの形式（Python, Node.js, Java等）によっては抽出精度が異なります。
- ローカルで開いているファイルや編集履歴の取得は、エディタやターミナルの連携状況に依存します。
- 除外パスや一時ファイルは自動で無視されますが、完全ではありません。
- ローカルにファイルや履歴を保存することはありません。

# 参考資料
詳細な設計方針や利用例は references/design_notes.md を参照してください。Python公式のtraceback解析（https://docs.python.org/ja/3/library/traceback.html）や、各種エディタのファイル管理仕様も参考にしています。