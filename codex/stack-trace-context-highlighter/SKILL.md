---
name: stack-trace-context-highlighter
description: エラー発生時にスタックトレースやTracebackが出力された場合、またはユーザーがデバッグ目的で明示的に呼び出した場合に発動。キーワード例: Traceback, Exception, stack trace, error, debug。
---

# 機能概要
stack-trace-context-highlighterは、プログラム実行時のエラーで出力されたスタックトレース（Traceback）から、関係する関数名やファイル名を自動抽出し、現在開いているファイルや直近の編集箇所と突き合わせて、注目すべき箇所をハイライト表示します。これにより、作業ファイルが多い大規模プロジェクトでも、原因箇所への迅速なナビゲーションが可能となり、デバッグ効率が大幅に向上します。環境構築や特殊な依存は不要で、エディタやターミナル上の情報のみを活用します。

# 使い方
- 明示的な呼び出し: `/skills stack-trace-context-highlighter` または Skill メニューから選択。
- 暗黙発動: エラー出力や "Traceback (most recent call last):"、"Exception"、"stack trace" などのキーワードを含むログやターミナル出力が認識された場合に自動発動。

# 出力例
```
[stack-trace-context-highlighter]
- 関連ファイル: src/utils/data_loader.py (編集中), src/main.py
- 注目関数: load_data (行42), main (行10)
- 推奨ナビゲート: src/utils/data_loader.py:42  (現在の編集箇所と一致)
- スタックトレース抜粋:
  File "src/utils/data_loader.py", line 42, in load_data
    raise ValueError("Invalid format")
```

# 注意点
- サポート形式は標準的なPythonスタックトレース。Go, Java等の他言語は一部対応。
- ローカルで開いているファイル情報取得はエディタ連携APIや環境変数経由。
- ログが断片的な場合や、ファイルパスが省略されている場合は精度が低下することがあります。
- ローカルファイルの保存や自動修正は行いません。

# 参考資料
- [Python公式: Tracebackオブジェクト](https://docs.python.org/ja/3/library/traceback.html)
- references/design_notes.md を参照