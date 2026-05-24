---
name: context-map-mini-view
description: Antigravityは、ユーザーが現在作業中のファイルやディレクトリの関係性や役割を把握したいとき、またはプロジェクト全体の構造を素早く俯瞰したいときにこのSkillを発動します。キーワード例: "プロジェクト全体像", "依存関係", "ファイルの役割", "影響範囲"。
---

# 機能概要
context-map-mini-viewは、プロジェクトの主要なファイル・ディレクトリ構成や役割、各要素間の関連性を自動で抽出・要約し、作業中に即座に俯瞰できるミニビューを表示するSkillです。これにより、初見のリポジトリや複雑なプロジェクトでも迷子にならず、今開いているファイルの位置づけや影響範囲を一目で把握できます。READMEやPROJECT_MAPなど既存のドキュメントも活用し、コンテキスト理解を強力にサポートします。

# 使い方
このSkillは明示的なコマンド呼び出しは不要で、"全体構造を見たい"、"このファイルの役割は?"、"依存関係を教えて"などの発言や、README/PROJECT_MAP/ディレクトリツリーの確認要求などのキーワードで自動発動します。暗黙的なトリガー例:
- このプロジェクトの全体像を教えて
- 今開いているファイルの役割と関連ファイルは?
- 依存関係や主要ディレクトリを俯瞰したい

# 出力例
```
[Context Map Mini View]
- src/: アプリ本体のロジック (main.py, utils/)
- tests/: テストコード (pytest)
- README.md: プロジェクト概要
- requirements.txt: 依存パッケージ

[main.py] ← あなたが開いているファイル
  └─ utils/helpers.py: 補助関数
  └─ data/: 入力データ格納先
```

# 注意点
- 除外パス(.git, venv, node_modules等)は自動でフィルタします。
- 巨大なリポジトリでは主要ファイルのみ抽出・要約します。
- ローカルのREADMEやPROJECT_MAPが無い場合はディレクトリ構造から推定します。
- 出力は一時的な表示で、ローカルに保存はしません。

# 参考資料
- references/design_notes.md
- 公式: https://docs.python.org/3/library/os.html, https://docs.python.org/3/library/ast.html