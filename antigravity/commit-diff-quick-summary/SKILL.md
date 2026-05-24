---
name: commit-diff-quick-summary
description: コミット前の git diff や staged changes を自動要約したいとき、または "差分要約" や "変更点確認" などのキーワードがプロンプトや指示に含まれる場合に発動します。変更点の見落とし防止やレビュー効率化が求められる場面で有効です。
---

# 機能概要
`commit-diff-quick-summary` は、Gitリポジトリ内でコミット前の差分（staged/uncommitted changes）をAIが自動要約し、主要な変更点や影響範囲を端的に表示するSkillです。これにより、開発者は手動でdiffを精読する手間を省き、不要な変更や意図しない修正の混入を未然に防ぐことができます。日本語・英語を問わず高精度な要約が期待でき、ワークフローに追加ファイル不要で即時導入可能です。

# 使い方
明示的な呼び出しは不要で、"差分要約" "コミット前確認" "変更点をまとめて" などのキーワードがプロンプトや指示に含まれると自動発動します。ローカルで `python diff_quick_summary.py summary` を実行することで、現在のgit差分要約を即座に表示できます。

# 出力例
```
$ python diff_quick_summary.py summary
主要な変更点:
- src/utils.py: バグ修正（Nullチェック追加）
- docs/usage.md: 使用例セクションを更新
- tests/test_utils.py: 新規テストケースを追加
影響範囲: ユーティリティ関数利用箇所、ドキュメント参照箇所
不要なファイル変更は検出されませんでした
```

# 注意点
- 大規模な差分やバイナリファイルは要約対象外です
- .gitignore で除外されたファイルは自動的に無視されます
- 要約結果はローカルに保存されません
- AI要約のため100%の精度は保証されません。重要な変更は手動確認も推奨します

# 参考資料
- [git diff 公式ドキュメント](https://git-scm.com/docs/git-diff)
- references/design_notes.md 参照