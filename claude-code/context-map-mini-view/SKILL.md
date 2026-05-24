---
name: context-map-mini-view
description: Claude Codeがプロジェクト全体の構造や主要ファイルの関係性を即座に把握する必要があるとき、または「コンテキスト」「全体像」「依存関係」などのキーワードを検知した際に発動します。明示的なコマンド呼び出し（/context-map-mini-view）にも対応します。
---

# 機能概要
context-map-mini-viewは、プロジェクトの主要ディレクトリ・ファイル構成と、それぞれの役割や関連性を自動で要約し、作業中のファイルとの関係まで可視化するミニビューを生成します。初見のリポジトリや複雑なプロジェクトで「どこに何があるか」「今触っているファイルが全体にどう影響するか」を一目で把握でき、迷子防止や効率的な開発を支援します。

# 使い方
- 明示呼び出し例:
  `/context-map-mini-view` もしくは `/context-map-mini-view path/to/file.py`
- 暗黙発動キーワード例:
  「全体構造」「依存関係」「どこにありますか」「このファイルの役割」「プロジェクトマップ」などを含む発言時に自動発動します。

# 出力例
```
[Context Map Mini View]
project-root/
├── src/         # アプリケーション本体
│   ├── main.py  # エントリポイント（全体の起動）
│   └── utils.py # 補助関数群（main.pyから呼び出し）
├── tests/       # テストコード
│   └── test_main.py (main.pyのテスト)
├── README.md    # プロジェクト概要

[現在のファイル: src/main.py]
- 依存: src/utils.py
- 影響範囲: tests/test_main.py
```

# 注意点
- .gitignoreや除外設定に従い、一時ファイルや依存ライブラリは除外されます。
- 既存のREADMEやPROJECT_MAPがあれば内容を優先的に参照します。
- ローカルでのみ実行され、外部に内容を送信しません。
- 複雑な循環依存や巨大プロジェクトでは要約が簡略化される場合があります。

# 参考資料
- references/design_notes.md に設計方針や適用例を記載
- 公式: https://docs.python.org/3/library/os.html, https://docs.python.org/3/library/ast.html